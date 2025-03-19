import os
from conan import ConanFile
from conan.tools.files import copy

class Clay(ConanFile):
    name = "clay"
    version = "1.0"
    exports_sources = "*.h", "profiles*"
    no_copy_source = True

    def package(self):
        copy(self, "LICENSE.md", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, pattern="clay.h", src=self.source_folder, dst=os.path.join(self.package_folder, "include"), keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
