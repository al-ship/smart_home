#!/usr/bin/env python
# -*- coding: utf-8 -*- 

PKG = "smart_home_core"
NAME = "notification_node_test"

import unittest
import sys
import rosunit
import rospy
from smart_home_core.notification_node import *
import datetime

class TestNotificationNode(unittest.TestCase):

    def test_get_interval(self):
        interval = get_interval("10:10:10-20:20:20", "%H:%M:%S")
        self.assertEquals(interval[0], datetime.time(10,10,10), "10:10:10 problem")
        self.assertEquals(interval[1], datetime.time(20,20,20), "20:20:20 problem")

    def test_is_interval(self):
        interval = [datetime.time(10,0,0), datetime.time(20,0,0)]
        self.assertTrue(is_interval(interval, datetime.time(15,0,0)), "15:00 not in 10:00-20:00")
        self.assertFalse(is_interval(interval, datetime.time(22,0,0)), "22:00 in 10:00-20:00")

        interval = [datetime.time(20,0,0), datetime.time(10,0,0)]
        self.assertTrue(is_interval(interval, datetime.time(22,0,0)), "22:00 not in 20:00-10:00")
        self.assertFalse(is_interval(interval, datetime.time(11,0,0)), "11:00 in 20:00-10:00")

if __name__ == '__main__':
    if __name__ == '__main__':
        rosunit.unitrun(PKG, NAME, TestNotificationNode, sys.argv)
