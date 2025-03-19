cmake_minimum_required(VERSION 3.27)
project(clay_examples_introducing_clay_video_demo C)
set(CMAKE_C_STANDARD 99)

find_package(raylib)

add_executable(clay_examples_introducing_clay_video_demo main.c)
target_compile_options(clay_examples_introducing_clay_video_demo PUBLIC)
target_include_directories(clay_examples_introducing_clay_video_demo PUBLIC .)
target_link_libraries(clay_examples_introducing_clay_video_demo PUBLIC raylib clay::clay)

add_custom_command(
        TARGET clay_examples_introducing_clay_video_demo POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_SOURCE_DIR}/resources
        ${CMAKE_CURRENT_BINARY_DIR}/resources)
