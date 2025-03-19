import os
from conan import ConanFile
from conan.tools.files import copy

class Clay(ConanFile):
    name = "clay"
    version = "1.0"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        copy(self, "*.h", src="include", dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
