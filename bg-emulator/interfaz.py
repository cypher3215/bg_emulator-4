import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QWidget
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
import logging
from memoria import Memory  # Asegúrate de que este módulo esté implementado correctamente

# Configuración básica de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("GameBoy Emulator")

# Constantes de tamaño de la pantalla de GameBoy
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 144

# Paleta de colores GameBoy original (4 tonos de gris)
PALETTE = [
    (255, 255, 255),  # Blanco
    (169, 169, 169),  # Gris claro
    (85, 85, 85),     # Gris oscuro
    (0, 0, 0)         # Negro
]

class GameBoyCPU:
    """Simula la CPU del GameBoy."""

    def __init__(self, memory):
        self.memory = memory
        self.pc = 0x100  # El contador de programa inicial
        self.sp = 0xFFFE  # Puntero de pila
        self.af = 0x01B0  # El par de registros AF (A=0x01, F=0xB0)
        self.bc = 0x0013  # El par de registros BC (B=0x00, C=0x13)
        self.de = 0x00D8  # El par de registros DE (D=0x00, E=0xD8)
        self.hl = 0x014D  # El par de registros HL (H=0x01, L=0x4D)

    def execute_instruction(self):
        """Ejecutar una instrucción según el byte en el contador de programa."""
        instruction = self.memory[self.pc]
        if instruction == 0x00:  # NOP: No hacer nada
            self.pc += 1
        elif instruction == 0x76:  # HALT: Detener la ejecución
            return False
        else:
            # Instrucción ficticia que avanza el programa
            self.pc += 1
        return True

class GameBoyEmulator:
    """Clase para emular el GameBoy completo, incluyendo CPU y pantalla."""

    def __init__(self):
        self.game_loaded = False
        self.framebuffer = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8)
        self.memory = bytearray(0x10000)  # 64KB de memoria
        self.cpu = GameBoyCPU(self.memory)  # Instanciar la CPU

    def cargar_rom(self, ruta):
        """Cargar la ROM y simular la creación del framebuffer."""
        try:
            with open(ruta, 'rb') as rom_file:
                self.rom_data = rom_file.read()

            # Copiar los datos de la ROM en la memoria, comenzando desde la dirección 0x100
            self.memory[0x100:0x100+len(self.rom_data)] = self.rom_data

            # La ROM se carga correctamente
            self.game_loaded = True
            logger.info(f"ROM cargada con éxito desde: {ruta}")
        except Exception as e:
            logger.error(f"Error al cargar la ROM: {str(e)}")
            self.game_loaded = False

    def ejecutar_ciclo(self):
        """Emular un ciclo de la CPU y actualizar el framebuffer."""
        if not self.game_loaded:
            return False

        # Ejecutar el ciclo de la CPU
        if not self.cpu.execute_instruction():
            logger.info("Emulación detenida (HALT).")
            return False  # Detener la emulación

        # Simulación del framebuffer (actualizar la pantalla)
        self.framebuffer = self.simular_buffer_pantalla()

        return True

    def simular_buffer_pantalla(self):
        """Simula el framebuffer de la pantalla de la GameBoy."""
        framebuffer = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8)

        # Simulamos el framebuffer con un patrón de colores simple
        # (Este es solo un patrón básico para propósitos de demostración)
        for y in range(SCREEN_HEIGHT):
            for x in range(SCREEN_WIDTH):
                framebuffer[y, x] = (x + y) % 4  # Crear un patrón de colores de la paleta (0-3)

        return framebuffer

    def obtener_imagen(self):
        """Convertir el framebuffer a una imagen usando la paleta de colores de la GameBoy."""
        if self.framebuffer is None:
            return None

        # Crear una imagen RGB usando la paleta de colores
        image = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)

        # Convertir los valores del framebuffer (0-3) a colores RGB
        for i in range(4):
            mask = self.framebuffer == i
            image[mask] = PALETTE[i]

        return image


class GameBoyWidget(QWidget):
    """Widget personalizado para mostrar la imagen del GameBoy."""

    def __init__(self, emulator):
        super().__init__()

        self.emulador = emulator
        self.setFixedSize(SCREEN_WIDTH * 3, SCREEN_HEIGHT * 3)  # Tamaño fijo de la ventana (escala 3x)
        self.setWindowTitle("Emulador de Game Boy")

        # Crear un temporizador que ejecute ciclos de emulación cada 100ms (aproximadamente 60Hz)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_pantalla)
        self.timer.start(100)  # Actualizar cada 100ms

    def paintEvent(self, event):
        """Evento para pintar la imagen en la pantalla."""
        if self.emulador.game_loaded:
            painter = QPainter(self)
            # Obtener la imagen convertida del framebuffer
            image_data = self.emulador.obtener_imagen()

            if image_data is not None:
                # Convertir la imagen de NumPy a formato QImage
                image = Image.fromarray(image_data)

                # Escalar la imagen al tamaño de la ventana
                image = image.resize((self.width(), self.height()), Image.ANTIALIAS)

                qim = QImage(image.tobytes(), image.width, image.height, image.width * 3, QImage.Format_RGB888)

                # Dibujar la imagen usando QPainter
                painter.drawImage(0, 0, qim)
            painter.end()

    def actualizar_pantalla(self):
        """Actualizar la pantalla al ejecutar un ciclo de la emulación."""
        if not self.emulador.ejecutar_ciclo():
            logger.info("Emulación detenida.")
            self.timer.stop()  # Detener el temporizador cuando la emulación se detenga
        self.repaint()  # Redibujar el widget para actualizar la pantalla


class ROMSelectionWidget(QWidget):
    """Widget de selección de ROM, donde se carga la ROM y luego cambia al widget de emulación."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seleccionar ROM")
        self.setFixedSize(300, 150)

        self.open_button = QPushButton("Abrir ROM", self)
        self.open_button.clicked.connect(self.seleccionar_rom)
        self.open_button.setGeometry(80, 50, 140, 40)  # Colocar el botón en el centro

    def seleccionar_rom(self):
        """Abrir el cuadro de diálogo para seleccionar un archivo ROM y cargarlo."""
        archivo_rom, _ = QFileDialog.getOpenFileName(self, "Seleccionar ROM", "", "Archivos de ROM (*.gb);;Todos los archivos (*)")
        if archivo_rom:
            try:
                logger.info(f"Abriendo ROM: {archivo_rom}")
                # Crear el emulador y cargar la ROM
                emulador = GameBoyEmulator()
                emulador.cargar_rom(archivo_rom)

                # Crear el widget de emulación con el emulador
                self.emulador_widget = GameBoyWidget(emulador)

                # Ocultar el widget actual (de selección de ROM)
                self.close()

                # Mostrar el nuevo widget de emulación
                self.emulador_widget.show()

            except Exception as e:
                logger.error(f"Error al cargar la ROM: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el widget de selección de ROM
        self.rom_selection_widget = ROMSelectionWidget()
        self.setCentralWidget(self.rom_selection_widget)
        self.setFixedSize(300, 150)

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
