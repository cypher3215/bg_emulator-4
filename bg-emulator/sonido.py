import numpy as np
import pygame
import time

# Definir la clase para emular un canal de sonido
class SoundChannel:
    def __init__(self, frequency, wave_type='square'):
        self.frequency = frequency
        self.wave_type = wave_type
        self.sample_rate = 44100  # Frecuencia de muestreo (44100 Hz es común para audio)
        self.amplitude = 0.5  # Volumen
        self.volume = 1.0     # Control del volumen
        self.envelope = 1.0   # Envolvente de volumen simple

    def generate_wave(self, duration):
        """Genera una onda con frecuencia, tipo de onda y duración definidos"""
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        
        if self.wave_type == 'square':
            # Generar una onda cuadrada
            wave = self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * t))
        elif self.wave_type == 'triangle':
            # Generar una onda triangular
            wave = 2 * self.amplitude * np.abs(np.mod(t * self.frequency, 1) - 0.5) - self.amplitude
        elif self.wave_type == 'sawtooth':
            # Generar una onda de sierra
            wave = self.amplitude * (2 * (t * self.frequency - np.floor(t * self.frequency + 0.5)))
        elif self.wave_type == 'noise':
            # Generar ruido blanco
            wave = np.random.uniform(-self.amplitude, self.amplitude, size=t.shape)
        
        # Aplicar envolvente simple (para simular cambios de volumen)
        return wave * self.volume * self.envelope

    def play(self, duration):
        """Genera la onda y la reproduce"""
        wave_data = self.generate_wave(duration)
        
        # Convertir el sonido monoaural en estéreo duplicando los canales
        stereo_wave = np.vstack((wave_data, wave_data)).T  # Duplicamos la señal para estéreo

        # Asegurarse de que el arreglo esté contiguo en memoria
        stereo_wave = stereo_wave.copy()

        # Convertir a sonido en Pygame
        sound = pygame.sndarray.make_sound(stereo_wave.astype(np.float32))  
        sound.play()

# Emulación de la Game Boy con sonidos
class GameBoySoundEmulator:
    def __init__(self, rom_path):
        self.rom_path = rom_path
        self.sample_rate = 44100
        self.channels = []
        self.running = True
        pygame.mixer.init(frequency=self.sample_rate, size=-16, channels=2)  # Inicializar pygame mixer en estéreo
    
    def load_rom(self):
        """ Cargar el archivo de la ROM de GameBoy """
        with open(self.rom_path, 'rb') as rom_file:
            self.rom_data = rom_file.read()

        # Aquí deberíamos leer las instrucciones y registros de la ROM,
        # pero por ahora solo emulamos sonidos básicos.
    
    def emulate_audio(self):
        """ Emular la salida de sonido de la Game Boy """
        # Simulamos dos canales: uno de onda cuadrada y otro de ruido
        square_channel = SoundChannel(frequency=440, wave_type='square')  # Canal de onda cuadrada
        noise_channel = SoundChannel(frequency=5000, wave_type='noise')  # Canal de ruido blanco

        self.channels.append(square_channel)
        self.channels.append(noise_channel)

        # Reproducir los sonidos en un ciclo (esto simula la emulación de la CPU)
        try:
            while self.running:
                for channel in self.channels:
                    channel.play(duration=0.1)  # Reproducir cada canal por 0.1 segundos
                time.sleep(0.1)  # Simular el tiempo entre ciclos de la CPU
        except KeyboardInterrupt:
            print("Emulación detenida.")
            self.running = False

# Código principal
if __name__ == "__main__":
    rom_path = 'a.gb'  # Ruta al archivo .gb
    emulator = GameBoySoundEmulator(rom_path)
    emulator.load_rom()  # Cargar la ROM
    emulator.emulate_audio()  # Emular y reproducir audio