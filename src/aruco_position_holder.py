#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import geometry_msgs.msg
from sensor_msgs.msg import sensor_msgs, Image
import math
from cv_bridge import CvBridge
import cv2
from PID import pid


bridge = CvBridge()

center = [0,0]
position = [0,0,0]

def get_center(data):
    
    h = data.height/2
    w = data.width/2
    global center
    center = [h,w]


def read_position(data):
    
    x_pos = data.pose.position.x * 100 # millimeter
    y_pos = data.pose.position.y * 100 # millimeter
    z_pos = data.pose.position.z * 100 # millimeter
    global position
    position = [x_pos, y_pos, z_pos]

def gui(data):
    cv2_img = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.line(cv2_img, (center[1], 0), (center[1], 2*center[0]), (0, 20, 200), 1)
    cv2.line(cv2_img, (0, center[0]), (2*center[1], center[0]), (0, 20, 200), 1)
    cv2.circle(cv2_img, (center[1], center[0]), 5, (0, 20, 200), 1)
    cv2.imshow('raw_image', cv2_img)
    cv2.waitKey(1)

def main():

    rospy.init_node('position_holder', anonymous=False)
    rospy.Subscriber("/aruco_single/pose", geometry_msgs.msg.PoseStamped, read_position)
    rospy.Subscriber("/tello_node/image_raw", sensor_msgs.msg.Image, get_center)
    rospy.Subscriber("/aruco_single/result", sensor_msgs.msg.Image, gui)
    # pose_publisher = rospy.Publisher('position', String, queue_size=10)
    # pose_publisher.publish(position)
    rospy.spin()

if __name__ == '__main__':
    main()