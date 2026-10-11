import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String

class Node3(Node):
    def __init__(self):
        super().__init__('node3')
        self.create_subscription(RT2String, 'result_topic', self.sub_cb, 10)

    def sub_cb(self, msg):
        res = "Yes" if msg.data == "1" else "No"
        print(f"Input: {msg.data} -> Output: {res}")

def main():
    rclpy.init()
    node = Node3()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()