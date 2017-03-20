#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import roslib
import rospy
from std_msgs.msg import String
from nav_msgs import Odometry
from math import sin,pi
import tf

class my_odom:
    #---------------------------------------------------------------------#
    # initialized
    #---------------------------------------------------------------------#	
    def __init__(self):
		rospy.init_node('my_odom', anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.rate  = rospy.Rate(1) #10Hz
		self.pub = rospy.Publisher('/odom',LaserScan,queue_size=10)
		rospy.sleep(2)

    #---------------------------------------------------------------------#
    # publish odommetry data
    #---------------------------------------------------------------------#		 
    def pub_data(self):
        odom = Odometry()

	#---------------------------------------------------------------------#
    # exception shutdown
    #---------------------------------------------------------------------#	
    def shutdown(self):
        rospy.loginfo("tf exti")
        rospy.sleep(1)  

        
if __name__ == '__main__':
    ins_odom = my_odom()
    ins_odom.pub_data()