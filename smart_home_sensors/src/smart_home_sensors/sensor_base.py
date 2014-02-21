#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Base class for sensors
import rospy
from std_msgs.msg import String
from smart_home_sensors.srv import *

"""
Base class for sensor nodes
"""
class SensorBase(object):

    """
    Reads sensor data (low level).
    Returns object of type get_message_class
    Override this in child class
    """
    def read(self):
       return self.get_message_class()()

    """
    writes sensor data (low level).
    Override this in child class
    """
    def write(self, data):
        pass

    """
    returns class of publishing message.
    Override this in child class
    """
    def get_message_class(self):
        return String

    """
    returns service class for reading sensor data.
    Override this
    """
    def get_read_srv_class(self):
        return None

    """
    Sensor reading handler.
    Returns srv class.
    Override this
    """
    def read_srv_handle(self, req):
        return self.get_read_srv_class()()

    """
    returns service class for writing data to sensor.
    Override this
    """
    def get_write_srv_class(self):
        return None

    """
    Sensor writing handler
    Override this
    """
    def write_srv_handle(self, req):
        return self.get_write_srv_class()

    """
    name of node by default
    """
    def get_name(self):
        return "sensor_base"


    def __init__(self):
        # init publisher for current sensor and message
        self.timer = None
        rospy.init_node(self.get_name())
        if self.get_message_class is not None:
            self.pub = rospy.Publisher(rospy.get_name(), self.get_message_class())
        self.interval = rospy.get_param('~check_interval', 10)
        # init service for reading and writing
        if self.get_read_srv_class() is not None:
            reader = rospy.Service(rospy.get_name() + '/read', self.get_read_srv_class(), self.read_srv_handle)
        if self.get_write_srv_class() is not None:
            writer = rospy.Service(rospy.get_name() + '/write', self.get_write_srv_class(), self.write_srv_handle)
        if self.pub:
            self.timer = rospy.Timer(rospy.Duration(self.interval), self.timer_call)

    def timer_call(self, event):
        try:
            self.pub.publish(self.read())
        except:
            rospy.logerr('sensor read error %s' % rospy.get_name())

    def stop(self):
        if self.timer is not None:
            self.timer.shutdown()

if __name__ == "__main__":
    sensor = SensorBase()
    rospy.spin()
    sensor.stop()


