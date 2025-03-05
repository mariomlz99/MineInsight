import yaml
import cv2
import numpy as np
import pandas as pd
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
from scipy.spatial.transform import Rotation as R
from pathlib import Path

class CSVPointReprojection:
    def __init__(self, yaml_file_path):
        self.config = self.load_yaml(yaml_file_path)
        self.bag_file = self.config["bag_file_path"]
        self.csv_file = self.config["csv_file_path"]
        self.camera_topic = self.config["camera_topic"]
        self.rotate_image_180 = self.config.get("rotate_image_180", False)
        self.intrinsics = self.config["intrinsics"]
        self.extrinsics = self.config["extrinsics"]
        self.T_lidar_camera = self.get_transformation_matrix()
        self.bridge = CvBridge()
        self.points = self.read_points_from_csv()
        self.id_to_text = self.load_id_to_text()

    def load_yaml(self, yaml_path):
        try:
            with open(yaml_path, 'r') as file:
                return yaml.safe_load(file)
        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"Error loading YAML: {e}")
            return None

    def get_transformation_matrix(self):
        translation = np.array([
            self.extrinsics["translation"]["tx"],
            self.extrinsics["translation"]["ty"],
            self.extrinsics["translation"]["tz"]
        ])
        rotation = R.from_quat([
            self.extrinsics["rotation"]["rx"],
            self.extrinsics["rotation"]["ry"],
            self.extrinsics["rotation"]["rz"],
            self.extrinsics["rotation"]["rw"]
        ]).as_matrix()
        
        T = np.eye(4)
        T[:3, :3] = rotation
        T[:3, 3] = translation
        return T

    def load_id_to_text(self):
        mine_list_path = Path.cwd() / "tracks_targets_list" / "targets_list.yaml"

        try:
            with open(mine_list_path, 'r') as file:
                mine_data = yaml.safe_load(file)
            return {item['id']: item['text'] for track in mine_data.values() for item in track}
        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"Error loading ID mapping: {e}")
            return {}

    def read_points_from_csv(self):
        df = pd.read_csv(self.csv_file, header=None)
        df.columns = ["timestamp.sec", "timestamp.nanosec", "id", "x", "y", "z", "bbox_lwir", "bbox_rgb", "bbox_swir"]
        return df

    def find_closest_points(self, frame_sec, frame_nanosec):
        frame_timestamp = frame_sec + frame_nanosec * 1e-9
        self.points["timestamp"] = self.points["timestamp.sec"] + self.points["timestamp.nanosec"] * 1e-9
        self.points["time_diff"] = abs(self.points["timestamp"] - frame_timestamp)
        closest_points = self.points[self.points["time_diff"] == self.points["time_diff"].min()]

        # Select bounding box size based on camera topic (the last 3 col of the excel file)
        if "rgb" in self.camera_topic:
            bbox_column = "bbox_rgb"
        elif "swir" in self.camera_topic:
            bbox_column = "bbox_swir"
        elif "lwir" in self.camera_topic:
            bbox_column = "bbox_lwir"
        else:
            print("Unknown camera type, defaulting to 250px bbox")
            bbox_column = "bbox_rgb"

        return closest_points[["x", "y", "z", "id", bbox_column]].to_numpy()

    def process_bag(self):
        storage_options = StorageOptions(uri=self.bag_file, storage_id="sqlite3")
        converter_options = ConverterOptions(input_serialization_format="cdr", output_serialization_format="cdr")
        
        reader = SequentialReader()
        reader.open(storage_options, converter_options)

        topic_types = reader.get_all_topics_and_types()
        type_map = {topic.name: topic.type for topic in topic_types}

        while reader.has_next():
            topic, data, timestamp = reader.read_next()
            msg_type = get_message(type_map[topic])
            msg = deserialize_message(data, msg_type)

            if topic == self.camera_topic and isinstance(msg, CompressedImage):
                self.image_callback(msg)

    def image_callback(self, image_msg):
        frame_sec = image_msg.header.stamp.sec
        frame_nanosec = image_msg.header.stamp.nanosec
        closest_points = self.find_closest_points(frame_sec, frame_nanosec)
        self.reproject_points(image_msg, closest_points)
    
    def reproject_points(self, image_msg, points):
        try:
            image = self.bridge.compressed_imgmsg_to_cv2(image_msg)
        except Exception as e:
            print(f"Failed to decode image data: {e}")
            return

        if image is None:
            print("Image is empty")
            return

        output_image = image.copy()
        T_camera_lidar = np.linalg.inv(self.T_lidar_camera)

        fx, fy = self.intrinsics["fx"], self.intrinsics["fy"]
        cx, cy = self.intrinsics["cx"], self.intrinsics["cy"]

        for point in points:
            x, y, z, point_id, bbox_size = point  

            point_lidar = np.array([x, y, z, 1.0])
            point_camera = T_camera_lidar @ point_lidar

            if point_camera[2] <= 0:
                continue

            u = int((fx * point_camera[0] / point_camera[2]) + cx)
            v = int((fy * point_camera[1] / point_camera[2]) + cy)

            if 0 <= u < output_image.shape[1] and 0 <= v < output_image.shape[0]:
                box_width, box_height = int(bbox_size), int(bbox_size)
                top_left = (u - box_width // 2, v - box_height // 2)
                bottom_right = (u + box_width // 2, v + box_height // 2)

                # Draw bounding box on the image
                cv2.rectangle(output_image, top_left, bottom_right, (0, 0, 255), 2)

                # Display text based on ID
                point_text = self.id_to_text.get(int(point_id), f"ID: {int(point_id)}")
                text_position = (top_left[0], bottom_right[1] + 20)
                cv2.putText(
                    output_image, point_text, text_position,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
                )

        # If SWIR is true in YAML, rotate the image
        if self.rotate_image_180:
            output_image = cv2.rotate(output_image, cv2.ROTATE_180)

        cv2.imshow("Detected Targets", output_image)
        cv2.waitKey(1)

if __name__ == "__main__":
    yaml_file_path = Path.cwd() / "param" / "params.yaml"

    with open(yaml_file_path, 'r') as file:
        params = yaml.safe_load(file)

    reprojection = CSVPointReprojection(yaml_file_path)
    reprojection.process_bag()

    print(f"Loaded YAML file from: {yaml_file_path}")
    print(f"Using bag file: {params['bag_file_path']}")
