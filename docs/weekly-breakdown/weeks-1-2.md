---
sidebar_position: 1
---

# Weeks 1-2: Introduction to Physical AI

This two-week block establishes the core conceptual foundation for the entire course, shifting the perspective from traditional digital AI to embodied intelligence.

## Topics Covered

### Foundations of Physical AI and Embodied Intelligence

Physical AI represents a paradigm shift from traditional digital AI systems that operate purely in virtual spaces. **Embodied Intelligence** refers to AI systems that must interact with the physical world through a physical body, requiring them to understand and respond to real-world constraints. Unlike digital AI that processes abstract data, physical AI must:

- **Perceive the environment** through sensors that provide noisy, incomplete, and time-varying data
- **Reason about spatial relationships** and physical constraints (gravity, friction, collisions)
- **Plan and execute actions** that have real-world consequences
- **Adapt to uncertainty** in both perception and actuation

This foundation establishes why humanoid robots are particularly well-suited for human environments—they share our physical form, allowing them to navigate spaces designed for humans and interact with tools and objects built for human use.

### From Digital AI to Physical Laws

Transitioning from digital AI to physical AI introduces fundamental challenges that don't exist in purely computational domains:

- **Gravity and Balance**: Humanoid robots must constantly maintain balance against gravity, requiring continuous control adjustments. Unlike wheeled robots that have stable bases, bipedal robots are inherently unstable.
- **Friction and Contact**: Understanding how forces propagate through contact points (feet on ground, hands on objects) is essential for stable locomotion and manipulation.
- **Spatial Constraints**: Robots must navigate 3D space, avoiding collisions while operating in cluttered, dynamic environments designed for human scale.
- **Real-time Requirements**: Physical systems operate in continuous time, requiring real-time responses. Delays in processing can lead to instability or failure.
- **Energy Efficiency**: Physical actions consume energy, requiring efficient motion planning and control strategies.

Students will learn to think about AI problems through the lens of physics, understanding how algorithms must account for these physical constraints to be effective in the real world.

### Overview of Humanoid Robotics Landscape

The humanoid robotics field has seen rapid advancement in recent years, with both commercial and research efforts pushing the boundaries of what's possible. This overview covers:

- **Commercial Platforms**: Examining current humanoid robots like Boston Dynamics' Atlas, Tesla's Optimus, Figure AI's Figure 01, and others, understanding their capabilities and limitations.
- **Research Initiatives**: Surveying academic and research lab efforts, including work from institutions like MIT, Stanford, and various robotics labs worldwide.
- **Key Technical Challenges**: Identifying common problems across platforms (balance, manipulation, perception) and how different teams approach solutions.
- **Market Applications**: Understanding where humanoid robots are being deployed (warehouses, manufacturing, healthcare, service industries) and what use cases drive development.

This context helps students understand where the field is today and where it's heading, providing motivation and direction for their learning journey.

### Sensor Systems

Sensors are the robot's eyes, ears, and sense of touch, providing the raw data that AI algorithms process to understand the world. Each sensor modality has unique characteristics:

- **LIDAR (Light Detection and Ranging)**: Emits laser pulses and measures their return time to create precise 3D point clouds of the environment. Essential for mapping, localization, and obstacle detection. Provides accurate distance measurements but can struggle with transparent or reflective surfaces.

- **Cameras (RGB and Depth)**: 
  - **RGB cameras** capture color images, enabling object recognition, scene understanding, and human detection.
  - **Depth cameras** (like Intel RealSense, Microsoft Kinect) provide per-pixel distance information, combining visual and spatial data for manipulation tasks.

- **IMUs (Inertial Measurement Units)**: Measure acceleration and angular velocity using accelerometers and gyroscopes. Critical for balance control in humanoid robots, providing orientation and motion data even when visual sensors fail (e.g., in darkness or when cameras are occluded).

- **Force/Torque Sensors**: Measure forces and torques applied at contact points (feet, hands). Essential for:
  - **Balance control**: Detecting ground contact forces to maintain stability
  - **Manipulation**: Sensing grip force to prevent dropping objects or applying excessive force
  - **Safety**: Detecting unexpected collisions or human contact

Students will learn how these sensors work, their strengths and limitations, and how to fuse data from multiple sensors to create robust perception systems.