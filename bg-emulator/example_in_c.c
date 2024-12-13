# cpu.pyx


# cpu.pyx

cdef class CPU:
    # Definimos los registros principales de la CPU (A, B, C, D, E, H, L, etc.)
    cdef uint8_t A, B, C, D, E, H, L
    cdef uint8_t memory[65536]  # Simulamos la memoria del sistema
    
    # Constructor para inicializar los registros y la memoria
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        self.memory = [0] * 65536

    # Funciones para manipular los bits de los registros y memoria

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1B6(self) noexcept nogil:
        # RES 6, (HL) - Resetea el bit 6 del valor en la memoria apuntada por HL
        self.memory[self.H << 8 | self.L] &= ~(1 << 6)
        return 8  # Tiempos de ciclo, puedes ajustar según sea necesario

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1B7(self) noexcept nogil:
        # RES 6, A - Resetea el bit 6 del registro A
        self.A &= ~(1 << 6)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1B8(self) noexcept nogil:
        # RES 7, B - Resetea el bit 7 del registro B
        self.B &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1B9(self) noexcept nogil:
        # RES 7, C - Resetea el bit 7 del registro C
        self.C &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BA(self) noexcept nogil:
        # RES 7, D - Resetea el bit 7 del registro D
        self.D &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BB(self) noexcept nogil:
        # RES 7, E - Resetea el bit 7 del registro E
        self.E &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BC(self) noexcept nogil:
        # RES 7, H - Resetea el bit 7 del registro H
        self.H &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BD(self) noexcept nogil:
        # RES 7, L - Resetea el bit 7 del registro L
        self.L &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BE(self) noexcept nogil:
        # RES 7, (HL) - Resetea el bit 7 del valor en la memoria apuntada por HL
        self.memory[self.H << 8 | self.L] &= ~(1 << 7)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t RES_1BF(self) noexcept nogil:
        # RES 7, A - Resetea el bit 7 del registro A
        self.A &= ~(1 << 7)
        return 8

    # SET Instructions (Set bits)

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C0(self) noexcept nogil:
        # SET 0, B - Seta el bit 0 del registro B
        self.B |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C1(self) noexcept nogil:
        # SET 0, C - Seta el bit 0 del registro C
        self.C |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C2(self) noexcept nogil:
        # SET 0, D - Seta el bit 0 del registro D
        self.D |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C3(self) noexcept nogil:
        # SET 0, E - Seta el bit 0 del registro E
        self.E |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C4(self) noexcept nogil:
        # SET 0, H - Seta el bit 0 del registro H
        self.H |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C5(self) noexcept nogil:
        # SET 0, L - Seta el bit 0 del registro L
        self.L |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C6(self) noexcept nogil:
        # SET 0, (HL) - Seta el bit 0 de la memoria apuntada por HL
        self.memory[self.H << 8 | self.L] |= (1 << 0)
        return 8

    @cython.locals(v=int, flag=uint8_t, t=int)
    cdef uint8_t SET_1C7(self) noexcept nogil:
        # SET 0, A - Seta el bit 0 del registro A
        self.A |= (1 << 0)
        return 8

    # Incluir más instrucciones SET y RES según sea necesario, siguiendo el mismo patrón

    # Ejecutar una instrucción (se puede extender para manejar códigos de operación)
    def execute_instruction(self, opcode: int):
        # Esto mapea los códigos de operación a las funciones correspondientes.
        if opcode == 0x1B6: return self.RES_1B6()
        elif opcode == 0x1B7: return self.RES_1B7()
        elif opcode == 0x1B8: return self.RES_1B8()
        elif opcode == 0x1B9: return self.RES_1B9()
        elif opcode == 0x1BA: return self.RES_1BA()
        elif opcode == 0x1BB: return self.RES_1BB()
        elif opcode == 0x1BC: return self.RES_1BC()
        elif opcode == 0x1BD: return self.RES_1BD()
        elif opcode == 0x1BE: return self.RES_1BE()
        elif opcode == 0x1BF: return self.RES_1BF()
        elif opcode == 0x1C0: return self.SET_1C0()
        elif opcode == 0x1C1: return self.SET_1C1()
        elif opcode == 0x1C2: return self.SET_1C2()
        elif opcode == 0x1C3: return self.SET_1C3()
        elif opcode == 0x1C4: return self.SET_1C4()
        elif opcode == 0x1C5: return self.SET_1C5()
        elif opcode == 0x1C6: return self.SET_1C6()
        elif opcode == 0x1C7: return self.SET_1C7()
        # Agregar más condiciones según se agreguen más instrucciones
        else:
            return 0  # No se encuentra el opcode



#Cuando quieras que la CPU ejecute una instrucción, simplemente llamas al método execute_instruction pasando el opcode de la instrucción que deseas ejecutar, como por ejemplo:


#cpu = CPU()
#cpu.execute_instruction(0x1C0)  # Ejecutar SET 0, B