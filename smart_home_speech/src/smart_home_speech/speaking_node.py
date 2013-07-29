#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
import os
import tempfile
import roslib; roslib.load_manifest('sound_play')
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

class Speaking(object)
    
    def say(data):
        text = data.data
        for key in self.word_map.keys(): # replacing 'bad' words
	    text = text.replace(key, self.word_map[key])
        soundhandle.say(text, 'Elena')
        rospy.sleep(1)

    def __init__():
        rospy.init_node('speaking_node', anonymous = True)
    
        self.wordmap = {} # dict. for replacing 'bad' words
        dic_file_path  = rospy.get_param('~mapfile','russian.map')
        try:
            dic_file = codecs.open(dic_file_path, 'r', 'utf-8')    
            self.word_map = json.load(dic_file)
	    dic_file.close()
        except:
            rospy.logerr('Can not open mapping file %s' % dic_file_path)

        rospy.Subscriber('speak', String, say)


if __name__ == '__main__':
    speaking = Speaking()
    speaking.soundhandle = SoundClient()
    rospy.sleep(1)
    rospy.spin()
