cmake_minimum_required(VERSION 3.4...3.22)
project(BuildAll LANGUAGES CXX)

include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/dependencies.cmake)

add_subdirectory(engine)
