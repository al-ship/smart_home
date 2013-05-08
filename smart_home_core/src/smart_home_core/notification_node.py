#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from smart_home_core.msg import Notification
from std_msgs.msg import String

def callback(notification):
    if 'log' in notification.destination:
        if notification.level == 0:
	    rospy.loginfo(notification.text)
	elif notification.level == 1:
	    rospy.logwarn(notification.text)
	elif notification.level == 2:
	    rospy.logfatal(notification.text)
	else:
	    rospy.logdebug(notification.text)
	    
    if 'voice' in notification.destination:
    #todo check current voice notification level        
	pub.publish(String(notification.text))

    if 'mail' in notification.destination:
    #todo
        pass
    if 'sms' in notification.destination:
    #todo
        pass
    if 'display' in notification.destination:
    #todo
        pass
    if 'audio' in notification.destination:
    #todo
        pass

def notification_node():
    global pub
    pub = rospy.Publisher('speak', String)

    rospy.init_node('notification_node', anonymous=True)
    rospy.Subscriber("notification", Notification, callback)
    rospy.spin()

if __name__ == '__main__':
    notification_node()
