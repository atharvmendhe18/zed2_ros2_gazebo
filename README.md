# ZED2 ROS2 Gazebo Package

This package allows you to load the ZED2 camera into Gazebo Classic in ROS2. You can attach the ZED2 to your robot or visualize it independently in Gazebo.

---

## Installation

Follow these steps to install the package:

```bash
cd path_to_your_ros2_ws/src
git clone git@github.com:atharvmendhe18/zed2_ros2_gazebo.git
cd ../
colcon build --packages-select zed2_ros2_gazebo
source install/setup.bash
```
---
## Steps to Attach ZED2 to Your Robot
1. Import the ZED2 xacro file into your robot's xacro file:

    Add the following line to your robot's xacro file:
    ```xml
    <xacro:include filename="$(find zed2_ros2_gazebo)/urdf/zed2_ros2.xacro" />
    ```
2. Attach the ZED2 to your robot:

    Replace the parent link in the ZED2 xacro file with your robot's desired parent link. For example:
    ```xml
    <joint name="zed2_tilt_head_joint" type="fixed">
    <origin xyz="0 0 -1.5" rpy="0 0.2 0"/>
    <parent link="world"/> <!-- Replace "world" with your robot's parent link -->
    <child link="zed2_tilt_head_link"/>
    </joint>
    ```
    You can adjust the origin parameters (xyz and rpy) to set the position and orientation of the ZED2 relative to your robot.
3.  Spawn your robot:

    When you spawn your robot in Gazebo, the ZED2 should also be spawned at your desired location.

---

## Visualizing Only the ZED2 in Gazebo

If you want to visualize only the ZED2 in Gazebo, follow these steps:

1. Source your workspace:
    ```bash
    source install/setup.bash
    ```

2. Launch the ZED2 in Gazebo:
    ```bash
    ros2 launch zed2_ros2_gazebo zed2_gazebo.launch.py
    ```
 
Notes
- Ensure that the parent link in the ZED2 xacro file matches the desired link in your robot's URDF/xacro file.

- Adjust the origin parameters to position the ZED2 correctly on your robot.
