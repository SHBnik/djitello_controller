#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import geometry_msgs.msg
# import sensor_msgs/Image
import math


# def get_center():
#     pass


def read_position(data):
    
    robot_x_pos = data.pose.position.x / 10 # centimeter
    robot_y_pos = data.pose.position.y / 10 # centimeter
    robot_z_pos = data.pose.position.z / 10 # centimeter
    position = [robot_x_pos, robot_y_pos, robot_z_pos]
    print(data)

def main():

    rospy.init_node('position_holder', anonymous=False)
    rospy.Subscriber("/aruco_single/pose", geometry_msgs.msg.PoseStamped, read_position)
    # rospy.Subscriber("/tello_node/image_raw", sensor_msgs/Image, read_position)
    rospy.spin()

if __name__ == '__main__':
    main()