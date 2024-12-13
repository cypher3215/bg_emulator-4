#python3 compiler.py build_ext --inplace
from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("opcodesinstrucciones.pyx")  # Descomenta esta lÃnea para que compile el archivo .pyx
)