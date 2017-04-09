#!/usr/bin/env python
#coding:utf-8


import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class toRobot():
    #---------------------------------------------------------------------#
    #init
    #---------------------------------------------------------------------#
    def __init__(self):
        rospy.init_node('toRobot', anonymous=False)
        rospy.on_shutdown(self.shutdown)
    #---------------------------------------------------------------------#
    #forward
    #line_speed : linear speed m/s 
    #---------------------------------------------------------------------#
    def moveforward(self,line_speed):
        r = rospy.Rate(10)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        mycmd = Twist()
        mycmd.linear.x = line_speed
        while not rospy.is_shutdown():
            self.pub.publish(mycmd)
            r.sleep()
    #---------------------------------------------------------------------#
    #shutdown
    #---------------------------------------------------------------------#
    def shutdown(self):
        self.pub.publish(Twist())
        rospy.loginfo("Stopping the robot...")
        rospy.sleep(1)

if __name__ == '__main__':
    n = toRobot()
    n.moveforward(0.2)
        
        
