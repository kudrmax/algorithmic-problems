cmake_minimum_required(VERSION 3.24)
project(leetcode)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE my_src temp.cpp)
add_executable(${PROJECT_NAME} ${my_src})