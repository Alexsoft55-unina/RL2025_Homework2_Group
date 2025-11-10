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
