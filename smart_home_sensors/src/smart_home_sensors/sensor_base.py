#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Base class for sensors

class SensorBase(object):

    def read(self):
        pass
    
    def write(self, data):
        pass
