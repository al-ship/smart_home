#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Sensor notification node

import rospy
import uuid
from sensor_base import SensorBase
from fs_sensor import FsSensor
from smart_home_core.msg import Notification

class Notifier(object):

    def __init__(self):
        self.pub = rospy.Publisher('notification', Notification)
        rospy.init_node('sensor_notifier_node')

        sensor_type = rospy.get_param('~sensor_type','fs')
        sensor_param = rospy.get_param('~sensor_param', '')
        self.init_sensor(sensor_type, sensor_param)

        self.notification_text = rospy.get_param('~notification_text', u'Сработал датчик')
        self.notification_level = rospy.get_param('~notification_level', 2)
        self.notification_target = rospy.get_param('~notification_target', 'voice,log')
        self.notification_value = str(rospy.get_param('~notification_value', '1'))

        interval = rospy.get_param('~check_inteval', 10)
        self.timer = rospy.Timer(rospy.Duration(interval), self.timer_call)

    def init_sensor(self, sensor_type, param):
        if sensor_type == 'fs':
            self.sensor = FsSensor(param)
        else:
            rospy.logerr('sensor type %s not found' % sensor_type)

    def stop(self):
        self.timer.shutdown()

    def timer_call(self, event):
        data = ''
        try:
            data = self.sensor.read().strip()
        except:
            rospy.logerr('Ошибка чтения датчика %s' % rospy.get_name())
        #print data + self.notification_value
        if self.notification_value == str(data):
            #print self.notification_text
            self.pub.publish(Notification(str(uuid.uuid1()), self.notification_text, self.notification_level, self.notification_target, "", ()))
#	else:
        #print self.notification_value + "!=" + data

if __name__ == "__main__":
    notifier = Notifier()
    rospy.spin()
    notifier.stop()
