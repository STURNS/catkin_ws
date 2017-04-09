#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Twist,Pose,Vector3


class TEST:
    def __init__(self):
        rospy.init_node('test_node')
        rate = rospy.Rate(1)

    def te(self):
        return '123456'

def pass_prara(pa):
    pa = TEST()
    print(pa.te())

if __name__ == '__main__':
    rospy.init_node('test', log_level=rospy.INFO)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        print(rospy.get_param('~TrajectoryPlannerROS')['escape_vel'])
        r.sleep()

#test