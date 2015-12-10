#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from smart_home_core.srv import *
import rospy
import os
import inspect
import modules.basemodule
from smart_home_core.msg import Notification
import uuid

plugin_dir = "modules"
_modules = {}

def command_server():
    #load modules
    modules_dir = os.path.dirname(os.path.realpath(__file__)) + '/' + plugin_dir
    print 'Loading modules from /%s' % modules_dir
    for fname in os.listdir(modules_dir):
        if fname.endswith (".py")  and fname != "basemodule.py" and fname != "__init__.py":
            module_name = fname[: -3]
            print "Load module '%s'..." % module_name
            package_obj = __import__(plugin_dir + "." + module_name)
            module_obj = getattr (package_obj, module_name)
            for elem in dir (module_obj):
                obj = getattr (module_obj, elem)
                if inspect.isclass(obj) and issubclass(obj, modules.basemodule.basemodule):
                    add_module(obj(), module_name)
            #check
            if _modules.has_key(module_name):
                 print "module '%s' loaded" % module_name
            else:
                 print "error: module '%s' has no class '%s'!" % (module_name, module_name)
    global pub
    pub = rospy.Publisher('notification', Notification, queue_size=10)
    rospy.init_node('command_server')
    rospy.sleep(1)
    s = rospy.Service('command', Command, handle_command)
    pub.publish(Notification(str(uuid.uuid1()), "Командный интерпретатор запущен.", 0, "voice,log", "", ()))
    rospy.spin()

def add_module(module, name):
    _modules[name] = module
    for key in module.names:
        _modules[key] = module

def handle_command(req):
    print "Parsing '%s'"%req.command
    params = req.command.split(' ')
    cmd = ''
    module = ''
    if len(params) > 0:
        cmd = params.pop(0).lower()
    if len(params) > 0:
        module = params.pop(0).lower()
    response = 'неизвестная команда %s' % cmd

    if cmd == 'switch':
        if _modules.has_key(module):
            response = _modules[module].exec_cmd(params)
    elif cmd == 'test':
        response = 'test ok, param:%s'%module
    elif cmd == 'say':
        if _modules.has_key(module):
            response = _modules[module].exec_cmd(params)
        else:
            response = 'не могу ничего сказать про это %s %s' % (module, " ".join(params))
    else:
        if _modules.has_key(cmd):
            response = _modules[cmd].exec_cmd(params)
        else:
            response = exec_command(req.command)

    return CommandResponse(response)

def exec_command(command):
    command = command.decode('utf-8')
    for key in _modules.keys():
        if key in command:
            return _modules[key].exec_cmd(command.split(' '))
    return u'неизвестная команда'

if __name__ == "__main__":
    command_server()
