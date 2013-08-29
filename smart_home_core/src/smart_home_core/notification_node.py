#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from smart_home_core.msg import Notification
from std_msgs.msg import String
import smtplib

class Notifier(object):

    def __init__(self):
        self.pub = rospy.Publisher('speak', String)
        rospy.init_node('notification_node', anonymous=True)
        rospy.Subscriber("notification", Notification, self.callback)

        self._from = rospy.get_param('~mail_from', 'SmartHome')
        self._to_addr = rospy.get_param('~mail_to', '')
        self._smtp = rospy.get_param('~smtp', 'smtp.gmail.com:587')
        self._smtp_user = rospy.get_param('~smtp_user', '')
        self._smtp_password = rospy.get_param('~smtp_password', '')

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

if __name__ == '__main__':
    n = Notifier()
    rospy.spin()
