#!/usr/bin/python
# -*- coding: utf-8 -*-

import basemodule
import json
import subprocess
import shlex
import xml.etree.ElementTree as ET
import sys

class Weather(basemodule.basemodule):

    def exec_cmd(self, params):
        #args = shlex.split('wget -q -O - "http://informer.gismeteo.ru/rss/28440.xml"')
        args = shlex.split('wget -q -O - "http://meteoinfo.ru/rss/forecasts/28440"')
        out,err = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
        if not err and len(out) > 20:
            result = ''
            root = ET.fromstring(out)
            txt = 'погода в екатеринбурге '
            if 'tomorrow' in params:
                txt = txt + 'на завтра. ' + root.find("./channel/item[last()-1]/description").text.encode('utf-8')
            else:
                txt = txt + '.' + root.find("./channel/item/description").text.encode('utf-8')
            return txt


    def __init_(self):
        pass

if __name__ == "__main__":
    t = Weather();
    print t.exec_cmd(sys.argv)

