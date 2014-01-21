#!/usr/bin/env python

TEMPLATE_PACKAGE = "rosserial_client"

__usage__ = """
make_libraries.py generates the smart_home_avr library files.

rosrun smart_home_avr make_libraries.py <output_path>
"""

import rospkg
import rosserial_client
from rosserial_client.make_library import *

# for copying files
import shutil

ROS_TO_EMBEDDED_TYPES = {
    'bool'    :   ('bool',              1, PrimitiveDataType, []),
    'byte'    :   ('int8_t',            1, PrimitiveDataType, []),
    'int8'    :   ('int8_t',            1, PrimitiveDataType, []),
    'char'    :   ('uint8_t',           1, PrimitiveDataType, []),
    'uint8'   :   ('uint8_t',           1, PrimitiveDataType, []),
    'int16'   :   ('int16_t',           2, PrimitiveDataType, []),
    'uint16'  :   ('uint16_t',          2, PrimitiveDataType, []),
    'int32'   :   ('int32_t',           4, PrimitiveDataType, []),
    'uint32'  :   ('uint32_t',          4, PrimitiveDataType, []),
    'int64'   :   ('int64_t',           8, PrimitiveDataType, []),
    'uint64'  :   ('uint64_t',          4, PrimitiveDataType, []),
    'float32' :   ('float',             4, PrimitiveDataType, []),
    'float64' :   ('float',             4, AVR_Float64DataType, []),
    'time'    :   ('ros::Time',         8, TimeDataType, ['ros/time']),
    'duration':   ('ros::Duration',     8, TimeDataType, ['ros/duration']),
    'string'  :   ('char*',             0, StringDataType, []),
    'Header'  :   ('std_msgs::Header',  0, MessageDataType, ['std_msgs/Header'])
}

# need correct inputs
if (len(sys.argv) < 2):
    print __usage__
    exit()

# get output path
path = sys.argv[1]
if path[-1] == "/":
    path = path[0:-1]
print "\nExporting to %s" % path

rospack = rospkg.RosPack()

# copy ros_lib stuff in
#template_dir = rospack.get_path(TEMPLATE_PACKAGE)
#shutil.copytree(template_dir+"/src/ros_lib", path+"/ros_lib")
rosserial_client_copy_files(rospack, path+"/ros_lib/")

# generate messages
rosserial_generate(rospack, path+"/ros_lib", ROS_TO_EMBEDDED_TYPES)

