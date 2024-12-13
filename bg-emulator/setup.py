from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("opcodesinstrucciones.pyx")  # Descomenta esta línea para que compile el archivo .pyx
)