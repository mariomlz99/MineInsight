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

MineInsight is a publicly available multi-spectral dataset designed to support advancements in robotic demining and off-road navigation. It features a diverse collection of sensor data, including visible (RGB, monochrome), short-wave infrared (SWIR), long-wave infrared (LWIR), and LiDAR scans. The dataset includes dual-view sensor scans from both an Unmanned Ground Vehicle (UGV) and its robotic arm, providing multiple viewpoints to mitigate occlusions and improve detection accuracy. 

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
<p align="left">
  <img src="repo_images/experimental_setup.png" alt="Experimental Setup" width="60%" style="float: left; margin-right: 20px;">
</p>

### Platform and robotic arm
🔹 [Clearpath Husky A200 UGV](https://clearpathrobotics.com/husky/)  
🔹 [Universal Robots UR5e Robotic Arm](https://www.universal-robots.com/products/ur5e/)  

### <span style="color:red;">Platform sensor suite</span>
🔹 [Livox Mid-360 LiDAR](https://www.livoxtech.com/mid-360)  
🔹 [Sevensense Core Research Module](https://github.com/sevensense-robotics/core_research_manual)  
🔹 [Microstrain 3DM-GV7-AR IMU](https://www.microstrain.com/inertial-sensors/3dm-gv7-ar)  

### <span style="color:#003366;">Robotic arm sensor suite</span>
🔹 [Teledyne FLIR Boson 640](https://www.flir.com/products/boson/?model=20640A095&vertical=lwir&segment=oem)  
🔹 [Alvium 1800 U-130 VSWIR](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/130-vswir/)  
🔹 [Alvium 1800 U-240](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-u/240/)  
🔹 [Livox AVIA](https://www.livoxtech.com/avia)  





