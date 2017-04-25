#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import roslib ,rospy
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from sensor_msgs.msg  import  LaserScan
from math import pi,pow,sin,cos

class Base_Controller:
    #---------------------------------------------------------------------#
    #init
    #---------------------------------------------------------------------#
    def __init__(self):
        rospy.init_node('comm', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.rate  = rospy.Rate(3) #10Hz

        #load the params
        self.port =  rospy.get_param("~port", "/dev/ttyUSB1")
        self.buadrate =  rospy.get_param("~buadrate", 115200)

        self.pub = rospy.Publisher('/laser_scan',LaserScan,queue_size=10)
        #Connect to the slave
        #mb_logger = modbus_tk.utils.create_logger("console")
        try:
            
            self.master = modbus_rtu.RtuMaster(
                serial.Serial(port=self.port, baudrate=self.buadrate , bytesize=8, parity='N', stopbits=1, xonxoff=0)
            )
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            #mb_logger.info("connecting to base_controller...")
            rospy.loginfo("connecting to base_controller...")
            print(list(self.master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 100)))
        except modbus_tk.modbus.ModbusError as exc:
            rospy.logerr("%s- Code=%d", exc, exc.get_exception_code())
    #---------------------------------------------------------------------#
    #poll
    #---------------------------------------------------------------------#          
    def pub_data(self):

        n = 100
        lrange = pi
        laser_data = LaserScan()
        laser_data.range_max = 10
        laser_data.range_min = 0.1
        laser_data.angle_max = lrange
        laser_data.angle_min = 0
        laser_data.angle_increment = lrange/(n-1)
        for i in range(n):
            laser_data.ranges.append(0)
            laser_data.intensities.append(0)
        laser_data.header.frame_id = 'base_link'
        while not rospy.is_shutdown():
            din = list(self.master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 100))
            laser_data.header.stamp = rospy.Time()
            for i in range(n):
                laser_data.ranges[i] = din[i]/100
                laser_data.intensities[i] = 0
            self.pub.publish(laser_data)
            self.rate.sleep()
    #---------------------------------------------------------------------#
    #poll
    #---------------------------------------------------------------------#
    #def poll(self):
    #    while rospy.is_shutdown()

    #---------------------------------------------------------------------#
    #poll
    #---------------------------------------------------------------------#
    def shutdown(self):
        rospy.loginfo("Exiting Base_Controller")


if __name__ == "__main__":
    BC = Base_Controller()
    BC.pub_data()