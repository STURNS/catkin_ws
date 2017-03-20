#!/usr/bin/env python
# license removed fo brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3, Point, Quaternion
import tf
import math
#---------------------------------------------------------------------#
# class 
#---------------------------------------------------------------------#  
class toMyrobot():
    def __init__(self):  
        self.static_t = '/world'  
        self.test1 = '/turtle1'     #'/base_link'
        self.test2 = '/turtle2'     #'/base_footprint'

        rospy.init_node('talker',anonymous=True)
        rospy.on_shutdown(self.shutdown)
        self.rate  = rospy.Rate(10) #10Hz
        self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.tf_listener = tf.TransformListener()
        rospy.sleep(2)
        #deteced what's the name is used by base_frame
        try:
            self.tf_listener.waitForTransform(self.static_t,self.test1 ,
                                              rospy.Time(),rospy.Duration())
            self.base_frame = self.test1 
        except (tf.Exception,tf.ConnectivityException, tf.LookupException):
            try:
                self.tf_listener.waitForTransform(self.static_t,self.test2,
                                              rospy.Time(),rospy.Duration())
                self.base_frame = self.test2
            except (tf.Exception,tf.ConnectivityException, tf.LookupException):
                rospy.loginfo('cannot transforn ' + self.static_t + ' to ..')
                rospy.signal_shutdown('tf exception')     
    #---------------------------------------------------------------------#
    # moveForward
    #---------------------------------------------------------------------#
    def moveForward(self,distance):
        position = Point()      
        move_cmd = Twist()
        move_cmd.linear.x = distance
        rospy.loginfo('Move Forward')
        while not rospy.is_shutdown():
            #(position,rotation) = self.get_odom()
            move_cmd.linear.z = position.x
            self.pub.publish(move_cmd)
            self.rate.sleep()
    #---------------------------------------------------------------------#
    # get_odom
    #---------------------------------------------------------------------#        
    def get_odom(self):
        try:
            (trans, rot) = self.tf_listener.lookupTransform(self.static_t,self.base_frame,
                                                            rospy.Time(0))
        except(tf.Exception,tf.ConnectivityException, tf.LookupException):
            rospy.loginfo('tf exception')
            return

        return (Point(*trans),
            tf.transformations.euler_from_quaternion(rot))
    #---------------------------------------------------------------------#
    # shutdown
    #---------------------------------------------------------------------#
    def shutdown(self):
        self.pub.publish(Twist())
        rospy.loginfo("Robot is stopped!")
        rospy.sleep(1)

#---------------------------------------------------------------------#
# main()
#---------------------------------------------------------------------#        
if __name__ == '__main__':
    n= toMyrobot()
    try:
        n.moveForward(0.5)
    except rospy.ROSInterruptException:
        pass
 
