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

---
# Motivation

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

---
# Experimental Setup
This section follows the terminology and conventions outlined in the accompanying paper.  
For a more detailed understanding of the methodology and experimental design, please refer to the paper.

## Sensors overview
| <img src="repo_images/experimental_setup.png" alt="Experimental Setup" align="left" width="50%"> | **Platform and robotic arm**  <br> [🔹 Clearpath Husky A200 UGV](https://clearpathrobotics.com/husky/)  <br> [🔹 Universal Robots UR5e Robotic Arm](https://www.universal-robots.com/products/ur5e/) <br><br> <span style="color:red;"><b>Platform sensor suite</b></span>  <br> [🔹 Livox Mid-360 LiDAR](https://www.livoxtech.com/mid-360)  <br> [🔹 Sevensense Core Research Module](https://github.com/sevensense-robotics/core_research_manual)  <br> [🔹 Microstrain 3DM-GV7-AR IMU](https://www.microstrain.com/inertial-sensors/3dm-gv7-ar)  <br><br> <span style="color:#003366;"><b>Robotic arm sensor suite</b></span>  <br> [🔹 Teledyne FLIR Boson 640](https://www.flir.com/products/boson/?model=20640A095&vertical=lwir&segment=oem)  <br> [🔹 Alvium 1800 U-130 VSWIR](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/130-vswir/)  <br> [🔹 Alvium 1800 U-240](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/240/)  <br> [🔹 Livox AVIA](https://www.livoxtech.com/avia) |
|:---------------------------------------------:|:----------------------------------------------:|
## Sensors setup

 *[Mario] IMAGE WITH TF POSITIONIGN TO BE ADDED :) *

---
# Environments and sequences
The dataset was collected across **3 distinct tracks**, each designed to represent a demining scenario with varying terrain and environmental conditions. 
These tracks contain a diverse set of targets, positioned to challenge algorithms development.
The figures represents a top-view pointcloud distribution of the targets along the track.

<p align="center">
  <img src="repo_images/tracks_pointcloud_topview.png" alt="dataset_tracks_presentation" >
</p>

---
# Targets

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

---
# Calibration

[Mario] aggiungi

---
# Data

We release **2 sequences per track**, resulting in a total of **6 sequences**.  
The data is available in **three different formats**:

- 🗄 **ROS 2 Bags**
- 🗄 **ROS 2 Bags with Livox Custom Msg** 
- 🖼 **Images + Target Location Annotations**  



## ROS 2 Bags Structure

Each **ROS 2 Bag**, includes:

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

### **📌 Track 1**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/K2r4cdB3gJGdmKS) [19.1 GB]
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/WKgpJ5FbT68Z8BE) [19.6 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/bDFSDiEiZiSgEQ8) [75.3 GB] 
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/zLj9cAPEtXKHiwm) [77.9 GB]  


### **📌 Track 2**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/QMcps9zEwonBSw5) [15.1 GB] 
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/RmfDRxFAcoCb73a) [15.5 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/yTb7XRPYk2bT958) [68.9 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/EWXLWWkJH9c3oKX) [71 GB]  


### **📌 Track 3**
🔹 **Sequence 1**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/jxJ62mq8EErewLN) [5.5 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/j98Abz57Nf39RB7) [5.9 GB]  

🔹 **Sequence 2**:  
   - 🗂️ [ROS 2 Bag (Standard)](https://cloud.cylab.be/s/qoQReDy3RCJBL8c) [24.4 GB]  
   - 🗂️ [ROS 2 Bag (with Livox Custom Msg)](https://cloud.cylab.be/s/J9G54g52NZXyYW5) [26 GB]  


## Images + Target Location Annotations

You can download each folder containing images and target locations from the links below:

| **Track / Seq** | **RGB** | **SWIR** | **LWIR** |
|---------------------|-----------|------------|------------|
| **Track 1 - Seq 1** | [track_1_s1_rgb](https://cloud.cylab.be/s/z2dRbj8ZAw7nPrQ) [3.8 GB]| [track_1_s1_swir](https://cloud.cylab.be/s/mLd8p9QwixTzbJF) [1.2 GB]| [track_1_s1_lwir](https://cloud.cylab.be/s/5A4sq8Bjn8pmwe8) [671.0 MB]|
| **Track 1 - Seq 2** | [track_1_s2_rgb](#) | [track_1_s2_swir](#) | [track_1_s2_lwir](#) |
| **Track 2 - Seq 1** | [track_2_s1_rgb](https://cloud.cylab.be/s/ceoNXCjjsjm6GGc) [2.8 GB| [track_2_s1_swir](https://cloud.cylab.be/s/2B2Ny5dHfJtiaAJ) [872.5 MB]| [track_2_s1_lwir](https://cloud.cylab.be/s/EeJk4HZHnZLry2M) [521.3 MB]|
| **Track 2 - Seq 2** | [track_2_s2_rgb](#) | [track_2_s2_swir](#) | [track_2_s2_lwir](#) |
| **Track 3 - Seq 1** | ❌ | [track_3_s1_swir](https://cloud.cylab.be/s/7ki4axDPAZ9ebWi) [630.3 MB]| [track_3_s1_lwir](https://cloud.cylab.be/s/djQQfs6QCDgBdr6) [568.3 MB]|
| **Track 3 - Seq 2** | ❌ | [track_3_s2_swir](#) | [track_3_s2_lwir](#) |

Each folder (.zip) follows the naming convention:

```
track_(nt)_s(ns)_camera.zip
```
Where:  
- **(nt)** → Track number (**1, 2, 3**)  
- **(ns)** → Sequence number (**1, 2**)  
- **camera** → Image type (**rgb, swir, or lwir**)  

Each folder contains:  
- **📷 Images** → Stored in `.jpg` format  
- **📝 Annotations** → Corresponding `.txt` files  

The generic naming convention for each jpg/txt is:

```
track_(nt)_s(ns)_camera_timestampsec_timestampnanosec (.jpg / .txt)
```

The **YOLO bounding box format** is used for annotations of the targets position in the .txt files.  
Each ID corresponds to an object, and the **full ID description** can be found in the YAML file here:  
📄 **[Link to YAML File]** _(to be added later)_

---

# Target Location Annotations
