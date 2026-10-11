import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.pub = self.create_publisher(RT2String, 'string_topic', 10)
        while rclpy.ok():
            val = input("Enter string: ")
            msg = RT2String()
            msg.data = val
            self.pub.publish(msg)

def main():
    rclpy.init()
    Node1()
    rclpy.shutdown()

if __name__ == '__main__':
    main()