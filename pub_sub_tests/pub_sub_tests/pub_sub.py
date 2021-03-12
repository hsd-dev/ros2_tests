import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.executors import SingleThreadedExecutor

class MinimalPublisher(Node):

    def __init__(self, topic='topic', msg_type=String):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(msg_type, topic, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


class MinimalSubscriber(Node):

    def __init__(self, topic='topic', msg_type=String):
        super().__init__('minimal_subscriber')
        self.subscription_ = self.create_subscription(
            msg_type,
            topic,
            self.listener_callback,
            10)
        self.subscription_  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: [%s]' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    minimal_subscriber = MinimalSubscriber()

    executor = SingleThreadedExecutor()
    executor.add_node(minimal_publisher)
    executor.add_node(minimal_subscriber)

    executor.spin()
    #try:
    #    executor.spin()
    #except KeyboardInterrupt:
    #    # Destroy the node explicitly
    #    # (optional - otherwise it will be done automatically
    #    # when the garbage collector destroys the node object)
    #    minimal_publisher.destroy_node()
    #    minimal_subscriber.destroy_node()
    #    rclpy.shutdown()


if __name__ == '__main__':
    main()
