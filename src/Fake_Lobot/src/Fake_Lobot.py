#!/usr/bin/env python
#coding:utf-8


import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3,Pose,Quaternion,Point
from nav_msgs.msg import Odometry
import tf
from math import pi,sin,cos

class Lobot():
    #---------------------------------------------------------------------#
    #init
    #---------------------------------------------------------------------#
    def __init__(self):
        rospy.init_node('Lobot', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.__rate = rospy.Rate(1)
        rospy.Subscriber("cmd_vel", Twist, self.vel_update)
        self.pub_odom = rospy.Publisher("odom", Odometry, queue_size=50)
        self.tf_broadcaster = tf.TransformBroadcaster()
        self.__vel = Twist()
        self.__odom = Odometry()
        self.__sum_x = 0
        self.__sun_y = 0
        self.__sum_th = 0

    #---------------------------------------------------------------------#
    #vel_update
    #callback
    #---------------------------------------------------------------------#
    def vel_update(self,req):
        self.__vel = req

    #---------------------------------------------------------------------#
    #forward
    #line_speed : linear speed m/s 
    #---------------------------------------------------------------------#
    def poll(self):
        last = rospy.get_time()
        while not rospy.is_shutdown():
            t = rospy.get_time() - last
            self.__sum_th += self.__vel.angular.z*t
            self.__sum_x += self.__vel .linear.x*t*cos(self.__sum_th)
            self.__sun_y += self.__vel .linear.x*t*sin(self.__sum_th)
            
            quat = tf.transformations.quaternion_from_euler(0,0,self.__sum_th)
            self.tf_broadcaster.sendTransform(
                        (self.__sum_x, self.__sun_y, 0.),
                        quat,
                         rospy.Time.now() ,
                        "base_link",
                        "odom"
                        )  
            self.tf_broadcaster.sendTransform(
                        (0, 0, 0.),
                        tf.transformations.quaternion_from_euler(0,0,0),
                         rospy.Time.now() ,
                        "odom",
                        "map"
                        ) 
            self.tf_broadcaster.sendTransform(
                        (0, 0, 0.1),
                        tf.transformations.quaternion_from_euler(0,0,0),
                         rospy.Time.now() ,
                        "base_footprint",
                        "base_link"
                        ) 
            self.__odom.header.frame_id = 'odom'
            self.__odom.child_frame_id = 'base_link'
            self.__odom.header.stamp = rospy.Time.now()

            self.__odom.pose.pose = Pose(Point(self.__sum_x,
                                        self.__sun_y,
                                        0),Quaternion(*quat))
            self.__odom.twist.twist = Twist(Vector3(self.__vel .linear.x, self.__vel .linear.y, 0), 
                                            Vector3(0, 0, self.__vel.angular.z))
            self.pub_odom.publish(self.__odom)

            last = rospy.get_time()
            self.__rate.sleep()
    #---------------------------------------------------------------------#
    #shutdown
    #---------------------------------------------------------------------#
    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        rospy.sleep(1)

if __name__ == '__main__':
    lobot = Lobot()
    lobot.poll()
        
        
