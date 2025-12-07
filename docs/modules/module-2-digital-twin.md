---
sidebar_position: 2
---

# Module 2: The Digital Twin (Gazebo & Unity)

**Focus**: Physics simulation and environment building.

To safely test and train our Physical AI systems, we utilize high-fidelity digital twins—simulations that accurately reflect real-world physics and environments.

## Simulation Environments

### Simulating physics, gravity, and collisions in Gazebo

Gazebo is a powerful physics-based simulator that accurately models real-world physics including gravity, friction, collisions, and rigid body dynamics. For humanoid robots, this is critical because bipedal locomotion requires precise balance, weight distribution, and ground contact forces. Gazebo uses physics engines (like ODE, Bullet, or DART) to simulate how the robot's joints move, how forces propagate through the kinematic chain, and how the robot interacts with its environment.

Students will configure Gazebo worlds, spawn robot models, and observe how physics parameters affect robot behavior. This enables safe testing of control algorithms without risking damage to expensive hardware.

### High-fidelity rendering and human-robot interaction in Unity

Unity provides photorealistic rendering capabilities that go beyond physics simulation, creating visually rich environments for testing human-robot interaction scenarios. Unity's advanced graphics engine allows for realistic lighting, shadows, textures, and animations, making it ideal for:
- **Visual perception testing**: Training and validating computer vision algorithms
- **Human-robot interaction studies**: Creating realistic scenarios where humans and robots interact
- **Presentation and demos**: Showcasing robot capabilities in visually appealing environments

Unity can interface with ROS 2 through plugins, allowing the same control code to work in both Gazebo (for physics) and Unity (for visualization and HRI scenarios).

### Simulating sensors: LiDAR, Depth Cameras, and IMUs

Virtual sensors in simulation generate synthetic data streams that mirror real-world sensor outputs. **LiDAR** (Light Detection and Ranging) sensors produce point clouds representing the 3D structure of the environment, essential for mapping and obstacle avoidance. **Depth cameras** (like RGB-D sensors) provide both color images and per-pixel depth information, enabling object recognition and manipulation. **IMUs** (Inertial Measurement Units) measure acceleration and angular velocity, critical for balance and orientation estimation in humanoid robots.

Simulated sensor data is crucial for:
- **Training perception models**: Generating large datasets without expensive data collection
- **Algorithm development**: Testing perception pipelines before hardware deployment
- **Sensor fusion**: Understanding how multiple sensors work together

Students will configure sensor plugins, calibrate sensor parameters, and process synthetic sensor data using the same algorithms that will run on real hardware.

:::note
The digital twin environment is vital for reducing costs and iteration time before deployment to real hardware.
:::