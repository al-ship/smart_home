#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from std_msgs.msg import Float32
from smart_home_sensors.srv import *
from bit_sensor import BitSensor

class FloatSensor(BitSensor):

    def get_name(self):
        return "float_sensor"

    def get_message_class(self):
        return Float32

    def __init__(self):
        super(FloatSensor, self).__init__()

    def read(self):
        f = open(self.path, 'r')
        data = f.read()
        f.close()
        return float(data)

    def write(self, data):
        f = open(self.path, 'w')
        f.write(data)
        f.close()
        return Bool(True)

    def get_read_srv_class(self):
        return ReadSensorFloat

    def read_srv_handle(self, req):
       return ReadSensorFloatResponse(self.read())

    def get_write_srv_class(self):
        return WriteSensorFloat

    def write_srv_handle(self, req):
        self.write(req.value)
        return WriteSensorFloatResponse(True)


if __name__ == "__main__":
    sensor = FloatSensor()
    rospy.loginfo("Float sensor running %s:%s" % (sensor.get_name(), sensor.path))
    rospy.spin()
    sensor.stop()




