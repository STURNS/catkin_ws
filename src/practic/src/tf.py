#!/usr/bin/env python
'''
test
'''
import roslib
gi
import rospy
roslib.load_manifest('learning_tf')

import tf


if __name__ == '__main__':
    rospy.init_node('tf_node')
    br = tf.TransformBroadcaster()
    t_m_w = tf.TransformBroadcaster()
    r = rospy.Rate(10)
    while not ropy.is_shutdown():
        br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")


        r.sleep()

#test