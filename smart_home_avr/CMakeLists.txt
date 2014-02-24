cmake_minimum_required(VERSION 2.8.3)
project(smart_home_avr)

find_package(catkin REQUIRED COMPONENTS std_msgs message_generation)

catkin_package(CATKIN_DEPENDS message_runtime)

install(DIRECTORY src/ros_lib
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/src
)

install(PROGRAMS make_libraries.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
