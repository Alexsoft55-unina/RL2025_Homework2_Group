from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, ExecuteProcess
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
import xacro
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    

   	
   
    
    nodes_to_start = []
    
    ros2_kdl_node = Node(
        package='ros2_kdl_package',
        executable='ros2_kdl_node',
        name='ros2_kdl_node',
        parameters=[PathJoinSubstitution([FindPackageShare('ros2_kdl_package'),'config','kdl_params.yaml'])]
    )
    
    
  

 
    nodes_to_start = [
    	ros2_kdl_node
    ]
        
    return LaunchDescription(nodes_to_start) 
