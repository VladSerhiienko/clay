import os
from conan import ConanFile
from conan.tools.files import copy

class Clay(ConanFile):
    name = "clay"
    version = "1.0"
    # No settings/options are necessary, this is header only
    exports_sources = "include/*"
    # We can avoid copying the sources to the build folder in the cache
    no_copy_source = True

    def package(self):
        print(f"Packing headers from: {os.path.join(self.source_folder, 'include')}")
        print(f"Packing headers to: {os.path.join(self.package_folder, 'include')}")
        copy(self, "*.h", src="include", dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
