#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images


class ImagePublisher(Node):

    def __init__(self):
        super().__init__('vision_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera', 10)
        timer_period = 0.033  # seconds
        self.timer = self.create_timer(timer_period, self.sendImage)
        self.i = 0
        self.cam = cv2.VideoCapture(0)
        self.br = CvBridge()

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def sendImage(self):
        ret, frame = self.cam.read()
        if ret:
            cv2.putText(frame,'Hello World!', 
                    (50,50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1,
                    (0, 0, 255),
                    4,
                    cv2.LINE_AA)
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame, 'bgr8'))

        # Display the message on the console
        self.get_logger().info('Publishing frame')

def main(args=None):
    rclpy.init(args=args)

    image_publisher = ImagePublisher()

    rclpy.spin(image_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()