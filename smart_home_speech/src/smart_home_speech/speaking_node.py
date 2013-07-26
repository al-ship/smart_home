#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
import os
import tempfile
import roslib; roslib.load_manifest('sound_play')
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

#throttle = 3 # seconds

def say(data):
    soundhandle = SoundClient()
    soundhandle.say(data.data, 'Elena')
    rospy.sleep(1)

def speaking_node():
    rospy.init_node('speaking_node', anonymous = True)
    #global allow_yak
    #allow_yak = rospy.Time.now()
    rospy.Subscriber('speak', String, say)
    rospy.spin()

if __name__ == '__main__':
    #soundhandle = SoundClient()
    rospy.sleep(1)
       
    speaking_node()
