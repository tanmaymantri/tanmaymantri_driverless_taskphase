import rclpy
from rclpy.node import Node
from rt2_interfaces.msg import RT2String

class Node2(Node):
    def __init__(self):
        super().__init__('node2')
        self.create_subscription(RT2String, 'string_topic', self.sub_cb, 10)
        self.pub = self.create_publisher(RT2String, 'result_topic', 10)

    def sub_cb(self, msg):
        txt = msg.data.replace(" ", "").lower()
        val = "1" if txt == txt[::-1] else "0"
        print(f"Received: '{msg.data}' | Sent: {val}")
        out_msg = RT2String()
        out_msg.data = val
        self.pub.publish(out_msg)

def main():
    rclpy.init()
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()