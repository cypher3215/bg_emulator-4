import pygame
import time
from cpu import CPU 

class GameBoyEmulator:
    def __init__(self):
        # Inicializamos la CPU y la pantalla de Pygame
        self.cpu = CPU()
        pygame.init()
        self.screen = pygame.display.set_mode((160, 144))  # Tamaño de pantalla de la GameBoy
        pygame.display.set_caption("GameBoy Emulator")

    def render(self):
        """Renderizar una imagen de la memoria en la pantalla (simplemente 0s y 1s por ahora)"""
        self.screen.fill((255, 255, 255))  # Fondo blanco

        for y in range(144):
            for x in range(160):
                color = (0, 0, 0) if self.cpu.memory[0x8000 + y * 160 + x] == 1 else (255, 255, 255)
                pygame.draw.rect(self.screen, color, pygame.Rect(x, y, 1, 1))

        pygame.display.update()

    def run(self):
        """Ciclo principal de ejecución"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Ejecutar el ciclo de la CPU
            self.cpu.run()

            # Renderizar la pantalla
            self.render()

            time.sleep(0.02)  # Mantener 50 FPS

        pygame.quit()

# Iniciar el emulador
if __name__ == "__main__":
    emulator = GameBoyEmulator()
    emulator.run()
