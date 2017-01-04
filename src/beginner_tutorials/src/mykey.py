#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def circle():
	rospy.init_node('mykey', anonymous=False)
	cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	CMD = Twist()
	r = rospy.Rate(1)
	#CMD.linear.x = 1 
	#CMD.linear.y = 2
	'''
	#(A)
	CMD.linear.x = 200
	CMD.linear.y = 0
	CMD.linear.z= 0
	CMD.angular.x = 0
	CMD.angular.y = 0
	CMD.angular.z = 1.8
'''
	for i in range(2):
		cmd_vel.publish(Twist(Vector3(4,0,0),Vector3(0,0,1.00)))
		r.sleep()
    #for i in range(250):
    #    cmd_vel.publish(CMD)
    #    r.sleep()
	rospy.sleep(1);
	
if __name__ == '__main__':
	circle();
