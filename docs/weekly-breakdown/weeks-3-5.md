---
sidebar_position: 2
---

# Weeks 3-5: ROS 2 Fundamentals

This three-week segment is dedicated to mastering the **Robot Operating System 2 (ROS 2)**, the communication framework that powers the robot's nervous system.

## Topics Covered

### ROS 2 Architecture and Core Concepts

ROS 2 (Robot Operating System 2) is the industry-standard middleware framework for building robotic systems. Unlike a traditional operating system, ROS 2 provides a communication layer that allows different software components to work together seamlessly, even when running on different machines. Key architectural concepts include:

- **Distributed System**: ROS 2 nodes can run on the same machine or across a network, enabling distributed computing for complex robots with multiple processors.
- **Middleware Abstraction**: ROS 2 abstracts away low-level communication details, allowing developers to focus on robot logic rather than networking.
- **Language Agnostic**: Components can be written in Python, C++, or other languages and still communicate seamlessly.
- **Real-time Capabilities**: ROS 2 supports real-time execution, critical for safety-critical applications like humanoid balance control.
- **Quality of Service (QoS)**: Configurable communication policies that determine reliability, durability, and delivery guarantees for different types of data.

Understanding ROS 2 architecture is fundamental—it's the foundation upon which all robotic software is built, enabling modular, reusable, and maintainable code.

### Nodes, Topics, Services, and Actions

ROS 2 provides four primary communication mechanisms, each suited for different types of interactions:

#### Nodes: The Process Unit of ROS 2

A **node** is an executable process that performs a specific function (e.g., sensor data processing, motor control, path planning). Nodes are the building blocks of ROS 2 systems:
- **Modularity**: Each node has a single responsibility, making systems easier to develop, test, and debug
- **Independence**: Nodes can be started, stopped, or restarted independently without affecting others
- **Scalability**: New functionality can be added by creating new nodes without modifying existing ones

#### Topics: Asynchronous, One-way Message Passing

**Topics** enable publish-subscribe communication, ideal for continuous data streams:
- **Publisher**: A node that sends messages to a topic (e.g., camera node publishing images)
- **Subscriber**: A node that receives messages from a topic (e.g., object detection node subscribing to images)
- **Asynchronous**: Publishers and subscribers operate independently—if a subscriber is slow, it doesn't block the publisher
- **One-to-many**: Multiple subscribers can receive the same message, enabling data distribution
- **Use cases**: Sensor data (camera feeds, LiDAR scans), status updates, continuous control commands

#### Services: Synchronous, Request-Response Communication

**Services** provide synchronous communication for operations that need immediate responses:
- **Client**: Sends a request and waits for a response
- **Server**: Receives requests, processes them, and sends responses
- **Synchronous**: The client blocks until the server responds
- **Use cases**: Querying sensor status, triggering one-time actions, configuration changes

#### Actions: Long-running, Goal-oriented Tasks

**Actions** combine the benefits of topics and services for tasks that take time to complete:
- **Goal**: Client sends a goal (e.g., "navigate to position X, Y")
- **Feedback**: Server sends periodic updates on progress (e.g., "50% complete, currently at position A, B")
- **Result**: Server sends final result when complete (e.g., "Successfully reached destination")
- **Cancelable**: Goals can be canceled mid-execution
- **Use cases**: Navigation, manipulation sequences, long-duration tasks

Students will implement practical examples of each communication type, understanding when to use each pattern and how they work together in complex systems.

### Building ROS 2 Packages with Python

Python is the preferred language for AI/ML integration in robotics due to its rich ecosystem of machine learning libraries. Using `rclpy` (ROS Client Library for Python), students will:

- **Create custom ROS 2 packages**: Organizing code into reusable, distributable packages
- **Implement nodes**: Writing Python classes that inherit from `rclpy.Node` to create functional nodes
- **Handle messages**: Working with ROS 2 message types (standard and custom) for data exchange
- **Integrate AI models**: Connecting machine learning models (PyTorch, TensorFlow) to ROS 2 topics and services
- **Error handling**: Implementing robust error handling and logging for production systems
- **Testing**: Writing unit tests for ROS 2 nodes to ensure reliability

Hands-on projects will include creating nodes for sensor processing, AI inference, and control logic, building the foundation for more complex systems later in the course.

### Launch Files and Parameter Management

Real robotic systems consist of dozens or hundreds of nodes that must be started in the correct order with proper configuration. **Launch files** automate this process:

- **Multi-node orchestration**: Starting multiple nodes with a single command
- **Dependency management**: Ensuring nodes start in the correct order
- **Parameter configuration**: Setting node parameters (e.g., sensor calibration values, control gains)
- **Conditional execution**: Starting different node sets based on conditions (simulation vs. real hardware)
- **Namespace management**: Organizing nodes into logical groups to avoid naming conflicts

**Parameter management** is crucial for:
- **Configuration**: Storing robot-specific settings (dimensions, sensor positions, control parameters)
- **Tuning**: Adjusting system behavior without recompiling code
- **Deployment**: Using different parameter sets for different robots or environments
- **Version control**: Tracking configuration changes over time

Students will create launch files for complex systems, learning best practices for organizing and managing large-scale robotic software deployments.