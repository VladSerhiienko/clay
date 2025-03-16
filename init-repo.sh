#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

mkdir -p conan_build
cd conan_build

conan_args="-of . -s build_type=Debug -o with_raylib_examples=True -o with_sdl2_examples=True -o with_cpp_example=True -o with_demos=True -pr:b=../profiles/linux_x86_64 -pr:h=../profiles/linux_x86_64"
conan install .. -b missing ${conan_args}
conan build .. -b missing ${conan_args}
