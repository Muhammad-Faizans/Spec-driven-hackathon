---
sidebar_position: 1
---

# Module 1: The Robotic Nervous System (ROS 2)

**Focus**: Middleware for robot control.

The Robot Operating System (ROS 2) acts as the nervous system for our physical AI, providing the foundational middleware necessary for real-time robotic control and communication.

## Core Concepts

### ROS 2 Nodes, Topics, and Services

ROS 2 uses a distributed architecture where different components communicate through a publish-subscribe messaging system. **Nodes** are individual processes that perform specific tasks (e.g., sensor data processing, motor control, path planning). **Topics** enable asynchronous communication between nodes using a publish-subscribe pattern—nodes can publish messages to topics or subscribe to receive messages from topics. This allows for decoupled, flexible system design. **Services** provide synchronous request-response communication for operations that require immediate feedback, such as querying sensor status or triggering specific actions.

Understanding this communication model is fundamental to building robotic systems, as it enables modular design where different components can be developed, tested, and replaced independently.

### Bridging Python Agents to ROS controllers using rclpy

The `rclpy` (ROS Client Library for Python) provides the Python API for ROS 2, allowing developers to create ROS nodes in Python. This is crucial for integrating AI/ML agents written in Python with the underlying robotic hardware controllers. Python agents can subscribe to sensor topics, process data using machine learning models, and publish control commands to actuator topics.

The bridge between high-level AI logic (written in Python) and low-level hardware controllers (often in C++) is essential for creating intelligent robotic systems. Students will learn to create custom ROS 2 nodes that interface between their AI models and the robot's physical components.

### Understanding URDF (Unified Robot Description Format) for humanoids

URDF is an XML format used to describe the physical properties of a robot, including its links (rigid bodies), joints (connections between links), visual and collision geometries, inertial properties, and joint limits. For humanoid robots, this includes modeling the kinematic chain from the base (pelvis) through the legs, torso, arms, and head.

A proper URDF model is essential for:
- **Simulation**: Accurate physics simulation in Gazebo and other simulators
- **Kinematics**: Computing forward and inverse kinematics for motion planning
- **Visualization**: Rendering the robot in RViz and other visualization tools
- **Control**: Understanding joint relationships for coordinated movement

Students will learn to read, modify, and create URDF files for humanoid robots, understanding how joint hierarchies and coordinate frames define the robot's structure.