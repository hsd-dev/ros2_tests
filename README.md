## Testing in ROS2

This repo demonstrates some testing capabilities in ROS2

### Usage

```
$ mkdir -p ~/test_ws/src && cd ~/test_ws/src
$ git clone https://github.com/ipa-hsd/ros2_tests
$ cd ~/test_ws
$ . /opt/ros/foxy/setup.bash
$ colcon build --symlink-install
$ colcon test
$ colcon test-result --verbose
```

Analyse the results and fix the bugs accordingly