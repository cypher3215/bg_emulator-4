import numpy as np

SCREEN_HEIGHT = 144  # Resolución de la pantalla GameBoy (144 píxeles de alto)
SCREEN_WIDTH = 160   # Resolución de la pantalla GameBoy (160 píxeles de ancho)

class GameBoyEmulator:
    """Clase para simular el bucle de actualización del emulador."""

    def __init__(self):
        self.game_loaded = False
        self.framebuffer = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8)  # Inicializamos el framebuffer de la pantalla
        self.memory = bytearray(0x10000)  # 64KB de memoria (GameBoy tiene 64KB de memoria direccionable)
        self.pc = 0x100  # Program Counter (PC), empieza en 0x100 después del encabezado de la ROM
        self.LCDC = 0  # Control de la pantalla (LCDC) - se usa para manejar la visualización
        self.SCX = 0   # Desplazamiento en el eje X
        self.SCY = 0   # Desplazamiento en el eje Y
        self.WX = 0    # Posición de la ventana X
        self.WY = 0    # Posición de la ventana Y

    def cargar_rom(self, ruta):
        """Cargar la ROM en la memoria del emulador."""
        try:
            with open(ruta, 'rb') as rom_file:
                rom_data = rom_file.read()

            # Copiar los datos de la ROM en la memoria, comenzando desde la dirección 0x100
            self.memory[0x100:0x100+len(rom_data)] = rom_data

            # La ROM se cargó correctamente
            self.game_loaded = True
            print(f"ROM cargada con éxito desde: {ruta}")
        except Exception as e:
            print(f"Error al cargar la ROM: {str(e)}")
            self.game_loaded = False

    def ejecutar_ciclo(self):
        """Emular un ciclo de la CPU."""
        if not self.game_loaded:
            return
        
        # Obtener el valor de la memoria en la dirección indicada por el PC
        byte_instruccion = self.memory[self.pc]

        # Emular la ejecución de la instrucción (esto es solo un ejemplo simplificado)
        if byte_instruccion == 0x00:  # NOP: No hacer nada
            self.pc += 1
        elif byte_instruccion == 0x76:  # HALT: Detener la ejecución
            print("Emulación detenida (HALT).")
            return False  # Detener el emulador
        else:
            self.pc += 1  # Avanzar el PC para simular el paso de tiempo de la CPU

        # Actualizar el framebuffer (simulando que se ha actualizado la pantalla)
        self.actualizar_pantalla()

        return True

    def actualizar_pantalla(self):
        """Simular la actualización del framebuffer."""
        # En un emulador real, los registros LCD afectarían al framebuffer aquí
        # Por ahora, usamos valores aleatorios como simplificación
        self.framebuffer = np.random.randint(0, 4, (SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8)
    
    def mostrar_frame(self):
        """Mostrar el framebuffer (imprimir el contenido de la pantalla como simplificación)."""
        # Aquí podríamos imprimir los valores del framebuffer como una representación simplificada
        # En un emulador real, usaríamos una librería gráfica para mostrar la imagen
        for row in self.framebuffer:
            print("".join(str(pixel) for pixel in row))
    
    def reset(self):
        """Restablecer el emulador."""
        self.framebuffer = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH), dtype=np.uint8)
        self.pc = 0x100  # Resetear el PC a 0x100 después del encabezado de la ROM
        self.LCDC = 0
        self.SCX = 0
        self.SCY = 0
        self.WX = 0
        self.WY = 0
        self.game_loaded = False

# Uso del emulador
emulador = GameBoyEmulator()

# Cargar una ROM (esto depende de la ruta del archivo ROM que tengas)
emulador.cargar_rom("b.gb")

# Ejecutar ciclos de emulación
for _ in range(10):
    if not emulador.ejecutar_ciclo():
        break  # Detener si el ciclo encuentra un HALT
    emulador.mostrar_frame()  # Mostrar el estado del framebuffer

# Puedes resetear el emulador en cualquier momento
# emulador.reset()
