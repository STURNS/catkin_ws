#-*- coding: UTF-8 -*-
#!/usr/bin/env python
import roslib
import rospy
import tf
if __name__ == '__main__':
    rospy.init_node('tf_node')
    br = tf.TransformBroadcaster()
    r = rospy.Rate(10)
    while not ropy.is_shutdown():
        br.sendTransform((msg.x, msg.y, 0),tf.transformations.quaternion_from_euler(0, 0, msg.theta),rospy.Time.now(),'base_link,"world")
        r.sleep()
#test