#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_turtle')

    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=10)
    rate = rospy.Rate(10.0)
    listener.waitForTransform('/turtle2','/carrot1',rospy.Time(0), rospy.Duration(4.0))
    while not rospy.is_shutdown():
        try:
            now=rospy.Time.now()
            past = now - rospy.Duration(4.0)
            listener.waitForTransformFull('/turtle2',now,'/carrot1',past,'/world',rospy.Duration(1.0))
            (trans,rot) = listener.lookupTransformFull('/turtle2', now,'/carrot1', past,'/world') #'/turtle1'
        #except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        except (tf.Exception,tf.LookupException,tf.ConnectivityException):
            continue

        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()

''' 
#difference between rospy.Time(0) and now()
now = rospy.Time.now()
listener.waitForTransform('/turtle2','/carrot1',rospy.Time(0),rospy.Duration(4.0))	
(trans,rot) = listener.lookupTransform('/turtle2', '/carrot1', now) #'/turtle1'		
'''