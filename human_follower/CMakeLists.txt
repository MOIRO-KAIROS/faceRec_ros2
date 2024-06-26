cmake_minimum_required(VERSION 3.8)
project(human_follower)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(moiro_interfaces REQUIRED)

include_directories(
  include
)

# install
install(DIRECTORY
  # launch
  DESTINATION share/${PROJECT_NAME}
)

set(DEPENDENCIES
  "rclcpp"
  "tf2"
  "geometry_msgs"
  "sensor_msgs"
  "moiro_interfaces"
)

# build
add_executable(human_follower src/dynamic_follow.cpp)
ament_target_dependencies(human_follower ${DEPENDENCIES})

install(TARGETS
human_follower
DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
