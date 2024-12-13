import time 
from cpu import CPU 

class GameBoy:
    def __init__(self, rom_path):
        self.cpu = CPU()  # Inicializamos la CPU
        self.rom_path = rom_path
        self.load_rom()  # Cargamos la ROM

    def load_rom(self):
        """Carga el archivo ROM en la memoria de la GameBoy"""
        with open(self.rom_path, 'rb') as f:
            self.cpu.memory[0x0100:] = list(f.read())  # Carga la ROM a partir de 0x0100

    def run(self):
        """Ejecuta el ciclo de la GameBoy"""
        try:
            while True:
                opcode = self.cpu.memory[self.cpu.PC]  # Leemos el opcode en la posición del PC
                cycles = self.cpu.execute(opcode)  # Ejecutamos la instrucción correspondiente
                self.cpu.PC += 1  # Avanzamos el contador de programa
                print(f"Ejecutando opcode {hex(opcode)} en PC {hex(self.cpu.PC)}")
                time.sleep(0.01)  # Esto es solo para simular un pequeño retraso (el ciclo real de la CPU)
        except KeyboardInterrupt:
            print("Emulación detenida.")
