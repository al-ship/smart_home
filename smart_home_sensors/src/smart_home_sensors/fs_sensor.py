#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File system sensor (for 1-wire fuse fs)
import sys
from sensor_base import SensorBase

class FsSensor(SensorBase):

    def __init__(self, path):
        self.path = path

    def read(self):
        f = open(self.path, 'r')
        data = f.read()
        f.close()
        return data

    def write(self, data):
        f = open(self.path, 'w')
        f.write(data)
        f.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        sensor = FsSensor(sys.argv[0])
        print 'reading file %s:'%sensor.path
        print sensor.read()
	print 'writing 0 to file %s'%sensor.path
	sensor.write('0')
    else:
        print "provide path as argument"
