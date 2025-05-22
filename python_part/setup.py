from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pybind11

ext_modules = [
    Pybind11Extension(
        "example",  # Имя модуля
        [r"C:\Python_projects\PracticeProject\cpp_part\pybind\source.cpp"],  # Путь к исходному файлу
        language="c++",
    ),
]

setup(
    name="example",
    version="0.1",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
