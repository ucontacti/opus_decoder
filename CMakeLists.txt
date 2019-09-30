cmake_minimum_required(VERSION 2.8.12)
project(celt_decoder)

set(CMAKE_CXX_STANDARD 14)


execute_process(COMMAND conan install .. --build missing)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(celt_decoder main.cpp)
target_link_libraries(celt_decoder ${CONAN_LIBS})