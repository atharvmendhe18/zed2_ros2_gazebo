import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    pkg_name = 'zed2_ros2_gazebo'
    file_subpath = 'urdf/zed2_ros2.xacro'

    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)
    robot_description = xacro.process_file(xacro_file).toxml().replace('<?xml version="1.0" encoding="utf-8"?>', '')

    # Start Robot State Publisher for Zed2
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description,
                     'use_sim_time': True}],
    )

    # Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
        launch_arguments={
            'pause': 'false',
            'physics': 'ode',
            'max_step_size': '0.001',
            'real_time_update_rate': '1000',
            'use_sim_time': 'true',
            'verbose': 'true',
            #'world': "path to your world file"
        }.items()
    )

    spawn_camera = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', '/robot_description',
                   '-entity', 'zed2_camera',
                   '-x', '0', '-y', '0', '-z', '2', '-Y', '3.14'], # Coordinates to spawn the camera
        output='screen'
    )

    
    return LaunchDescription([
        gazebo,
        node_robot_state_publisher,
        spawn_camera,
    ])
