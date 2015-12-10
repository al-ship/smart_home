#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import basemodule
import datetime

class time(basemodule.basemodule):

    names = ['whats time', 'time', u'сколько время', u'который час']

    def __init__(self):
        pass

    def exec_cmd(self, params):
        d = datetime.datetime.now();
        hour = 'часов'
        if (d.hour % 10) == 1:
            hour = 'час'
        elif (1 < (d.hour % 10) < 5) and (d.hour > 20):
            hour = 'часа'

        minute = 'минут'
        if (d.minute % 10) == 1:
            minute = 'минута'
        elif (1 < (d.minute % 10)< 5) and (d.minute > 20):
            minute = 'минуты'

        return 'Текущее время %d %s %d %s' % (d.hour,hour,d.minute,minute)

if __name__ == "__main__":
    t = time();
    print t.exec_cmd('')
