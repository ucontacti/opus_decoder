from conans import ConanFile, CMake
import traceback


class CeltDecoder(ConanFile):
    name = "Celt_Decoder"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    requires = "opus/1.3.1@bincrafters/stable"
    generators = "cmake"


def requirements(self):
    self.requires("opus/1.3.1@bincrafters/stable")


def build(self):
    cmake = CMake(self)
    cmake.configure(source_folder="celtdecoder")
    cmake.build()

def package(self):
        # self.copy("*", dst="include", src="redlib/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
