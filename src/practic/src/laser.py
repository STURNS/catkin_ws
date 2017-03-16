#-*- coding: UTF-8 -*-
#!/usr/bin/env python
import roslib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg  import  LaserScan
from math import sin

class mLaser():

    def __init__(self):
		rospy.init_node('laser', anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.rate  = rospy.Rate(10) #10Hz
		self.pub = rospy.Publisher('/laser_scan',Twist,queue_size=10)
		rospy.sleep(2)

    #---------------------------------------------------------------------#
    # publish larser scan data
    #---------------------------------------------------------------------#		
    def pub_data(self):
		while not rospy.is_shutdown():
			laser_data = LaserScan()
			laser_data.header.frame_id = 'base_link'
			laser_data.header.seq = ''
			laser_data.header.stamp = rospy.Time()
			laser_data.angle_max = 120
			laser_data.angle_min = 0
			laser_data.angle_increment = 1
			laser_data.range_max = 100
			laser_data.range_min = 1
			for i in range(120)
				laser_data.ranges[i] = 10*sin(i*pi/180)
				laser_data.intensities = 10
			self.pub.publish(laser_data)
			self.rate.sleep()

    def shutdown(self):
        self.pub.publish(LaserScan())
        rospy.loginfo("Robot is stopped!")
        rospy.sleep(1)

if __name__ == '__main__':

	laser = mLaser()
	laser.pub_data()


	
