#!/usr/bin/env python  

import roslib
import rospy
import tf
from math import pi,pow

class TF_trans:
    def __init__(self):
        rospy.init_node('tf_node')
        self.br = tf.TransformBroadcaster()
        rospy.on_shutdown(self.shutdown)
        self.r = rospy.Rate(1)

    def pub_tranforms(self):
        rospy.loginfo('in vm')
        start_time = rospy.Time.from_sec(rospy.get_time()).to_sec()
        while not rospy.is_shutdown():
            self.br.sendTransform((2, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'base_link','odom')
            self.br.sendTransform((1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, pi/2),
                rospy.Time.now(),'odom','world')
            #self.br.sendTransform((0, 0, 0),
            #    tf.transformations.quaternion_from_euler(0, 0, 0),
            #    rospy.Time.now(),'map','odom')
                #rospy.Time.from_sec(rospy.get_rostime().secs).to_sec()
                #rospy.Time.from_sec(rospy.get_time()).to_sec()
                #rospy.Duration.from_sec(rospy.get_time()).to_sec()
            self.r.sleep()
    def shutdown(self):
        rospy.loginfo("tf exti")
        rospy.sleep(1)    
        
if __name__ == '__main__':
    mtf = TF_trans()
    mtf.pub_tranforms()
