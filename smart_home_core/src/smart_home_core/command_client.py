#!/usr/bin/env python

import roslib; roslib.load_manifest('smart_home_core')

import sys

import rospy
from smart_home_core.srv import *

def command_client(row):
    rospy.wait_for_service('command')
    try:
        command = rospy.ServiceProxy('command', Command)
        resp1 = command(row)
        return resp1.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) > 0:
        sys.argv.pop(0)
        command = ' '.join(sys.argv)
    else:
        print usage()
        sys.exit(1)
    print "command: %s" % command
    print "> %s" % command_client(command)
