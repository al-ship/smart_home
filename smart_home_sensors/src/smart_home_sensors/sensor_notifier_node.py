#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Sensor notification node

import rospy
import uuid
#from sensor_base import SensorBase
#from fs_sensor import FsSensor
from smart_home_core.msg import Notification
import rostopic
import roslib

class Notifier(object):

    def __init__(self):
        self.pub = rospy.Publisher('notification', Notification)
        rospy.init_node('sensor_notifier_node')

        sensor_topic = rospy.get_param('~sensor_topic', None)
        if sensor_topic == None:
            rospy.logerr('param sensor_topic not defined')

        self.notification_text = rospy.get_param('~notification_text', u'sensor activated')
        self.notification_level = rospy.get_param('~notification_level', 2)
        self.notification_target = rospy.get_param('~notification_target', 'voice,log')
        self.notification_value = rospy.get_param('~notification_value', '1')
        self.criteria = rospy.get_param('~criteria', 'eq')
        # subscribe to sensor topic
        data_type = rostopic.get_topic_type(sensor_topic, blocking=False)[0]
        if data_type:
            data_class = roslib.message.get_message_class(data_type)
            rospy.Subscriber(sensor_topic, data_class, self.callback)
            rospy.loginfo("start listening to %s, notification: %s %s", sensor_topic, self.criteria, str(self.notification_value))
        else:
            rospy.logerr("error getting type for topic " + sensor_topic)

    def callback(self, value):
        #rospy.loginfo(str(value.data) + self.criteria + str(self.notification_value)
        # value mast be one of std_msgs (field data)
        if (self.criteria == 'eq' and value.data == self.notification_value ) or \
           (self.criteria == 'gt' and value.data > self.notification_value ) or \
           (self.criteria == 'lt' and value.data < self.notification_value ) or \
           (self.criteria == 'ge' and value.data >= self.notification_value ) or \
           (self.criteria == 'le' and value.data <= self.notification_value ) or \
           (self.criteria == 'ne' and value.data != self.notification_value ):
            self.pub.publish(Notification(str(uuid.uuid1()), self.notification_text, self.notification_level, self.notification_target, "", ()))

if __name__ == "__main__":
    notifier = Notifier()
    rospy.spin()
