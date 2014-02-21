#!/usr/bin/env python
# -*- coding: utf-8 -*- 

PKG = 'smart_home_sensors'
NAME = 'sensor_base_test'

import unittest
import sys
import rospy
import rostest
import time
from smart_home_sensors.srv import *
from std_msgs.msg import String

class TestSensorBase(unittest.TestCase):
    def __init__(self, *args):
        super(TestSensorBase, self).__init__(*args)
        self._flag = False

    def test_empty_call(self):
        rospy.Subscriber('sensor_base_test', String, self.callback)
        rospy.init_node(NAME, anonymous=True)
        timeout_t = time.time() + 10.0#*1000 #10 seconds
        while not rospy.is_shutdown() and not self._flag and time.time() < timeout_t:
            time.sleep(0.1)
        self.assertTrue(self._flag, "timeout")

    def callback(self, data):
        self._flag = True

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestSensorBase, sys.argv)
