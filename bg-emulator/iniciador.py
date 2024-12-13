import pygame
import time

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana (puedes ajustarlas según tus necesidades)
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 144

# Crear la ventana de Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Título de la ventana
pygame.display.set_caption("GameBoy Emulator")

# Función para cargar y mostrar la imagen del juego
def show_game_image(image_path):
    try:
        # Cargar la imagen del juego (puede ser la imagen de la pantalla)
        game_image = pygame.image.load(image_path)
        
        # Escalar la imagen si es necesario
        game_image = pygame.transform.scale(game_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Rellenar la pantalla con un color de fondo (opcional)
        screen.fill((0, 0, 0))  # Fondo negro
        
        # Dibujar la imagen en la pantalla
        screen.blit(game_image, (0, 0))
        
        # Actualizar la pantalla para reflejar los cambios
        pygame.display.update()
        
    except pygame.error as e:
        print(f"Error al cargar la imagen: {e}")

# Función principal para ejecutar la emulación y mostrar la imagen
def main():
    # Ruta de la imagen (deberías poner aquí la ruta a la imagen que representa la pantalla del juego)
    image_path = "game_screen.png"  # Cambia esta ruta a la correcta
    
    # Bucle principal de la emulación
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mostrar la imagen del juego
        show_game_image(image_path)
        
        # Pausar un poco para que la imagen se vea en la pantalla
        time.sleep(0.1)

    # Cerrar Pygame
    pygame.quit()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
