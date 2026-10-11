import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne

class WheelSubscriber(Node):
    def __init__(self):
        super().__init__('wheel_subscriber')
        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.listener_callback,
            10)
        self.get_logger().info('Wheel Subscriber Node has started, waiting for data...')

    def listener_callback(self, msg):
        # Calculate longitudinal speed: v = ang_vel * radius
        longitudinal_speed = msg.ang_vel * msg.radius
        self.get_logger().info(
            f'Received -> angVel: {msg.ang_vel}, radius: {msg.radius} | '
            f'Calculated Longitudinal Speed = {longitudinal_speed:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = WheelSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()