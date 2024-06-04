import rclpy
from rclpy.node import Node
import cv2
import time, os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from ament_index_python.packages import get_package_share_directory

package_path = os.path.abspath(get_package_share_directory('adaface_ros')).split('install')[0]

class ImagePublisher(Node):
    def __init__(self):
        super().__init__("image_publisher")
        
        self.bridge = CvBridge()

        video_path = os.path.join(package_path, video_path)
        self.cap = cv2.VideoCapture(video_path)
        self.pub = self.create_publisher(Image, "video_topic", 10)

    def run(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read() 
            if ret:
                self.pub.publish(self.bridge.cv2_to_imgmsg(frame,"rgb8"))
            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            time.sleep(1/60) 

        self.cap.release()

def main(args=None):
    rclpy.init(args=None)
    image_pub = ImagePublisher()
    print("Publishing...")
    image_pub.run()

    image_pub.destroy_node()
    rclpy.shutdown()