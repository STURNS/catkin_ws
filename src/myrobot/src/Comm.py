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
import tf
from ctypes import c_int16
from geometry_msgs.msg import Quaternion,Twist

class Base_Controller:
    #---------------------------------------------------------------------#
    #init
    #---------------------------------------------------------------------#
    def __init__(self):
        rospy.init_node('comm', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.rate  = rospy.Rate(3) #10Hz
        
        #load the params
        self.port =  rospy.get_param("~port", "/dev/ttyUSB0")
        self.buadrate =  rospy.get_param("~buadrate", 115200)
        self.reg_address = rospy.get_param("~reg_address",
            {'laser_start': 0,'laser_length': 360,'TF_start': 360,'TF_length': 6,
            'Odom_start': 366,'Odom_length': 6,'vel_start':372,'vel_length':2})
           

        self.pub = rospy.Publisher('/laser_scan',LaserScan,queue_size=10)
       
        self.__vel = Twist()
        rospy.Subscriber("cmd_vel", Twist, self.vel_update)
        #Connect to the slave
        #tf     
        self.br = tf.TransformBroadcaster()
        try:
            
            self.master = modbus_rtu.RtuMaster(
                serial.Serial(port=self.port, baudrate=self.buadrate , bytesize=8, parity='N', stopbits=1, xonxoff=0)
            )
            self.master.set_timeout(2.0)
            self.master.set_verbose(True)
            #mb_logger.info("connecting to base_controller...")
            rospy.loginfo("connecting to base_controller...")
            #print(list(self.master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 100)))

        except modbus_tk.modbus.ModbusError as exc:
            rospy.logerr("%s- Code=%d", exc, exc.get_exception_code())
    #---------------------------------------------------------------------#
    #subscribe the vel data
    #---------------------------------------------------------------------#      
    def vel_update(self,req):
        #should add a mutex
        self.__vel = req
        #print(req)
    
    #---------------------------------------------------------------------#
    #poll
    #---------------------------------------------------------------------#          
    def get_data(self):

        n = self.reg_address['laser_length']
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
        
        #get the data from base controller
        din = [0]*self.reg_address['laser_length']
        odom_data = [0]*self.reg_address['TF_length']
        section = int(self.reg_address['laser_length']/100)
        if(self.reg_address['laser_length']%100 != 0):
            section += 1
        while not rospy.is_shutdown():
            #----laser data----
            try:
                for i in range(section):
                    r_start = i*100
                    r_end = r_start+100                  
                    if(r_end > self.reg_address['laser_length']):
                        r_end = self.reg_address['laser_length']
                    din[r_start:r_end] = list(self.master.execute(1, cst.READ_HOLDING_REGISTERS,  r_start,  (r_end- r_start)))
            except Exception as e:
                rospy.loginfo('get data error %s'%e)
                pass

            #----odom data----
            try:
                odom_data =  list(self.master.execute(1, cst.READ_HOLDING_REGISTERS,  
                    self.reg_address['TF_start'],  self.reg_address['TF_length']+self.reg_address['Odom_length']))
            except Exception as e:
                rospy.loginfo('get data error %s'%e)
                pass
            
            #print(odom_data)
            #send vel data to Base_Controller
            # print(self.__vel.linear.x)
            x = int(self.__vel.linear.x*1000)
            y = int(self.__vel.linear.y*1000)
            rz = int(self.__vel.angular.z*1000)
            try : 
                self. master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, self.reg_address['vel_start'],  output_value=[x,y,rz])
               
            except Exception as e:
                print(e)
                pass  

            self.br.sendTransform((1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'odom','world')

            self.br.sendTransform((0.1, 0, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),'map','odom')
            
            self.br.sendTransform((self.mb_realvalue(odom_data[0])/1000.0,
                self.mb_realvalue(odom_data[1])/1000.0 , self.mb_realvalue(odom_data[2])/1000.0),
                tf.transformations.quaternion_from_euler(0, 0,self.mb_realvalue(odom_data[5])/1000.0 ),
                rospy.Time.now(),'base_link','world')
            
            #pubulish laser data       
            laser_data.header.stamp = rospy.Time()
            for i in range(n):
                laser_data.ranges[i] = din[i]/100
                laser_data.intensities[i] = 0
            self.pub.publish(laser_data)                
            self.rate.sleep()     
            
    #---------------------------------------------------------------------#
    #alter mobus value to real value(man can understand)
    #---------------------------------------------------------------------#           
    def mb_realvalue(self,v):
        return float(c_int16(v).value)
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
    BC.get_data()