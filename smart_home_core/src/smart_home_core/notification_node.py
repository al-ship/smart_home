#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from smart_home_core.msg import Notification
from std_msgs.msg import String
import smtplib
from datetime import datetime
import re

class Notifier(object):

    _time_mask = "%H:%M:%S"
    _pattern = "^\d\d:\d\d:\d\d-\d\d:\d\d:\d\d$"

    def __init__(self):
        self.pub = rospy.Publisher('speak', String)
        rospy.init_node('notification_node', anonymous=True)
        rospy.Subscriber("notification", Notification, self.callback)

        self._from = rospy.get_param('~mail_from', 'SmartHome')
        self._to_addr = rospy.get_param('~mail_to', '')
        self._smtp = rospy.get_param('~smtp', 'smtp.gmail.com:587')
        self._smtp_user = rospy.get_param('~smtp_user', '')
        self._smtp_password = rospy.get_param('~smtp_password', '')
        #silence interval
        default_inteval = '21:00:00-09:00:00'
        str_interval = rospy.get_param('~silence_interval', default_interval)
        pattern = re.compile(_pattern)
        if pattern.match(str_interval):
            self.silence_interval = get_interval(str_interval, _time_mask)
        else:
            self.silence_interval = get_interval(default_interval, _time_mask)
        rospy.sleep(1)
        print 'notification started'
        self.pub.publish('модуль уведомлений запущен')

    def callback(self, notification):
        print notification.destination
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
        #    print notification.text
            if not is_interval(self.silence_inteval, datetime.now().time()):
                self.pub.publish(String(notification.text))

        if 'mail' in notification.destination:
            self.send_mail(notification)
        if 'sms' in notification.destination:
            #todo
            pass
        if 'display' in notification.destination:
            #todo
            pass
        if 'audio' in notification.destination:
            #todo
            pass

    def send_mail(self, notification):
        if not self._to_addr:
            rospy.logwarn("Can't send email. Check email parameters")
            return
        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( self._from, self._to_addr, self.level_to_text(notification.level), notification.text)
        try:
            server = smtplib.SMTP(self._smtp)
#           server.set_debuglevel(1);
            server.starttls()
            server.login(self._smtp_user, self._smtp_password)
            server.sendmail(self._from, self._to_addr, msg)
            server.quit()
        except Exception, e:
            rospy.logwarn("email sending error: %s", e)

    def level_to_text(self, level):
        if level == 1:
            return "SmartHome: Внимание!"
        elif level == 2:
            return "SmartHome: Тревога!!!"
        else:
            return "SmartHome: Информация"

def get_interval(interval, time_mask):
    intervals = interval.split('-')
    if len(intervals) != 2:
        rospy.logerror("silence_interval - wrong format")
    return[datetime.strptime(intervals[0], time_mask).time(), datetime.strptime(intervals[1], time_mask).time()]

def is_interval(interval_, time_):
    if len(interval_) != 2:
        return false;
    return (interval_[0] < interval_[1] and (interval_[0] < time_ < interval_[1])) or\
        (interval_[0] > interval_[1] and (time_ > interval_[0] or time_ < interval_[1]))


if __name__ == '__main__':
    n = Notifier()
    rospy.spin()
