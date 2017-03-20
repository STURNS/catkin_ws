#!/usr/bin/env python  

import roslib
import rospy
import tf
from math import pi,pow,sin,cos

class TF_trans:
    #---------------------------------------------------------------------#
    # initialized
    #---------------------------------------------------------------------#	
    def __init__(self):
        rospy.init_node('tf_node')
        self.br = tf.TransformBroadcaster()
        rospy.on_shutdown(self.shutdown)
        self.r = rospy.Rate(2)
    #---------------------------------------------------------------------#
    # publish tf data
    #---------------------------------------------------------------------#	
    def pub_tranforms(self):
        start_time = rospy.Time.from_sec(rospy.get_time()).to_sec()
        while not rospy.is_shutdown():
            dt = rospy.Time.from_sec(rospy.get_time() - start_time).to_sec()
            self.br.sendTransform((1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'odom','world')

            self.br.sendTransform((0.1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'map','odom')

            self.br.sendTransform((0.5*cos(dt*0.1), 0.5*sin(dt*0.1), 0),
                tf.transformations.quaternion_from_euler(0, 0, dt*0.1),
                rospy.Time.now(),'base_link','odom')

            #self.br.sendTransform((0, 0, 0),
            #    tf.transformations.quaternion_from_euler(0, 0, 0),
            #    rospy.Time.now(),'map','odom')
                #rospy.Time.from_sec(rospy.get_rostime().secs).to_sec()
                #rospy.Time.from_sec(rospy.get_time()).to_sec()
                #rospy.Duration.from_sec(rospy.get_time()).to_sec()
            self.r.sleep()
    #---------------------------------------------------------------------#
    # shutdown
    #---------------------------------------------------------------------#	
    def shutdown(self):
        rospy.loginfo("tf exti")
        rospy.sleep(1)  

#---------------------------------------------------------------------#
# tf thread
#---------------------------------------------------------------------#	       
if __name__ == '__main__':
    mtf = TF_trans()
    mtf.pub_tranforms()
