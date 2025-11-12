# RL2025_Homework2

```
ros2 launch iiwa_bringup iiwa.launch.py use_sim:="true" command_interface:="velocity" robot_controller:="velocity_controller"
```

```
ros2 launch ros2_kdl_package launching.launch.py cmd_interface:=velocity ctrl:=velocity_ctrl
```
```
ros2 launch ros2_kdl_package launching.launch.py cmd_interface:=velocity ctrl:=velocity_ctrl_null
```
Then to start the action client that will activate the server and show the error position as feedback:

```
ros2 run ros2_kdl_package ros2_kdl_node_client

```

```
sudo apt update -y
sudo apt-get install ros-humble-ros-gazebo-bridge -y
sudo apt-get install ros-humble-ros-ign-gazebo -y
sudo apt-get install ros-humble-joint-state-publisher ros-humble-joint-state-publisher-gui -y
sudo apt-get install locate nano gedit gh -y
sudo apt-get install ros-humble-aruco-ros -y
```
```
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:$HOME/ros2_ws/src/iiwa_description/gazebo/models
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:$HOME/ros2_ws/install/iiwa_description/share/iiwa_description/gazebo/models
```

```
ros2 service call /set_aruco_pose ros_gz_interfaces/srv/SetEntityPose '{"entity": {"name": "aruco_tag", "type": 2}, "pose": {"position": {"x": 1.0, "y": 0.0, "z": 0.5}, "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}}}'
```