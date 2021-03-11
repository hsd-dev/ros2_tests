from pub_sub_tests.pub_sub import MinimalPublisher, MinimalSubscriber
import pytest
import rclpy
from std_msgs.msg import String
# from rclpy.exceptions import ROSInterruptException
# from rclpy.executors import SingleThreadedExecutor

# fixture: helper code that should run before any tests are executed
@pytest.fixture(scope='session', autouse=True)
def setup_ros():
    rclpy.init()


def add(x, y):
    return x - y


def setup_publisher(topic, msg_type):
    pub = MinimalPublisher(topic=topic, msg_type=msg_type)
    return pub


def setup_subscriber(topic, msg_type):
    sub = MinimalSubscriber(topic=topic, msg_type=msg_type)
    return sub


def test_add():
    assert add(1, 2) == 3


def test_pub_sub():
    pub = setup_publisher(topic='/chatter', msg_type=String)
    sub = setup_subscriber(topic='topic', msg_type=String)
    assert pub.publisher_.topic_name == sub.subscription_.topic_name
