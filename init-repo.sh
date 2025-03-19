#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

mkdir -p build; cd build

CONAN_ARGS="\
    -b missing \
    -s build_type=Debug \
    -o clay_test/*:with_raylib_examples=True \
    -o clay_test/*:with_sdl2_examples=True \
    -o clay_test/*:with_cpp_example=True \
    -o clay_test/*:with_demos=True \
    -pr:b=../profiles/linux_x86_64 \
    -pr:h=../profiles/linux_x86_64"

conan install .. -of . ${CONAN_ARGS}
conan build .. -of . ${CONAN_ARGS}
conan create .. ${CONAN_ARGS}
