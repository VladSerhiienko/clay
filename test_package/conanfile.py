
import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.build import can_run

class ClayTest(ConanFile):
    name = "clay_test"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    options = {
        "with_raylib_examples": [True, False],
        "with_sdl2_examples": [True, False],
        "with_cpp_example": [True, False],
        "with_demos": [True, False],
    }

    default_options = {
        "with_raylib_examples": False,
        "with_sdl2_examples": False,
        "with_cpp_example": False,
        "with_demos": False,
    }

    def requirements(self):
        self.requires(self.tested_reference_str)
        self.requires("raylib/5.5")
        self.requires("sdl/2.28.3")
        self.requires("sdl_ttf/2.24.0")
        self.requires("sdl_image/2.8.2")
        # self.requires("freetype/2.13.3", override=True)
        # self.requires("sdl/3.2.6")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables={
            # Disable all examples by default
            "CLAY_INCLUDE_ALL_EXAMPLES": False,
            # Temporary not supported due to missing packages
            "CLAY_INCLUDE_SDL3_EXAMPLES": False,
            # Enable supported examples based on options
            "CLAY_INCLUDE_RAYLIB_EXAMPLES": self.options.with_raylib_examples,
            "CLAY_INCLUDE_SDL2_EXAMPLES": self.options.with_sdl2_examples,
            "CLAY_INCLUDE_CPP_EXAMPLE": self.options.with_cpp_example,
            "CLAY_INCLUDE_DEMOS": self.options.with_demos,
        })
        cmake.build()

    def test(self):
        if can_run(self):
            self.output.warning("[clay_test]: nothing to test")
            pass
