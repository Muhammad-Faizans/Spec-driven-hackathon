---
sidebar_position: 2
---

# Hardware and Lab Requirements

This course is technically demanding, sitting at the intersection of three heavy computational loads: **Physics Simulation**, **Visual Perception (SLAM/Computer Vision)**, and **Generative AI (LLMs/VLA)**. The primary investment must be in High-Performance Workstations.

## 1. The "Digital Twin" Workstation (Required per Student)

This is the most critical component, as **NVIDIA Isaac Sim** requires **RTX (Ray Tracing)** capabilities. Standard laptops (MacBooks or non-RTX Windows machines) will not work.

| Component | Specification | Rationale |
| :--- | :--- | :--- |
| **GPU (The Bottleneck)** | NVIDIA RTX 4070 Ti (12GB VRAM) or higher. | Required for loading USD assets and running VLA models simultaneously. |
| **Ideal GPU** | RTX 3090 or 4090 (24GB VRAM) | Allows for smoother "Sim-to-Real" training cycles. |
| **CPU** | Intel Core i7 (13th Gen+) or AMD Ryzen 9. | Physics calculations (Rigid Body Dynamics) in Gazebo/Isaac are CPU-intensive. |
| **RAM** | 64 GB DDR5 (32 GB is the absolute minimum, but risks crashing). | Essential for complex scene rendering and multitasking. |
| **OS** | Ubuntu 22.04 LTS. | ROS 2 (Humble/Iron) is native to Linux. Dedicated Linux machines are mandatory for a friction-free experience. |

## 2. The "Physical AI" Edge Kit

This kit covers **Module 3 (Isaac ROS)** and **Module 4 (VLA)**, enabling students to set up the nervous system on a desk before deploying to a full robot.

| Component | Model / Role | Notes |
| :--- | :--- | :--- |
| **The Brain** | NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB). | Industry standard for embodied AI. Students deploy ROS 2 nodes here to understand resource constraints. |
| **The Eyes (Vision)** | Intel RealSense D435i or D455. | Provides RGB and Depth data, essential for VSLAM and Perception modules. |
| **The Inner Ear (Balance)** | Generic USB IMU (BNO055). | A separate module helps teach IMU calibration. |
| **Voice Interface** | Simple USB Microphone/Speaker array (e.g., ReSpeaker). | Used for the "Voice-to-Action" Whisper integration. |

## 3. The Robot Lab (Actuators)

For the physical part of the course, three tiers of options are available:

### Option A: The "Proxy" Approach (Recommended for Budget)

*   **Robot**: Unitree Go2 Edu (~$1,800 - $3,000).
*   **Pros**: Highly durable, excellent ROS 2 support, affordable enough for multiple units.
*   **Cons**: Not a biped (humanoid).

### Option B: The "Miniature Humanoid" Approach

*   **Robots**: Unitree G1 (~$16k) or Robotis OP3 (~$12k).
*   **Budget Alternative**: Hiwonder TonyPi Pro (~$600).
*   **Warning**: Cheap kits (Hiwonder) often use Raspberry Pi, which cannot run NVIDIA Isaac ROS efficiently.

### Option C: The "Premium" Lab (Sim-to-Real Specific)

*   **Robot**: Unitree G1 Humanoid.
*   **Why**: One of the few commercially available humanoids that can walk dynamically and has an SDK open enough for custom ROS 2 controllers.

## 4. Summary of Infrastructure Architecture

To teach this successfully, your lab should be integrated:

| Component | Hardware | Function |
| :--- | :--- | :--- |
| **Sim Rig** | PC with RTX 4080 + Ubuntu 22.04 | Runs Isaac Sim, Gazebo, Unity, and trains LLM/VLA models. |
| **Edge Brain** | Jetson Orin Nano | Runs the "Inference" stack. Students deploy their code here. |
| **Sensors** | RealSense Camera + Lidar | Connected to the Jetson to feed real-world data to the AI. |
| **Actuator** | Unitree Go2 or G1 (Shared) | Receives motor commands from the Jetson. |

## Option 2: The "Ether" Lab (Cloud-Native - High OpEx)

If RTX-enabled workstations are not available, the course can rely on cloud-based instances:

*   **Cloud Workstations**: Rent instances (e.g., AWS g5.2xlarge with A10G GPU).
*   **Estimated Cost**: ~$205 per student per quarter (for 120 hours of usage).
*   **Local Hardware Still Required**: You still need the **Edge AI Kits** (e.g., Jetson) for the physical deployment phase and at least one **physical robot** for the final demo, due to latency issues in controlling real hardware from the cloud. Training is done in the cloud, models are downloaded, and then flashed to the local Jetson kit for deployment.

### The Economy Jetson Student Kit

For core ROS 2 and basic vision learning:

| Component | Model | Price (Approx.) | Notes |
| :--- | :--- | :--- | :--- |
| **The Brain** | NVIDIA Jetson Orin Nano Super Dev Kit (8GB) | $249 | Capable of 40 TOPS. |
| **The Eyes** | Intel RealSense D435i | $349 | Includes IMU (essential for SLAM). |
| **The Ears** | ReSpeaker USB Mic Array v2.0 | $69 | Far-field microphone for voice commands. |
| **Power/Misc** | SD Card (128GB) + Jumper Wires | $30 | High-endurance microSD card required for the OS. |
| **TOTAL** | | **~$700 per kit** | |