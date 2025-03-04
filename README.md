# MineInsight: A Multi-spectral Dataset for Humanitarian Demining Robotics in Off-Road Environments

<p align="center">
  <a href="https://www.rma.ac.be/en">
    <img src="repo_images/rma_logo.png" alt="RMA_Logo" height="80">
  </a>
  <a href="https://mecatron.rma.ac.be/">
    <img src="repo_images/ras_lab_logo.png" alt="RAS_Logo" height="70">
  </a>
  <a href="https://rma-4dpl.github.io/">
    <img src="repo_images/4dpl_logo_2.jpeg" alt="4DPL_Logo" height="80">
  </a>
</p>
<p align="center">
  <a href="https://www.kuleuven.be/english/kuleuven/">
    <img src="repo_images/kul_logo.png" alt="KUL_Logo" height="60">
  </a>
  <a href="https://iiw.kuleuven.be/onderzoek/acro">
    <img src="repo_images/acro_logo.jpg" alt="ACRO_Logo" height="60">
  </a>
</p>
<p align="center" style="font-size:12px;">
  <b>
    <a href="https://scholar.google.com/citations?hl=en&user=3fDazuEAAAAJ">Mario Malizia</a>¹, 
    <a href="https://scholar.google.com/citations?hl=en&user=19a7OPUAAAAJ">Charles Hamesse</a>¹, 
    <a href="https://scholar.google.com/citations?hl=en&user=iyEhyh4AAAAJ">Ken Hasselmann</a>¹
  </b>
</p>
<p align="center" style="font-size:12px;">
  <b>
    <a href="https://scholar.google.com/citations?hl=en&user=wYXEEZ0AAAAJ">Geert De Cubber</a>¹, 
    <a href="https://scholar.google.com/citations?hl=en&user=3VTZcT4AAAAJ">Nikolaos Tsiogkas</a>², 
    <a href="https://scholar.google.com/citations?user=QKw1XxAAAAAJ&hl=en">Eric Demeester</a>², 
    <a href="https://scholar.google.com/citations?user=OQJ8ctsAAAAJ&hl=en">Rob Haelterman</a>¹
  </b>
</p>
<p align="center" style="font-size:10px;">
  ¹ Royal Military Academy of Belgium,  ² KU Leuven  
</p>
<p align="center" style="font-size:10px;">
  📄 <a href="https://your-dataset-site.com">Website</a> | 📜 <a href="https://arxiv.org/abs/xxxxx">Paper</a> | 📂 <a href="https://github.com/your-repo">GitHub</a>
</p>
<!-- Cleaning line breakers -->
<br> 
<p align="center">---------</p>

# Repository Index

- [1️) Motivation](#1-motivation)
- [2️) Experimental Setup](#2-experimental-setup)
  - [🔹 Sensors Overview](#sensors-overview)
  - [🔹 Sensors Positioning](#sensors-positioning)
- [3️) Environments and Sequences](#3-environments-and-sequences)
- [4️) Targets](#4-targets)
- [5️) Calibration](#5-calibration)
  - [🔹 Intrinsic Calibration](#intrinsic-calibration)
  - [🔹 Extrinsic Calibration](#extrinsic-calibration)
- [6️) Data](#6-data)
  - [🔹 ROS 2 Bags Structure](#ros-2-bags-structure)
  - [🔹 ROS 2 Bags Downloads](#ros-2-bags-downloads)
  - [🔹 Raw Images](#raw-images)
- [7️) Target Location Annotations](#7-target-location-annotations)
  - [🔹 Using Raw Images](#target-location-using-raw-images)
  - [🔹 Using ROS 2 Bags](#target-location-using-ros-2-bags)
- [8️) Acknowledgments](#8-acknowledgments)
- [9️) Citation](#9-citation)
- [10) License](#10-license)
- [11) Related Work](#11-related-work)
<br> 
<!-- Cleaning line breakers -->

# [1] Motivation 

Landmines remain a persistent threat in conflict-affected regions, posing risks to civilians and impeding post-war recovery. Traditional demining methods are often slow, hazardous, and costly, necessitating the development of robotic solutions for safer and more efficient landmine detection. 

MineInsight is a publicly available multi-spectral dataset designed to support advancements in robotic demining and off-road navigation. It features a diverse collection of sensor data, including visible (RGB, monochrome), short-wave infrared (SWIR), long-wave infrared (LWIR), and LiDAR scans. The dataset includes dual-view sensor scans from both a UGV and its robotic arm, providing multiple viewpoints to mitigate occlusions and improve detection accuracy. 

With over <b>38,000 RGB frames</b>, <b>53,000 SWIR frames</b>, and <b>108,000 LWIR frames</b> recorded in both daylight and nighttime conditions, featuring <b>35 different targets</b> distributed along <b>3 tracks</b>, MineInsight serves as a benchmark for developing and evaluating detection algorithms. It also offers an estimation of object localization, supporting researchers in algorithm validation and performance benchmarking. 

MineInsight follows best practices from established robotic datasets and provides a valuable resource for the community to advance research in landmine detection, off-road navigation, and sensor fusion.


<!-- Line-breaker di pulizia tra il testo e l'immagine-->
<br> 
<!-- Line-breaker di pulizia tra il testo e l'immagine-->

<p align="center" style="font-size:12px;">
  <img src="repo_images/full_dataset_picture_with_names.png" alt="dataset_presentation_pic" >
</p>


# [2] Experimental Setup

This section follows the terminology and conventions outlined in the accompanying paper.  
For a more detailed understanding of the methodology and experimental design, please refer to the paper.

## Sensors Overview

<p align="center"> <img src="repo_images/experimental_setup.png" alt="Experimental Setup" width="50%"> </p>


| **Platform and Robotic Arm** | **Platform Sensor Suite** | **Robotic Arm Sensor Suite** |
|-----------------------------|----------------------------|------------------------------|
| [Clearpath Husky A200 UGV](https://clearpathrobotics.com/husky/)  <br> [Universal Robots UR5e Robotic Arm](https://www.universal-robots.com/products/ur5e/)  | [Livox Mid-360 LiDAR](https://www.livoxtech.com/mid-360)  <br>[Sevensense Core Research Module](https://github.com/sevensense-robotics/core_research_manual)  <br> [Microstrain 3DM-GV7-AR IMU](https://www.microstrain.com/inertial-sensors/3dm-gv7-ar)  | [Teledyne FLIR Boson 640](https://www.flir.com/products/boson/?model=20640A095&vertical=lwir&segment=oem)  <br> [Alvium 1800 U-130 VSWIR](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/130-vswir/)  <br> [Alvium 1800 U-240](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/240/)  <br> [Livox AVIA](https://www.livoxtech.com/avia)  |



<br>

## Sensors Positioning

 *[Mario] IMAGE WITH TF POSITIONIGN TO BE ADDED :) *


# [3] Environments and Sequences


The dataset was collected across **3 distinct tracks**, each designed to represent a demining scenario with varying terrain and environmental conditions. 
These tracks contain a diverse set of targets, positioned to challenge algorithms development.
The figures represents a top-view pointcloud distribution of the targets along the track.

<p align="center">
  <img src="repo_images/tracks_pointcloud_topview.png" alt="dataset_tracks_presentation" >
</p>

# [4] Targets

For each track, a **detailed inventory PDF** is available, providing the full list of targets along with their respective details.  
You can find them in the **`tracks_inventory`** folder of this repository:

<p align="center">
  📄 <a href="tracks_inventory/track_1_targets.pdf">Track 1 Inventory</a> &nbsp;|&nbsp; 
  📄 <a href="tracks_inventory/track_2_targets.pdf">Track 2 Inventory</a> &nbsp;|&nbsp; 
  📄 <a href="tracks_inventory/track_3_targets.pdf">Track 3 Inventory</a>
</p>

Each PDF catalogs each item with:

- **ID:** Unique identifier for each target;  
- **Name:** Official name of the target;  
- **Image:** A visual reference of the object for recognition;  
- **[CAT-UXO link](https://www.cat-uxo.com/)**: Detailed explanation of the target (available only for landmines).  


# [5] Calibration

The dataset includes **intrinsic** and **extrinsic** calibration files for all cameras and LiDARs.

## Intrinsic Calibration

**`intrinsics_calibration/`**  
- `lwir_camera_intrinsics.yaml` → LWIR camera  
- `rgb_camera_intrinsics.yaml` → RGB camera  
- `sevensense_cameras_intrinsics.yaml` → Sevensense grayscale cameras  
- `swir_camera_intrinsics.yaml` → SWIR camera  

<!-- Each file contains:  
- **Camera matrix** (`fx`, `fy`, `cx`, `cy`)  
- **Distortion coefficients** (and distortion model used)  
- **Image resolution**  
- **Projection matrix**   -->

## Extrinsic Calibration

**`extrinsics_calibration/`**  
- `lwir_avia_extrinsics.yaml` → LWIR ↔ Livox AVIA  
- `rgb_avia_extrinsics.yaml` → RGB ↔ Livox AVIA  
- `sevensense_mid360_extrinsics.yaml` → Sevensense ↔ Livox Mid-360  
- `swir_avia_extrinsics.yaml` → SWIR ↔ Livox AVIA  

**Note:**  
Intrinsic parameters are also included in the **extrinsics calibration files**, as they were evaluated using **raw camera images**.

# [6] Data


We release **2 sequences per track**, resulting in a total of **6 sequences**.  
The data is available in **three different formats**:

- 🗄 **ROS 2 Bags**
- 🗄 **ROS 2 Bags with Livox Custom Msg** 
- 🖼 **Raw Images**  


## ROS 2 Bags Structure

Each **ROS 2 Bag**, includes:

<details>
  <summary>Click here to view all the topics with a detailed explaination</summary>

| Topic | Message Type | Description |
|-------------------------------|-----------------------------------|-----------------------------------------------------------|
| /allied_swir/image_raw/compressed | sensor_msgs/msg/CompressedImage | SWIR camera raw image |
| /allied_swir/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | SWIR camera rectified image |
| /alphasense/cam_0/image_raw/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 0 raw image |
| /alphasense/cam_0/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 0 rectified image |
| /alphasense/cam_1/image_raw/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 1 raw image |
| /alphasense/cam_1/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 1 rectified image |
| /alphasense/cam_2/image_raw/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 2 raw image |
| /alphasense/cam_2/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 2 rectified image |
| /alphasense/cam_3/image_raw/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 3 raw image |
| /alphasense/cam_3/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 3 rectified image |
| /alphasense/cam_4/image_raw/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 4 raw image |
| /alphasense/cam_4/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | Sevensense Core Greyscale camera 4 rectified image |
| /alphasense/imu | sensor_msgs/msg/Imu | IMU data from Sevensense Core |
| /avia/livox/imu | sensor_msgs/msg/Imu | IMU data from Livox AVIA LiDAR |
| /avia/livox/lidar/pointcloud2 | sensor_msgs/msg/PointCloud2 | Point cloud data from Livox AVIA LiDAR |
| /flir/thermal/compressed | sensor_msgs/msg/CompressedImage | LWIR camera raw image |
| /flir/thermal/rectified/compressed | sensor_msgs/msg/CompressedImage | LWIR camera rectified image |
| /flir/thermal/colorized/compressed | sensor_msgs/msg/CompressedImage | LWIR camera raw image with colorized overlay |
| /flir/thermal/rectified/colorized/compressed | sensor_msgs/msg/CompressedImage | LWIR camera rectified image with colorized overlay |
| /microstrain/imu | sensor_msgs/msg/Imu | IMU data from Microstrain (internal) |
| /mid360/livox/imu | sensor_msgs/msg/Imu | IMU data from Livox Mid-360 LiDAR |
| /mid360/livox/lidar/pointcloud2 | sensor_msgs/msg/PointCloud2 | Point cloud data from Livox Mid-360 LiDAR |
| /odometry/filtered | nav_msgs/msg/Odometry | Filtered odometry data (ROS 2 localization, fusion output ) |
| /odometry/wheel | nav_msgs/msg/Odometry | Wheel odometry data from UGV wheel encoder |
| /tf | tf2_msgs/msg/TFMessage | Real-time transformations between coordinate frames |
| /tf_static | tf2_msgs/msg/TFMessage | Static transformations |

</details>

If you are downloading a **ROS 2 Bag with Livox Custom Msg**, you will find the following additional topics:

| Topic | Message Type | Description |
|------------------------------|--------------------------------|------------------------------------------------|
| /avia/livox/lidar | livox_interfaces/msg/CustomMsg | Raw point cloud data from Livox AVIA LiDAR in custom Livox format |
| /mid360/livox/lidar | livox_ros_driver2/msg/CustomMsg | Raw point cloud data from Livox Mid-360 LiDAR in custom Livox format |

**Note:**
These messages include timestamps for each point in the point cloud scan.  
To correctly **decode and use** these messages, install the official Livox drivers:  

- **Livox AVIA** (🔗 [livox_ros2_driver](https://github.com/Livox-SDK/livox_ros2_driver))  
- **Livox Mid-360** (🔗 [livox_ros_driver2](https://github.com/Livox-SDK/livox_ros_driver2))  

For installation instructions, refer to the documentation in the respective repositories.

## ROS 2 Bags Downloads

You can download the datasets from the links below:

### **Track 1**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/K2r4cdB3gJGdmKS) [19.1 GB]
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/WKgpJ5FbT68Z8BE) [19.6 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/bDFSDiEiZiSgEQ8) [75.3 GB] 
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/zLj9cAPEtXKHiwm) [77.9 GB]  


### **Track 2**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/QMcps9zEwonBSw5) [15.1 GB] 
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/RmfDRxFAcoCb73a) [15.5 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/yTb7XRPYk2bT958) [68.9 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/EWXLWWkJH9c3oKX) [71 GB]  


### **Track 3**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/jxJ62mq8EErewLN) [5.5 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/j98Abz57Nf39RB7) [5.9 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/qoQReDy3RCJBL8c) [24.4 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/J9G54g52NZXyYW5) [26 GB]  


## Raw Images

You can download each folder containing the images from the links below:

| **Track / Seq** | **RGB** | **SWIR** | **LWIR** |
|---------------------|-----------|------------|------------|
| **Track 1 - Seq 1** | [track_1_s1_rgb](https://cloud.cylab.be/s/z2dRbj8ZAw7nPrQ) [3.8 GB]| [track_1_s1_swir](https://cloud.cylab.be/s/mLd8p9QwixTzbJF) [1.2 GB]| [track_1_s1_lwir](https://cloud.cylab.be/s/5A4sq8Bjn8pmwe8) [671.0 MB]|
| **Track 1 - Seq 2** | [track_1_s2_rgb](https://cloud.cylab.be/s/JSFsP6MjLeXtPyT) [12.7 GB]| [track_1_s2_swir](https://cloud.cylab.be/s/r59srt8DZqktee8) [4.2 GB]| [track_1_s2_lwir](https://cloud.cylab.be/s/oiAx9Ke4kKarxgx) [3.1 GB]|
| **Track 2 - Seq 1** | [track_2_s1_rgb](https://cloud.cylab.be/s/ceoNXCjjsjm6GGc) [2.8 GB]| [track_2_s1_swir](https://cloud.cylab.be/s/2B2Ny5dHfJtiaAJ) [872.5 MB]| [track_2_s1_lwir](https://cloud.cylab.be/s/EeJk4HZHnZLry2M) [521.3 MB]|
| **Track 2 - Seq 2** | [track_2_s2_rgb](https://cloud.cylab.be/s/7jnJEiMCBKx7Wbe) [15.8 GB]| [track_2_s2_swir](https://cloud.cylab.be/s/ernwP2FQeLdsDZ5) [2.9 GB]| [track_2_s2_lwir](https://cloud.cylab.be/s/tRJ9QEMgpf4KWPa) [2.3 GB]|
| **Track 3 - Seq 1** | <p align="center">❌</p> | [track_3_s1_swir](https://cloud.cylab.be/s/7ki4axDPAZ9ebWi) [630.3 MB]| [track_3_s1_lwir](https://cloud.cylab.be/s/djQQfs6QCDgBdr6) [568.3 MB]|
| **Track 3 - Seq 2** | <p align="center">❌</p> | [track_3_s2_swir](https://cloud.cylab.be/s/33rpTt4pbGrirsi) [2.6 GB]| [track_3_s2_lwir](https://cloud.cylab.be/s/obeexpcziiayyKG) [2.0 GB]|

Each folder (.zip) follows the naming convention:

```
track_(nt)_s(ns)_camera.zip
```
Where:  
- **(nt)** → Track number (**1, 2, 3**)  
- **(ns)** → Sequence number (**1, 2**)  
- **camera** → Image type (**rgb, swir, or lwir**)  



# [7] Target Location Annotations


Each target location is estimated for each sequence of each track (refer to the paper for this estimation).
The estimation of the target locations can be found according to the data you are using:

## Target Location Using Raw Images:

The target locations are already included in the folder downloaded in the previous sections [add hyperlink].


Each folder contains:  
- **Images** → Stored in `.jpg` format  
- **Annotations** → Corresponding `.txt` files  

The generic naming convention for each jpg/txt is:

```
track_(nt)_s(ns)_camera_timestampsec_timestampnanosec (.jpg / .txt)
```

The **YOLOv5 / YOLOv8 format** is used for annotations of the targets position in the .txt files.  

```
<class_id> <x_center> <y_center> <width> <height>
```
Each ID corresponds to an object, and the **full ID description** can be found in the YAML file:  
[`targets_list.yaml`](target_location_ros2_bags/tracks_targets_list/targets_list.yaml)

## Target Location Using ROS 2 Bags:
The code inside [`target_location_ros2_bags`](target_location_ros2_bags) allows you to localize targets in images by reprojecting 3D point cloud data onto image frames.
It supports RGB, SWIR, and LWIR cameras, automatically handling bounding boxes, timestamps, and target labeling.

### Folder Structure:

```
📂 target_location_ros2_bags/
│── 📂 param/                 # Configuration YAML files
│── 📂 target_locations_csv/   # CSV files with target locations
│── 📂 tracks_targets_list/    # YAML mapping target IDs to labels
│── ros2_bag_targets_display.py  # Main Python script
```


**Note:** For simplicity, the **`params.yaml`** file repeats the extrinsics and part of the intrinsics of each camera, avoiding dependencies on other configuration files higher in the repository hierarchy.


### How to run:
1) Set up the environment (Ensure ROS 2 and dependencies are installed):

```
source /opt/ros/$DISTRO/setup.bash
pip install numpy pandas opencv-python pyyaml scipy
```
2) Modify the configuration (Check param/params.yaml for bag path, CSV file, and camera topic you want to process).

3) Run the script to process the bag and display results:

```
python3 ros2_bag_targets_display.py
```

# [8] Acknowledgments  

The authors thank **Alessandra Miuccio** and **Timothée Fréville** for their support in the **hardware and software design**.  
They also thank **Sanne Van Hees** and **Jorick Van Kwikenborne** for their assistance in **organizing the measurement campaign**.

# [9] Citation


# [10] License

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.  
You are free to **share** and **adapt** this work **for non-commercial purposes**, as long as you **credit the authors** and **apply the same license** to any derivative works.

For full details, see:  
[CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)


# [11] Related Work

