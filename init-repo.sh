#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

conan create . \
    --test-folder=test_package \
    -b missing \
    -pr:b=profiles/linux_x86_64 \
    -pr:h=profiles/linux_x86_64 \
    -o clay_test/*:with_raylib_examples=True \
    -o clay_test/*:with_sdl2_examples=True \
    -o clay_test/*:with_cpp_example=True \
    -o clay_test/*:with_demos=True
