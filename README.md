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
## Motivation

Landmines remain a persistent threat in conflict-affected regions, posing risks to civilians and impeding post-war recovery. Traditional demining methods are often slow, hazardous, and costly, necessitating the development of robotic solutions for safer and more efficient landmine detection. 

MineInsight is a publicly available multi-spectral dataset designed to support advancements in robotic demining and off-road navigation. It features a diverse collection of sensor data, including visible (RGB, monochrome), short-wave infrared (SWIR), long-wave infrared (LWIR), and LiDAR scans. The dataset includes dual-view sensor scans from both a UGV and its robotic arm, providing multiple viewpoints to mitigate occlusions and improve detection accuracy. 

With over <b>38,000 RGB frames</b>, <b>53,000 SWIR frames</b>, and <b>108,000 LWIR frames</b> recorded in both daylight and nighttime conditions, featuring <b>35 different targets</b> distributed along <b>3 tracks</b>, MineInsight serves as a benchmark for developing and evaluating detection algorithms. It also offers an estimation of object localization, supporting researchers in algorithm validation and performance benchmarking. 

MineInsight follows best practices from established robotic datasets and provides a valuable resource for the community to advance research in landmine detection, off-road navigation, and sensor fusion.


<!-- Line-breaker di pulizia tra il testo e l'immagine-->
<br> 
<!-- Line-breaker di pulizia tra il testo e l'immagine-->

<p align="center">
  <img src="repo_images/full_dataset_picture_with_names.png" alt="dataset_presentation_pic" >
</p>

---
## Experimental Setup
This section follows the terminology and conventions outlined in the accompanying paper.  
For a more detailed understanding of the methodology and experimental design, please refer to the paper.

### Sensors overview
| <img src="repo_images/experimental_setup.png" alt="Experimental Setup" align="left" width="50%"> | **Platform and robotic arm**  <br> [🔹 Clearpath Husky A200 UGV](https://clearpathrobotics.com/husky/)  <br> [🔹 Universal Robots UR5e Robotic Arm](https://www.universal-robots.com/products/ur5e/) <br><br> <span style="color:red;"><b>Platform sensor suite</b></span>  <br> [🔹 Livox Mid-360 LiDAR](https://www.livoxtech.com/mid-360)  <br> [🔹 Sevensense Core Research Module](https://github.com/sevensense-robotics/core_research_manual)  <br> [🔹 Microstrain 3DM-GV7-AR IMU](https://www.microstrain.com/inertial-sensors/3dm-gv7-ar)  <br><br> <span style="color:#003366;"><b>Robotic arm sensor suite</b></span>  <br> [🔹 Teledyne FLIR Boson 640](https://www.flir.com/products/boson/?model=20640A095&vertical=lwir&segment=oem)  <br> [🔹 Alvium 1800 U-130 VSWIR](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/130-vswir/)  <br> [🔹 Alvium 1800 U-240](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/240/)  <br> [🔹 Livox AVIA](https://www.livoxtech.com/avia) |
|:---------------------------------------------:|:----------------------------------------------:|
### Sensors setup

 *[Mario] IMAGE WITH TF POSITIONIGN TO BE ADDED :) *

---
## Environments and sequences
The dataset was collected across **3 distinct tracks**, each designed to represent a demining scenario with varying terrain and environmental conditions. 
These tracks contain a diverse set of targets, positioned to challenge algorithms development.
The figure represents the tracks along with their targets' distribution.

<p align="center">
  <img src="repo_images/tracks_with_targets.png" alt="dataset_tracks_presentation" >
</p>

---
## Targets

For each track, a **detailed inventory PDF** is available, providing the full list of targets along with their respective details.  
You can find them in the **`tracks_inventory`** folder of this repository:

📄 [Track 1 Inventory](tracks_inventory/track_1_targets.pdf)  
📄 [Track 2 Inventory](tracks_inventory/track_2_targets.pdf)  
📄 [Track 3 Inventory](tracks_inventory/track_3_targets.pdf)

Each PDF catalogs each item with:

- **ID:** Unique identifier for each target;
- **Name:** Official name of the target;  
- **Image:** A visual reference of the object;  
- **[CAT-UXO](https://www.cat-uxo.com/) link** : Detailed explanation of the target (available only for landmines).

