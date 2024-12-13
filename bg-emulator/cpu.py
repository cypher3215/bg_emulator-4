import opcodesinstrucciones

class CPU:
    def __init__(self):
        # Inicialización de registros
        self.A = 0  # Acumulador
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        self.SP = 0xFFFE  # Stack Pointer (apunta a la dirección 0xFFFE)
        self.PC = 0x0100  # Program Counter (Comienza en 0x0100)

        # Registro de Flags
        self.F = 0x00  # Flags: [Z, N, H, C]
        
        # Memoria
        self.memory = [0] * 65536  # 64KB de memoria
        
        # Tabla de opcodes (esto se puede expandir conforme se necesiten más instrucciones)
        self.instructions = {
            0x00: self.NOP,  # No Operation
            0x01: self.LD_BC, # Cargar BC
            0x02: self.LD_A_BC, # Cargar A desde BC
            0x03: self.INC_BC, # Incrementar BC
            # Agregar más instrucciones aquí
        }

    def reset(self):
        """Reinicia los registros y la memoria"""
        self.A = self.B = self.C = self.D = self.E = self.H = self.L = 0
        self.SP = 0xFFFE
        self.PC = 0x0100
        self.F = 0
        self.memory = [0] * 65536

    # Métodos para gestionar las banderas
    def set_flag(self, flag, value):
        """Establece o limpia una bandera en el registro F"""
        if value:
            self.F |= flag
        else:
            self.F &= ~flag
    
    def get_flag(self, flag):
        """Devuelve el valor de una bandera específica en el registro F"""
        return (self.F & flag) != 0

    # Instrucciones
    def NOP(self):
        """No hace nada, es solo un ciclo de reloj"""
        return 4  # El ciclo de la instrucción NOP es 4

    def LD_BC(self):
        """Cargar el valor inmediato en BC"""
        self.B = self.memory[self.PC + 1]
        self.C = self.memory[self.PC + 2]
        self.PC += 3  # Avanzamos el PC por 3 bytes
        return 12  # El ciclo de la instrucción LD es 12

    def LD_A_BC(self):
        """Cargar el valor de la memoria en la dirección BC en A"""
        bc = (self.B << 8) | self.C
        self.A = self.memory[bc]
        self.PC += 1
        return 8  # El ciclo de la instrucción LD A, (BC) es 8

    def INC_BC(self):
        """Incrementa el valor del par de registros BC"""
        bc = (self.B << 8) | self.C
        bc += 1
        self.B = (bc >> 8) & 0xFF
        self.C = bc & 0xFF
        self.PC += 1
        return 8  # El ciclo de la instrucción INC BC es 8

    # Agregar más instrucciones según sea necesario

    def execute(self, opcode):
        """Ejecuta la instrucción correspondiente al opcode"""
        if opcode in self.instructions:
            cycles = self.instructions[opcode]()  # Llamamos al método correspondiente
            return cycles
        else:
            print(f"Opcode {hex(opcode)} no soportado.")
            return 0
