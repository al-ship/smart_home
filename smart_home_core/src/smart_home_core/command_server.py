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
	     if inspect.isclass (obj) and issubclass(obj, modules.basemodule.basemodule):
	             _modules[module_name] = obj()
         #check
         if _modules.has_key(module_name):
	     print "module '%s' loaded" % module_name
	 else:
	     print "error: module '%s' has no class '%s'!" % (module_name, module_name) 
   
   #test
   #Command.command = 'say weather asdf'
   #print handle_command(Command).response
   #return ''
   global pub
   pub = rospy.Publisher('notification', Notification)
   rospy.init_node('command_server')
   s = rospy.Service('command', Command, handle_command)
   pub.publish(Notification(str(uuid.uuid1()), "Командный интерпретатор запущен.", 0, "voice,log", "", ()))
   rospy.spin()

def handle_command(req):
   print "Parsing '%s'"%req.command
   params = req.command.split(' ')
   cmd = params.pop(0).lower()
   module = params.pop(0).lower()
   response = '"%s" not implemented' %cmd

   if cmd == 'say':
      if _modules.has_key(module):
         #module_p = module.basemodule.basemodule(modules[module]);
         response = _modules[module].exec_cmd(params)
      else:
         response = 'no module with name "%s" found' % module
      pub.publish(Notification(str(uuid.uuid1()), response, 0, "voice","", ()))
  #TODO

   return CommandResponse(response)

if __name__ == "__main__":
   command_server()
