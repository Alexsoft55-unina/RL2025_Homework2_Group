from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
FindPackageShare("package_a")
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    

    ros2_kdl_package_path = os.path.join(
        get_package_share_directory("ros2_kdl_package"),)
    yaml_parameter = os.path.join(ros2_kdl_package_path, "config", "parameter.yaml")

    nodes_to_start = []

    ros2_kdl_package_node = Node(
        package='ros2_kdl_package',
        executable='ros2_kdl_node',
        name='ros2_kdl_node',
        parameters=[yaml_parameter]
    )
    nodes_to_start += [ros2_kdl_package_node]
    return LaunchDescription(nodes_to_start) 