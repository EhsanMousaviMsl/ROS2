#!/usr/bin/python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('vision_subscriber')
        self.br = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/camera',
            self.getImage,
            10)
        self.subscription  # prevent unused variable warning

    def getImage(self, msg):
        self.get_logger().info('Receiving Frame')
        current_frame = self.br.imgmsg_to_cv2(msg)

        cv2.imshow("camera", current_frame)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()