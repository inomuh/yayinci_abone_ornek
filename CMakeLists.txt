cmake_minimum_required(VERSION 2.8.3)
project(yayinci_abone_ornek)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

 generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

foreach(dir launch scripts)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()