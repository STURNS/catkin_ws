#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
import tf
class mylaserscan():
    #---------------------------------------------------------------------#
    #init
    #---------------------------------------------------------------------#
    def __init__(self):                  
        rospy.init_node('learn_gmapping', anonymous=False)
        rospy.on_shutdown(self.shutdown)

    #---------------------------------------------------------------------#
    #pub the laser data
    #---------------------------------------------------------------------#	
    def fake_laser(self):
        r = rospy.Rate(1)
        mymap = rospy.Publisher('/base_scan', LaserScan, queue_size=1)
        Laser = LaserScan();
        Laser.header.seq = 10
        Laser.header.stamp = rospy.get_rostime()
        Laser.header.frame_id = '/base_laser'
        Laser.angle_min = 0
        Laser.angle_max = 1
        Laser.angle_increment  =0.1
        Laser.time_increment = 0.5
        Laser.scan_time = 1
        Laser.range_min = 0
        Laser.range_max = 100
        
        
        for i in range(10):           
            Laser.ranges.append(1)
            Laser.ranges[i] = i
            print Laser.ranges[i]
        
        #br = tf.TransformBroadcaster()
       # br.sendTransform((0, 0, 0),
       #              tf.transformations.quaternion_from_euler(0, 0, 0),
       #              rospy.Time.now(),
       #              '/base_link',
       #              "/base_laser")
        while not rospy.is_shutdown():
            mymap.publish(Laser)
            rospy.sleep(1)
            
    #---------------------------------------------------------------------#
    #exit
    #---------------------------------------------------------------------#
    def shutdown(self):
        rospy.loginfo("Stopping the robot...")

if __name__ == '__main__':  
    n = mylaserscan();
    n.fake_laser();                                                                                
	
