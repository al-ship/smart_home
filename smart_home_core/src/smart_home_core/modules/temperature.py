#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import basemodule

class Temperature(basemodule.basemodule):

    names = ['temperature', u'температуру', u'сколько градусов']
    path = '/mnt/1wire/28.87B236040000/fasttemp'

    def exec_cmd(self, params):
        f = open(self.path, 'r')
        data = f.read()
        f.close()
        data = data.strip().replace('-', 'минус ')
        if '.' in data:
            data = data.replace('.', ' и ') + ' десятых градуса'
        else:
            data = data + ' градусов'
        return 'температура %s' % data

if __name__ == "__main__":
    t = Temperature();
    print t.exec_cmd(sys.argv)
