#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import roslib
import rospy
from geometry_msgs.msg import Quaternion,Pose,Vector3,Point,Twist
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
        #start_t=rospy.Time.Now()
        x = 0.0
        y = 0.0
        th = 0.0
        vx = 0.1
        vy = -0.1
        vth = 0.1
        rospy.loginfo('in pub_data')
        while not rospy.is_shutdown():
            #dt = (rospy.Time.now()-start_t).to_sec()
            dt = rospy.Time.from_sec((rospy.get_time() - star_t)).to_sec()
            star_t = rospy.get_time()
            # @@ generate the odommetry data 
            odom_quat = tf.transformations.quaternion_from_euler(0,0,0)
            odom.child_frame_id = 'base_link'
            odom.pose.pose.orientation = odom_quat
            odom.pose.pose = Pose(Point(0,0,0),Quaternion(*odom_quat))
            #odom.pose.covariance = 
            odom.twist.twist = Twist(Vector3(0,0,0),Vector3(0,0,0))
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
    #print(Vector3(0,11,1))