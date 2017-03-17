#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import roslib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg  import  LaserScan
from math import sin,pi
import tf

class mLaser():
	#---------------------------------------------------------------------#
    # initialized
    #---------------------------------------------------------------------#	
    def __init__(self):
		rospy.init_node('laser_scan', anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.rate  = rospy.Rate(1) #10Hz
		self.pub = rospy.Publisher('/laser_scan',LaserScan,queue_size=10)
		rospy.sleep(2)
    #---------------------------------------------------------------------#
    # publish larser scan data
    #---------------------------------------------------------------------#		
    def pub_data(self):

		n = 1000
		lrange = pi
		laser_data = LaserScan()
		laser_data.range_max = 10
		laser_data.range_min = 0.1
		laser_data.angle_max = lrange
		laser_data.angle_min = 0
		laser_data.angle_increment = lrange/(n-1)
		for i in range(n):
			laser_data.ranges.append(0)
			laser_data.intensities.append(0)
		laser_data.header.frame_id = 'odom'
		while not rospy.is_shutdown():
			laser_data.header.stamp = rospy.Time()
			for i in range(n):
				laser_data.ranges[i] = 6*sin(i*laser_data.angle_increment)
				laser_data.intensities[i] = 5
			print(laser_data.header.seq)
			self.pub.publish(laser_data)
			self.rate.sleep()
	#---------------------------------------------------------------------#
    # shutdown
    #---------------------------------------------------------------------#	
    def shutdown(self):
        rospy.loginfo("Robot is stopped!")
        rospy.sleep(1)

if __name__ == '__main__':

	laser = mLaser()
	laser.pub_data()


	
