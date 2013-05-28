#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospi
import json
from std_msgs.msg import String
from smart_home_core.srv import *
from smart_home_core.msg import Notification

class recognizer(object):

    def __init__(self):
        self.name = 'железяка'
        try:
	   dic_file_path  = rospy.get_param('~dictionary')
	   dic_file = open(dic_file_path, r)
	   self.dictionary = json.load(dic_file)
	   dic_file.close()
	except:
	    rospy.logerr('Please specify a dictionary file properly')
	    return
	try:
	    self.name = rospy.get_param('~name')
	except:
	    rospy.logerr('name not specified, using default: '+self.name)
	# subscribe to the pocketsphinx output    
	rospy.Subscriber('/recognizer/output', String, self.on_speech)
        pub = rospy.Publisher('notification', Notification)
	pub.publish(Notification(str(uuid.uuid1()), "Модуль распознавания речи запущен.", 0, "voice,log", "", ()))

    def translate(self, lst)
        result = ()
	for word in lst:
           for (transl, keywords) in self.dictionary.iteritems():
               for keyword in keywords:
	           if word.find(keyword) > -1:
		       result.add(transl)
        return result

    def on_speech(self, msg):
        # find nickname
	start = msg.data.find(self.name);
	if start > -1:
	    # string after name
	    st = msg.data[start + len(self.name):]
	    #translate it, using dictionary
	    words = self.translate(st.split(' '))
	    st = words.split(' ')
	    try:
	        command = rospy.ServiceProxy('command', Command)
		resp1 = command(st)		    
	    except rospy.ServiceException, e:
	        print "Service call failed: %s"%e	

if __name__=="__main__":
    r = recognizer()
    while not rospy.is_shutdown():
        r.spin()   
