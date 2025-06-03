from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# pyside6-uic ui_window.ui -o ui_window.py
# python python_part\setup.py build_ext --inplace
# pyinstaller --onefile --windowed --add-data "example.cp313-win_amd64.pyd;." --icon=favicon.ico --name GraphPlotter python_part/main.py
ext_modules = [
    Pybind11Extension(
        'example',  # Имя модуля
        [r'C:\Python_projects\PracticeProject\cpp_part\pybind\source.cpp'],  # Путь к исходному файлу
        language='c++',
    ),
]

setup(
    name='example',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)
