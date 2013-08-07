#!/usr/bin/env python
# -*- coding: utf-8 -*- 

PKG = 'smart_home_core'
NAME = 'command_server_test'

import unittest
import sys
import rospy, rostest
from smart_home_core.srv import *

class TestCommandServer(unittest.TestCase):
    
    def test_empty_call(self):
        rospy.wait_for_service('command')
	command = rospy.ServiceProxy('command', Command)        
	resp = command('').response.decode('utf-8')
        self.assertTrue(resp.startswith(u'неизвестная команда'))
    
    def test_wrong_call(self):        
	rospy.wait_for_service('command')
	command = rospy.ServiceProxy('command', Command)
        resp = command('unknown').response.decode('utf-8')
	self.assertTrue(resp.startswith(u'неизвестная команда unknown'))
    
    def test_ok_call(self):
        rospy.wait_for_service('command')
	command = rospy.ServiceProxy('command', Command)        
	resp = command('test param').response.decode('utf-8')
        self.assertTrue(resp.startswith('test ok, param:param'))

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestCommandServer, sys.argv)
    
