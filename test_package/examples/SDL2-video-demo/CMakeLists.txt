cmake_minimum_required(VERSION 3.27)
project(SDL2_video_demo C)
set(CMAKE_C_STANDARD 99)

find_package(SDL2_ttf)
find_package(SDL2_image)
find_package(SDL2)

add_executable(SDL2_video_demo main.c)

target_compile_options(SDL2_video_demo PUBLIC)
target_include_directories(SDL2_video_demo PUBLIC .)

target_link_libraries(SDL2_video_demo PUBLIC
    SDL2::SDL2main
    SDL2::SDL2-static
    SDL2_ttf::SDL2_ttf-static
    SDL2_image::SDL2_image-static
)

add_custom_command(
        TARGET SDL2_video_demo POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_SOURCE_DIR}/resources
        ${CMAKE_CURRENT_BINARY_DIR}/resources)
