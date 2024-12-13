#pip install cython
from GameBoy import GameBoy
from setuptools import setup
#from Cython.Build import cythonize -- no lo pude solucionar intento que compile todo en un archivo
# python pero falla el compilador creo que puede se porque uso pyx y no pdx como mostraba el github
# de pyboy

#setup(
#    ext_modules=cythonize("opcodesinstrucciones.pyx")
#)

if __name__ == "__main__":
    rom_path = "b.gb"  # Ruta del archivo .gb
    gameboy = GameBoy(rom_path)
    gameboy.run()  # Inicia la ejecución del juego
