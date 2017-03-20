#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import roslib
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

from math import sin,pi,cos
import tf

class my_odom:
    #---------------------------------------------------------------------#
    # initialized
    #---------------------------------------------------------------------#	
    def __init__(self):
		rospy.init_node('my_odom', anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.rate  = rospy.Rate(1) #10Hz
		self.pub = rospy.Publisher('/odom',Odometry,queue_size=10)
		rospy.sleep(1)

    #---------------------------------------------------------------------#
    # publish odommetry data
    #---------------------------------------------------------------------#		 
    def pub_data(self):
        odom = Odometry()
        odom.header.stamp = rospy.Time.now() 
        odom.header.frame_id = 'odom'
        star_t = rospy.get_time()
        x = 0.0
        y = 0.0
        th = 0.0
        vx = 0.1
        vy = -0.1
        vth = 0.1
        rospy.loginfo('in pub_data')
        while not rospy.is_shutdown():
            dt = rospy.Time.from_sec((rospy.get_time() - star_t)).to_sec()
            star_t = rospy.get_time()
            delta_x = (vx * cos(th) - vy * sin(th)) * dt
            delta_y = (vx * sin(th) + vy * cos(th)) * dt
            delta_th = vth * dt
            x += delta_x
            y += delta_y
            th += delta_th

            odom_quat = tf.transformations.quaternion_from_euler(0,0,th)
            print(odom_quat)
            print(dt)
            odom.child_frame_id = 'base_link'
            odom.pose.pose.orientation = odom_quat
            odom.pose.pose.position.x = x
            odom.pose.pose.position.y = y
            odom.pose.pose.position.z = 0

            #odom.pose.covariance = 
            odom.twist.twist.angular.z = th
            odom.twist.twist.linear.x = vx
            odom.twist.twist.linear.y = vy
            #odom.twist.covariance
            self.pub.publish(odom)
            self.rate.sleep()
	#---------------------------------------------------------------------#
    # exception shutdown
    #---------------------------------------------------------------------#	
    def shutdown(self):
        #something else to do here 
        rospy.loginfo("odom_node exit")
        rospy.sleep(1)  


if __name__ == '__main__':
    ins_odom = my_odom()
    ins_odom.pub_data()