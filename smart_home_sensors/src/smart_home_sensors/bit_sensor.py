#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from std_msgs.msg import Bool
from smart_home_sensors.srv import *
from sensor_base import SensorBase

class BitSensor(SensorBase):

    def get_name(self):
        return "bit_sensor"

    def get_message_class(self):
        return Bool

    def __init__(self):
        super(BitSensor, self).__init__()
        self.path = rospy.get_param('~sensor_id', '')

    def read(self):
        f = open(self.path, 'r')
        data = f.read()
        f.close()
        if data == '1':
            return True
        else:
            return False

    def write(self, data):
        f = open(self.path, 'w')
        if data:
            f.write('1')
        else:
            f.write('0')
        f.close()
        return Bool(True)

    def get_read_srv_class(self):
        return ReadSensorBit

    def read_srv_handle(self, req):
       return ReadSensorBitResponse(self.read())

    def get_write_srv_class(self):
        return WriteSensorBit

    def write_srv_handle(self, req):
        self.write(req.value)
        return WriteSensorBitResponse(True)


if __name__ == "__main__":
    sensor = BitSensor()
    rospy.loginfo("bit sensor running %s:%s" % (sesor.get_name(), sensor.path))
    rospy.spin()
    sensor.stop()

