#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
import os
import tempfile
import roslib; roslib.load_manifest('sound_play')
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

throttle = 3 # seconds

def say(data):    
    global allow_yak
    if rospy.Time.now() <= allow_yak: # Throttles yak to avoid
        print("Sound throttled")      # SoundClient segfault
	return
    # when to reallow yak
    allow_yak = rospy.Time.now() + rospy.Duration.from_sec(throttle)
    rospy.logdebug('command for uncached text: "%s"' % data.data)
    txtfile = tempfile.NamedTemporaryFile(prefix='sound_play', suffix='.txt')
    #(wavfile,wavfilename) = tempfile.mkstemp(prefix='sound_play', suffix='.wav')
    txtfilename=txtfile.name
   # os.close(wavfile)
    try:
        txtfile.write(data.data)
        txtfile.flush()
#        os.system("RHVoice -W Elena -i "+txtfilename+" -o "+wavfilename)
	os.system("RHVoice -W Elena -i "+txtfilename+" | aplay")
#	try:
#	    if os.stat(wavfilename).st_size == 0:
#	        raise OSError
#	except OSError:
#	   rospy.logerr('Voice synth faled. Check RHVoice installed')
#	   return
    finally:
        txtfile.close()
    #print wavfilename
    #soundhandle.playWave(wavfilename)
    #rospy.sleep(1)

def speaking_node():
    rospy.init_node('speaking_node', anonymous = True)
    global allow_yak
    allow_yak = rospy.Time.now()
    rospy.Subscriber('speak', String, say)
    rospy.spin()

if __name__ == '__main__':
    soundhandle = SoundClient()
    rospy.sleep(1)
       
    speaking_node()
