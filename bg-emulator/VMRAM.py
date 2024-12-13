import pygame
import numpy as np
import time
import os

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla de la Game Boy
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 144
TILE_SIZE = 8  # Tamaño de un tile de la Game Boy (8x8 píxeles)

# Crear la ventana de Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emulador Game Boy")

# Colores (simulados para Game Boy: blanco y negro)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase para manejar la "pantalla" de la Game Boy
class GameBoyScreen:
    def __init__(self):
        # Inicializar la pantalla con píxeles blancos
        self.pixels = np.ones((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8) * 255  # Fondo blanco
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def update_screen(self):
        # Convertir el arreglo de píxeles a una imagen de Pygame
        pygame.surfarray.blit_array(self.surface, self.pixels)
        screen.blit(self.surface, (0, 0))  # Dibujar en la ventana principal

    def set_tile(self, tile, x_offset, y_offset):
        """Coloca un tile en la pantalla en la posición especificada"""
        for y in range(TILE_SIZE):
            for x in range(TILE_SIZE):
                color = WHITE if tile[y, x] == 0 else BLACK  # 0 = blanco, 1 = negro
                self.set_pixel(x_offset + x, y_offset + y, color)

    def set_pixel(self, x, y, color):
        """Poner un píxel en la posición (x, y) con un color"""
        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
            self.pixels[y, x] = color

# Función para cargar la ROM y extraer la VRAM
def load_rom(rom_path):
    try:
        with open(rom_path, "rb") as rom_file:
            rom_data = rom_file.read()
        print(f"ROM cargada correctamente desde {rom_path}")
        return rom_data
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar la ROM en la ruta {rom_path}")
        return None

# Función para extraer los tiles de la VRAM
def extract_tiles(vram_data):
    tiles = []
    for i in range(0, len(vram_data), TILE_SIZE * TILE_SIZE // 8):
        tile = np.zeros((TILE_SIZE, TILE_SIZE), dtype=np.uint8)
        for y in range(TILE_SIZE):
            byte1 = vram_data[i + y * 2]
            byte2 = vram_data[i + y * 2 + 1]
            for x in range(TILE_SIZE):
                # Establecer el valor del pixel en base a los bits de los bytes
                pixel_value = 0
                if ((byte1 >> (7 - x)) & 1):
                    pixel_value += 1
                if ((byte2 >> (7 - x)) & 1):
                    pixel_value += 2
                tile[y, x] = pixel_value
        tiles.append(tile)
    return tiles

# Función principal para ejecutar la emulación
def main():
    rom_path = "b.gb"  # Asegúrate de poner la ruta correcta de tu ROM
    print("Cargando la ROM...")
    rom_data = load_rom(rom_path)
    
    if rom_data is None:
        return  # Si no se pudo cargar la ROM, salimos de la ejecución

    # La VRAM se encuentra a partir de la dirección 0x8000 en la ROM
    vram_data = rom_data[0x8000:0xA000]  # La VRAM ocupa entre 0x8000 y 0xA000 en la memoria

    # Extraer tiles de la VRAM
    print("Extrayendo tiles de la VRAM...")
    tiles = extract_tiles(vram_data)

    # Inicializar la pantalla de la Game Boy
    gameboy_screen = GameBoyScreen()

    print("Emulando la pantalla de la Game Boy...")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar algunos tiles en la pantalla
        tile_index = 0
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            for x in range(0, SCREEN_WIDTH, TILE_SIZE):
                tile = tiles[tile_index]
                gameboy_screen.set_tile(tile, x, y)
                tile_index += 1
                if tile_index >= len(tiles):
                    break

        # Actualizar la pantalla
        gameboy_screen.update_screen()

        # Actualizar la ventana de Pygame
        pygame.display.flip()

        # Simulación de retraso (esto es solo para no ir demasiado rápido)
        time.sleep(0.01)

    pygame.quit()

if __name__ == "__main__":
    main()
