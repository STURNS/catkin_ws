#!/usr/bin/env python  

import roslib
import rospy
import tf


class TF_trans:
    def __init__(self):
        rospy.init_node('tf_node')
        self.br = tf.TransformBroadcaster()
        rospy.on_shutdown(self.shutdown)
        self.r = rospy.Rate(2)

    def pub_tranforms(self):
        while not rospy.is_shutdown():
            self.br.sendTransform((0.1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'map','odom')
            self.br.sendTransform((0.1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'base_link','odom')
            self.r.sleep()
    def shutdown(self):
        rospy.loginfo("tf exti")
        rospy.sleep(1)    
        
if __name__ == '__main__':
    mtf = TF_trans()
    mtf.pub_tranforms()
