import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne

class WheelPublisher(Node):
    def __init__(self):
        super().__init__('wheel_publisher')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)
        self.get_logger().info('Wheel Publisher Node has started.')
        self.publish_data()

    def publish_data(self):
        try:
            while rclpy.ok():
                print("\n--- Enter Wheel Parameters ---")
                ang_vel = float(input("Enter angular velocity (angVel): "))
                radius = float(input("Enter wheel radius (radius): "))

                msg = TaskOne()
                msg.ang_vel = ang_vel
                msg.radius = radius

                self.publisher_.publish(msg)
                self.get_logger().info(f'Published -> Angular Velocity: {ang_vel}, Radius: {radius}')
        except KeyboardInterrupt:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()
    rclpy.shutdown()

if __name__ == '__main__':
    main()