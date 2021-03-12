import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'launch'))  # noqa

from launch import LaunchDescription  # noqa: E402
from launch import LaunchIntrospector  # noqa: E402
from launch import LaunchService  # noqa: E402

import launch_ros.actions  # noqa: E402


def generate_launch_description():
    """Run demo nodes via launch."""
    return LaunchDescription([
        launch_ros.actions.Node(
            package='pub_sub_tests',
            executable='talker',
            output='screen',
            remappings=[('chatter', 'my_chatter')]),
    ])
