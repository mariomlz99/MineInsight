# [IEEE RA-L'25] MineInsight: A Multi-sensor Dataset for Humanitarian Demining Robotics in Off-Road Environments

### 📢 News 
<div style="height:80px; overflow-y:scroll; border:1px solid #ccc; padding:10px; border-radius:5px; background-color: #f9f9f9;">
  <ul>
    <li>📦 <strong>31 Jan 2026:</strong> The T2S1 RGB labels have been refined, resulting in 6,295 finalized labels and resolving inconsistencies in bounding box sizes caused by differences among labelers. This refinement process is ongoing for the remaining RGB sequences.</li>  
    <li>📦 <strong>28 Jan 2026:</strong> We have refined all VIS-SWIR sequence labels for the v2 release. This resulted in 14,766 cleaned labels and improved bounding box stability. Work on the RGB labels is ongoing.</li>    
    <li>🎯 <strong>21 Jan 2026:</strong> We are currently mass revising all of our VIS-SWIR and RGB labels to improve their precision. </li>
    <li>📦 <strong>11 Dec 2025:</strong> Published on IEEE RA-L.</li>
    <li>📦 <strong>5 Jun 2025:</strong> Initial dataset release on GitHub.</li>
  </ul>
</div>

---
<p align="center">
  <a href="https://rma.ac.be/en">
    <img src="repo_images/rma_logo.png" height="80" alt="RMA Logo">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.kuleuven.be/english/kuleuven">
    <img src="repo_images/kuleuven_logo.png" height="80" alt="KUL Logo">
  </a>
</p>

# Repository Index

- **[1]** [Motivation](#1-motivation)
- **[2]** [Experimental Setup](#2-experimental-setup)
  - [Sensors Overview](#sensors-overview)
  - [Sensors Coordinate Systems](#sensors-coordinate-systems)
- **[3]** [Environments and Sequences](#3-environments-and-sequences)
- **[4]** [Targets](#4-targets)
- **[5]** [Calibration](#5-calibration)
  - [Intrinsic Calibration](#intrinsic-calibration)
  - [Extrinsic Calibration](#extrinsic-calibration)
- **[6]** [Data](#6-data)
  - [ROS 2 Bags Structure](#ros-2-bags-structure)
  - [ROS 2 Bags Downloads](#ros-2-bags-downloads)
  - [Raw Images](#raw-images)
  - [Climatology](#climatology)
  - [Track 3 RGB Camera Failure](#track-3-rgb-camera-failure)
- **[7]** [Acknowledgments](#7-acknowledgments)
- **[8]** [Citation](#8-citation)
- **[9]** [License](#9-license)
- **[10]** [Related Work](#10-related-work)
<br> 
<!-- Cleaning line breakers -->

# [1] Motivation 

Landmines remain a persistent threat in conflict-affected regions, posing risks to civilians and impeding post-war recovery. Traditional demining methods are often slow, hazardous, and costly, necessitating the development of robotic solutions for safer and more efficient landmine detection. 

MineInsight is a publicly available multi-spectral dataset designed to support advancements in robotic demining and off-road navigation. It features a diverse collection of sensor data, including visible (RGB, monochrome), short-wave infrared (VIS-SWIR), long-wave infrared (LWIR), and LiDAR scans. The dataset includes dual-view sensor scans from both a UGV and its robotic arm, providing multiple viewpoints to mitigate occlusions and improve detection accuracy. 

With over <b>38,000 RGB frames</b>, <b>53,000 VIS-SWIR frames</b>, and <b>108,000 LWIR frames</b> recorded in both daylight and nighttime conditions, featuring <b>35 different targets</b> distributed along <b>3 tracks</b>, MineInsight serves as a benchmark for developing and evaluating detection algorithms. 

<!-- Line-breaker di pulizia tra il testo e l'immagine-->
<br> 
<!-- Line-breaker di pulizia tra il testo e l'immagine-->

<p align="center" style="font-size:12px;">
  <img src="repo_images/full_dataset_picture.png" alt="dataset_presentation_pic" >
</p>

# [2] Experimental Setup

This section follows the terminology and conventions outlined in the accompanying paper.  
For a more detailed understanding of the methodology and experimental design, please refer to the paper.

## Sensors Overview

<p align="center"> <img src="repo_images/sensors_setup_picture.jpg" alt="Experimental Setup" width="80%"> </p>


| **Platform and Robotic Arm** | **Platform Sensor Suite** | **Robotic Arm Sensor Suite** |
|-----------------------------|----------------------------|------------------------------|
| [Clearpath Husky A200 UGV](https://clearpathrobotics.com/husky/)  <br> [Universal Robots UR5e Robotic Arm](https://www.universal-robots.com/products/ur5e/)  | [Livox Mid-360 LiDAR](https://www.livoxtech.com/mid-360)  <br>[Sevensense Core Research Module](https://github.com/sevensense-robotics/core_research_manual)  <br> [Microstrain 3DM-GV7-AR IMU](https://www.microstrain.com/inertial-sensors/3dm-gv7-ar)  | [Teledyne FLIR Boson 640](https://www.flir.com/products/boson/?model=20640A095&vertical=lwir&segment=oem)  <br> [Alvium 1800 U-130 VSWIR](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/130-vswir/)  <br> [Alvium 1800 U-240](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/240/)  <br> [Livox AVIA](https://www.livoxtech.com/avia)  |


<br>

## Sensors Coordinate Systems

The coordinate systems (and their TF name) of all sensors in our platform are illustrated in the figure below.

> **Note:** The positions of the axis systems in the figure are approximate.  
> This visualization provides insight into the relative orientations between sensors,  
> whether in the **robotic arm sensor suite** or the **platform sensor suite**.

For the full transformation chain, refer to the following **ROS 2 topics** in the dataset:
- **`/tf_static`** → Contains static transformations between sensors.
- **`/tf`** → Contains dynamic transformations recorded during operation.


<p align="center">
  <img src="repo_images/sensors_references_figure.png" alt="tf_sens" width="100%">
</p>


# [3] Environments and Sequences

The dataset was collected across **3 distinct tracks**, each designed to represent a demining scenario with varying terrain and environmental conditions. 
These tracks contain a diverse set of targets, positioned to challenge algorithm development. 
The figure below represents a top-view pointcloud distribution of the targets along the tracks.

<p align="center">
  <img src="repo_images/tracks_pointcloud_topview.png" alt="dataset_tracks_presentation" >
</p>

## 3.1 Supplementary Material: Reference Data & Ground Truth

To support reproducibility and research into auto-labeling pipelines, we release the intermediate data used to generate our ground truth. This allows the community to study the "Reference Data Generation" process described in **Section IV.D** of our paper.

### 1. Reference Sequences (Raw Data)
We release the raw ROS 2 bags for the **3 Reference Sequences**. These sequences were recorded with AprilTags placed at every target location to facilitate precise pose estimation.

* **Note:** These bags are provided exactly as recorded (raw data) and have not been processed or topic-remapped like the main dataset sequences.

**Download:**
* [TRACK 1 Reference Sequence ROS 2 Bag](https://mineinsight.short.gy/I6o5dc)
* [TRACK 2 Reference Sequence ROS 2 Bag](https://mineinsight.short.gy/AQQXTH)
* [TRACK 3 Reference Sequence ROS 2 Bag](https://mineinsight.short.gy/8mgVoT)

### 2. AprilTag Ground Positions
We provide the ground truth position of each AprilTag stick relative to the reference frame map. These are released as JSON files. 

For details on how these were derived, please refer to **Section IV.D ("Reference data generation")** in the paper.

* [TRACK_1_REF.json](reference_sequences/TRACK_1_REF.json)
* [TRACK_2_REF.json](reference_sequences/TRACK_2_REF.json)
* [TRACK_3_REF.json](reference_sequences/TRACK_3_REF.json)

### 3. Automatic Labels (Pre-Refinement)
We also provide the **automatic label ground truth** generated by our pipeline before human supervision or further refinements. 

These labels were created by detecting AprilTags in the reference sequences, calculating their 3D pose via SLAM + ICP, and projecting them into the evaluation sequences (see **Section IV.D** of the paper for the full methodology).

Released as TXT files in a single folder for all tracks, these labels follow the naming convention detailed in **Section 6** of this repository to ensure temporal synchronization with the images.

* [Download AUTOMATIC LABELS](https://mineinsight.short.gy/l6T62i)

# [4] Targets

For each track, a **detailed inventory PDF** is available, providing the full list of targets along with their respective details.  
<p align="center">
  <img src="repo_images/target_pictures.png" alt="dataset_target_pictures" >
</p>
You can find them in the **tracks inventory** folder of this repository:

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
- `swir_camera_intrinsics.yaml` → VIS-SWIR camera  

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
- `swir_avia_extrinsics.yaml` → VIS-SWIR ↔ Livox AVIA  

**Note:**  
Intrinsic parameters are also included in the **extrinsics calibration files**, as they were evaluated using **raw camera images**.

# [6] Data


We release **2 sequences per track**, resulting in a total of **6 sequences**.  
The data is available in **three different formats**:

- 🗄️ **ROS 2 Bags**
- 🗄️ **ROS 2 Bags with Livox Custom Msg** 
- 📷 **Raw Images**  


## ROS 2 Bags Structure

Each **ROS 2 Bag**, includes:

<details>
  <summary>Click here to view all the topics with a detailed explaination</summary>

| Topic | Message Type | Description |
|-------------------------------|-----------------------------------|-----------------------------------------------------------|
| /allied_swir/image_raw/compressed | sensor_msgs/msg/CompressedImage | VIS-SWIR camera raw image |
| /allied_swir/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | VIS-SWIR camera rectified image |
| /allied_rgb/image_raw/compressed | sensor_msgs/msg/CompressedImage | RGB camera raw image |
| /allied_rgb/image_raw/rectified/compressed | sensor_msgs/msg/CompressedImage | RGB camera rectified image |
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

For installation instructions, please take a look at the documentation in the respective repositories.

## ROS 2 Bags Downloads

We provide the raw data in two formats. **Standard** bags use standard ROS 2 message type (PointCloud2), while **Livox Custom Msg** bags include the raw driver data for users who need the raw polar coordinate data.

| **Track / Seq** | **Standard ROS 2 Bag** | **Livox Custom Msg Bag** |
|:---|:---|:---|
| **Track 1 - Seq 1** | [Download](https://mineinsight.short.gy/hvMRPa) `19.1 GB` | [Download](https://mineinsight.short.gy/nZkpxH) `19.6 GB` |
| **Track 1 - Seq 2** | [Download](https://mineinsight.short.gy/IHmkB6) `75.3 GB` | [Download](https://mineinsight.short.gy/LDd1Bx) `77.9 GB` |
| **Track 2 - Seq 1** | [Download](https://mineinsight.short.gy/YY9Swf) `15.1 GB` | [Download](https://mineinsight.short.gy/5IAGR4) `15.5 GB` |
| **Track 2 - Seq 2** | [Download](https://mineinsight.short.gy/pciT5I) `68.9 GB` | [Download](https://mineinsight.short.gy/0MfPRY) `71.0 GB` |
| **Track 3 - Seq 1** | [Download](https://mineinsight.short.gy/5qRJQV) `5.5 GB` | [Download](https://mineinsight.short.gy/CgLNGg) `5.9 GB` |
| **Track 3 - Seq 2** | [Download](https://mineinsight.short.gy/vfHjPD) `24.4 GB` | [Download](https://mineinsight.short.gy/aAmgvU) `26.0 GB` |


## Raw Images and Labels

| **Track / Seq** | **RGB Data** | **VIS-SWIR Data** | **LWIR Data** |
| :--- | :--- | :--- | :--- |
| **Track 1 - Seq 1** | 🖼️ **[Images](https://mineinsight.short.gy/6Mvbjx)** `3.8 GB`<br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)** `sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/WsrVwa)** `4.8 MB`| 🖼️ **[Images](https://mineinsight.short.gy/bYB63R)** `465 MB` <br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)**`sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/zbxef4)** `1.2 MB`| 🖼️ **[Images](https://mineinsight.short.gy/LV5XZ1)** `669 MB` <br>🏷️ **[Reproj. Labels](https://mineinsight.short.gy/W4Idj5)**`sizeof`<br>🏷️ **[Auto Labels](YOUR_LINK_HERE)** `sizeof`|
| **Track 1 - Seq 2** | 🖼️ **[Images](https://mineinsight.short.gy/RBRY3I)** `12.0 GB` <br>🏷️ **[Labels](YOUR_LINK_HERE)**`sizeof`<br>🎭 *Masks Coming Soon* | 🖼️ **[Images](https://mineinsight.short.gy/rB9si6)** `4.2 GB` <br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)**`sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/8mLBb1)** `7.5 MB`| 🖼️ **[Images](https://mineinsight.short.gy/PYfYwf)** `3.0 GB` <br>🏷️ **[Reproj. Labels](YOUR_LINK_HERE)** `sizeof`<br>🏷️ **[Auto Labels](YOUR_LINK_HERE)** `sizeof`|
| **Track 2 - Seq 1** | 🖼️ **[Images](https://mineinsight.short.gy/OKXGyT)** `2.8 GB` <br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)** `sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/T1FSPQ)** | 🖼️ **[Images](https://mineinsight.short.gy/ZoJg2h)** `872 MB` <br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)** `sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/t6S5Sy)** `1 MB`| 🖼️ **[Images](https://mineinsight.short.gy/Tkb2ra)** `520 MB` <br>🏷️ **[Reproj. Labels](null)** `sizeof`<br>🏷️ **[Auto Labels](null)** `sizeof`|
| **Track 2 - Seq 2** | 🖼️ **[Images](https://mineinsight.short.gy/mZSLV8)** `15.8 GB` <br>🏷️ **[Labels](YOUR_LINK_HERE)**<br>🎭 *Masks Coming Soon* | 🖼️ **[Images](https://mineinsight.short.gy/DIObFu)** `2.9 GB` <br>🏷️ **[Labels (v2)](YOUR_LINK_HERE)** `sizeof`<br>🎭 **[Masks (auto)](https://mineinsight.short.gy/AHS1OK)** `6 MB`| 🖼️ **[Images](https://mineinsight.short.gy/CuoFOX)** `2.3 GB` <br>🏷️ **[Reproj. Labels](YOUR_LINK_HERE)** `sizeof`<br>🏷️ **[Auto Labels](YOUR_LINK_HERE)** `sizeof`|
| **Track 3 - Seq 1** | <br><p align="center">❌<br>*(Not Available)*</p> | 🖼️ **[Images](https://mineinsight.short.gy/aX73E)** `630 MB` <br>🏷️ **[Labels](YOUR_LINK_HERE)** `sizeof` <br>🎭 *Masks N/A* | 🖼️ **[Images](https://mineinsight.short.gy/UoD78c)** `566 MB GB` <br>🏷️ **[Reproj. Labels](YOUR_LINK_HERE)** `sizeof`<br>🏷️ **[Auto Labels](YOUR_LINK_HERE)** `sizeof` |
| **Track 3 - Seq 2** | <br><p align="center">❌<br>*(Not Available)*</p> | 🖼️ **[Images](https://mineinsight.short.gy/ewHM2o)** `2.6 GB` <br>🏷️ **[Labels](YOUR_LINK_HERE)** `sizeof`<br>🎭 *Masks N/A* | 🖼️ **[Images](https://mineinsight.short.gy/1XFhHc)** `2.0 GB` <br>🏷️ **[Reproj. Labels](YOUR_LINK_HERE)** `sizeof`<br>🏷️ **[Auto Labels](YOUR_LINK_HERE)** `sizeof` |

> **Key:** 🖼️: Images | 🏷️: Annotations | 🎭 Segmentation (SAM2)

### 📝 Data Format & Notes

#### **1. Directory Structure**
Each archive (`.zip`) follows the naming convention: `track_(nt)_s(ns)_camera_(type).zip`.
* **(nt)** → Track number (`1, 2, 3`)
* **(ns)** → Sequence number (`1, 2`)
* **camera** → Sensor (`rgb, swir, lwir`)
* **type** → Type of resource (`images, labels`) and only for LWIR (`labels_reproj, labels_auto`)


Inside, files are named: `track_(nt)_s(ns)_camera_timestampsec_timestampnanosec (.jpg / .txt)`

#### **2. Annotation Formats**
* **Bounding Boxes (YOLOv8):**
    Target positions are provided in `.txt` files:
    ```
    <class_id> <x_center> <y_center> <width> <height>
    ```
    **Classes list:** [tracks_inventory/targets_list.yaml](tracks_inventory/targets_list.yaml)

* **SAM2 Masks (Segmentation):**
    * **Visuals:** White polygons on black backgrounds (`.png`).
    * **Structure:** Subfolders by object ID (e.g., `/id_1/`).
    * **Disclaimer:** These are **raw auto-generated masks** used as initial guesses. They are not manually corrected and may contain noise (debris, vegetation) or temporal jitter.

#### **⚠️ Note on Thermal (LWIR) Labels**
Thermal annotations come in two variants:
1.  **Reprojected (Manual Verification):** Generated by projecting manual RGB/SWIR labels onto the thermal view. Limitations include lack of absolute precision and dependency on the source sensor's FOV.
2.  **Automatic:** Generated via algorithmic detection.

* **Track 3 Limitation:** Due to the absence of RGB, Track 3 reconstruction relied on the narrow FOV of the VIS-SWIR sensor under night conditions.

## Climatology  

We provide the **climatology data** for the two key days surrounding the test campaign:  

📄 [Climatology 29 & 30 Oct 2024.xlsx](data/Climatology%20_29_30_October_2024.xlsx)

**29 October 2024** → the day **before** the campaign, when targets were placed on the soil at around **09:00 AM local time**. 
**30 October 2024** → the day **of the campaign**, when sensor measurements were conducted.  

The full Excel file contains **minute-by-minute measurements** collected across both days. These measurements are useful for processing the thermal camera data, as they allow correlation between atmospheric and surface conditions and thermal imaging performance.  

### Parameters Provided  

The following parameters are available in the dataset (in the order of the Excel file):  

| Parameter                        | Unit     |
|----------------------------------|----------|
| Time                             | HH:MM:SS |
| Wind force (10 m)                | kt       |
| Wind gusts                       | kt       |
| Wind direction                   | ° (deg)  |
| Air temperature                  | °C       |
| T –5 cm (soil)                   | °C       |
| T –10 cm (soil)                  | °C       |
| T –20 cm (soil)                  | °C       |
| T –50 cm (soil)                  | °C       |
| Road surface temperature         | °C       |
| Grass surface temperature        | °C       |
| Dew point temperature            | °C       |
| Relative Humidity (HR)           | %        |
| Pressure                         | hPa      |
| Clouds (octas @ height @ type)   | –        |
| Total clouds                     | octas    |
| Precipitation quantity (1 min)   | mm       |
| Precipitation quantity (1 hour)  | mm       |
| Precipitation quantity (1 day)   | mm       |

### How to Use with Sequences  

To facilitate analysis, the table below shows the exact climatology time windows corresponding to each recorded sequence.  
All times refer to **30 October 2024** (campaign day).  

| Track | Sequence | Bag file start time (local) | Duration | Climatology window |
|-------|----------|-----------------------------|----------|---------------------|
| 1     | Seq 1    | 13:17:49                   | 4 min 12 s  | 13:17:49 → 13:22:01 |
| 1     | Seq 2    | 13:54:26                   | 19 min 58 s | 13:54:26 → 14:14:24 |
| 2     | Seq 1    | 15:16:35                   | 3 min 42.8 s | 15:16:35 → 15:20:17 |
| 2     | Seq 2    | 15:47:05                   | 14 min 46 s | 15:47:05 → 16:01:51 |
| 3     | Seq 1    | 17:42:19                   | 3 min 41.5 s | 17:42:19 → 17:46:00 |
| 3     | Seq 2    | 17:28:07                   | 13 min 18 s | 17:28:07 → 17:41:25 |

By aligning the timestamps of each **ROS 2 bag** with this climatology log, users can extract the environmental conditions (temperature, humidity, wind, etc.) at the exact moment of each recording.  

### Temperature Profiles (30 October 2024)

The figure below shows the **air and soil temperatures** (–5 cm, –10 cm, –20 cm, –50 cm) throughout the **campaign day (30 October 2024)**.  
**Red shaded regions** correspond to the time windows when each track sequence was recorded.  

<p align="center">
  <img src="repo_images/climatology_30_oct_24.png" alt="Temperature Profiles 30 Oct 2024" width="90%">
</p>

## Track 3 RGB Camera Failure  

During **Track 3 recordings** (30 October 2024), the **RGB camera experienced a progressive failure**.  

- The first part of the recording (starting at 17:28:07 and 17:42:19, see [Climatology section](#climatology)) already shows frames that would have been very dark, making it extremely difficult to detect any target or terrain details.  
- By the end of the sequences, the RGB feed would have been completely black, given the near-nighttime conditions. 
- This issue affects both **Sequence 1 (3 min 41.5 s)** and **Sequence 2 (13 min 18 s)**.  

We recovered the bag metadata and extracted a short video from the RGB camera illustrating the Track 3 illumination condition at the beginning of the recordings:  

<p align="center">
  <img src="repo_videos/track3_rgb_failure_preview_12s.gif" width="70%">
</p>

# [7] Acknowledgments  

The authors thank **Alessandra Miuccio** and **Timothée Fréville** for their support in the hardware and software design.  
They also thank **Sanne Van Hees** and **Jorick Van Kwikenborne** for their assistance in organizing the measurement campaign.
Finally, they thank the **Belgian Meteo Wing** for providing the climatology study during the days of the test campaign. 

# [8] Citation

If you use MineInsight in your own work, please cite the accompanying paper:
```
@article{11297788,
  author={Malizia, Mario and Hamesse, Charles and Hasselmann, Ken and De Cubber, Geert and Tsiogkas, Nikolaos and Demeester, Eric and Haelterman, Rob},
  journal={IEEE Robotics and Automation Letters}, 
  title={MineInsight: A Multi-Sensor Dataset for Humanitarian Demining Robotics in Off-Road Environments}, 
  year={2026},
  volume={11},
  number={2},
  pages={1650-1657},
  doi={10.1109/LRA.2025.3643265}}
```
# [9] License

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.  
You are free to **share** and **adapt** this work **for non-commercial purposes**, as long as you **credit the authors** and **apply the same license** to any derivative works.

For full details, see:  
[CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)


# [10] Related Work
If you are interested in this dataset, you may also be interested in some of the related work:

* **PFM-1 Landmine Detection in Vegetation Using Thermal Imaging with Limited Training Data.** Malizia, Mario, Ken Hasselmann, Alessandra Miuccio, Rob Haelterman, Nikolaos Tsiogkas, and Eric Demeester. 2025. 
    *Proceedings of the 25th International Conference on Control, Automation and Systems (ICCAS)*, Incheon, South Korea, pp. 1864-1869. [https://doi.org/10.23919/ICCAS66577.2025.11301116](https://doi.org/10.23919/ICCAS66577.2025.11301116)
* **Multimodal Ensemble with Verification Mechanism for Landmine Detection.** Melnykova, Nataliia, and Anna Vechirska. 2025. 
   *Science and Technology Today (Наука і техніка сьогодні)*, No. 9(50), pp. 939-948. [https://doi.org/10.52058/2786-6025-2025-9(50)-939-948](https://doi.org/10.52058/2786-6025-2025-9(50)-939-948)



<br>
<p align="center">
  <img src="https://api.visitorbadge.io/api/visitors?path=mariomlz99/mineinsight" alt="Visitors">
</p>
