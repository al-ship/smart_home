#!/usr/bin/python
# -*- coding: utf-8 -*-

import basemodule
import json
import subprocess
import shlex
import xml.etree.ElementTree as ET

class news(basemodule.basemodule):
    names = ['news', u'новости']

    def exec_cmd(self, params):
        args = shlex.split('wget -q -O - "http://news.google.ru/news?um=1&cf=all&ned=ru_ru&hl=ru&output=rss"')
        out,err = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
        if not err and len(out) > 20:
            result = ''
            root = ET.fromstring(out)
            for item in root.iter('item'):
                text = item.find('title').text.encode('utf-8')
                result = '%s %s.' % (result, text)
            return 'Новости...' + result;


    def __init_(self):
        pass

if __name__ == "__main__":
       t = news();
       print t.exec_cmd('')

