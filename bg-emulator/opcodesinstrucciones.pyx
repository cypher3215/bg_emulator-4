from cython import int
from GameBoy import cpu  # Asegúrate de que "cpu" esté importado correctamente
from cpython.pycapsule cimport PyCapsule_Import

cdef int SET_1F4(cpu.CPU) noexcept nogil:  # 1F4 SET 6,H
    # Modificar el bit 6 del registro H
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.H  # Obtener el valor del registro H
        v |= (1 << 6)  # Establecer el bit 6
        cpu.H = v  # Guardar el nuevo valor en el registro H
    return 0  # Código de operación ejecutado

cdef int SET_1F5(cpu.CPU) noexcept nogil:  # 1F5 SET 6,L
    # Modificar el bit 6 del registro L
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.L  # Obtener el valor del registro L
        v |= (1 << 6)  # Establecer el bit 6
        cpu.L = v  # Guardar el nuevo valor en el registro L
    return 0  # Código de operación ejecutado

cdef int SET_1F6(cpu.CPU) noexcept nogil:  # 1F6 SET 6,(HL)
    # Modificar el bit 6 de la memoria apuntada por HL
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.memory[cpu.HL]  # Obtener el valor de la memoria apuntada por HL
        v |= (1 << 6)  # Establecer el bit 6
        cpu.memory[cpu.HL] = v  # Guardar el nuevo valor en la memoria
    return 0  # Código de operación ejecutado

cdef int SET_1F7(cpu.CPU) noexcept nogil:  # 1F7 SET 6,A
    # Modificar el bit 6 del registro A
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.A  # Obtener el valor del registro A
        v |= (1 << 6)  # Establecer el bit 6
        cpu.A = v  # Guardar el nuevo valor en el registro A
    return 0  # Código de operación ejecutado

cdef int SET_1F8(cpu.CPU) noexcept nogil:  # 1F8 SET 7,B
    # Modificar el bit 7 del registro B
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.B  # Obtener el valor del registro B
        v |= (1 << 7)  # Establecer el bit 7
        cpu.B = v  # Guardar el nuevo valor en el registro B
    return 0  # Código de operación ejecutado

cdef int SET_1F9(cpu.CPU) noexcept nogil:  # 1F9 SET 7,C
    # Modificar el bit 7 del registro C
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.C  # Obtener el valor del registro C
        v |= (1 << 7)  # Establecer el bit 7
        cpu.C = v  # Guardar el nuevo valor en el registro C
    return 0  # Código de operación ejecutado

cdef int SET_1FA(cpu.CPU) noexcept nogil:  # 1FA SET 7,D
    # Modificar el bit 7 del registro D
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.D  # Obtener el valor del registro D
        v |= (1 << 7)  # Establecer el bit 7
        cpu.D = v  # Guardar el nuevo valor en el registro D
    return 0  # Código de operación ejecutado

cdef int SET_1FB(cpu.CPU) noexcept nogil:  # 1FB SET 7,E
    # Modificar el bit 7 del registro E
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.E  # Obtener el valor del registro E
        v |= (1 << 7)  # Establecer el bit 7
        cpu.E = v  # Guardar el nuevo valor en el registro E
    return 0  # Código de operación ejecutado

cdef int SET_1FC(cpu.CPU) noexcept nogil:  # 1FC SET 7,H
    # Modificar el bit 7 del registro H
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.H  # Obtener el valor del registro H
        v |= (1 << 7)  # Establecer el bit 7
        cpu.H = v  # Guardar el nuevo valor en el registro H
    return 0  # Código de operación ejecutado

cdef int SET_1FD(cpu.CPU) noexcept nogil:  # 1FD SET 7,L
    # Modificar el bit 7 del registro L
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.L  # Obtener el valor del registro L
        v |= (1 << 7)  # Establecer el bit 7
        cpu.L = v  # Guardar el nuevo valor en el registro L
    return 0  # Código de operación ejecutado

cdef int SET_1FE(cpu.CPU) noexcept nogil:  # 1FE SET 7,(HL)
    # Modificar el bit 7 de la memoria apuntada por HL
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.memory[cpu.HL]  # Obtener el valor de la memoria apuntada por HL
        v |= (1 << 7)  # Establecer el bit 7
        cpu.memory[cpu.HL] = v  # Guardar el nuevo valor en la memoria
    return 0  # Código de operación ejecutado

cdef int SET_1FF(cpu.CPU) noexcept nogil:  # 1FF SET 7,A
    # Modificar el bit 7 del registro A
    with gil:  # Acceder a los atributos de la clase CPU con GIL activado
        v = cpu.A  # Obtener el valor del registro A
        v |= (1 << 7)  # Establecer el bit 7
        cpu.A = v  # Guardar el nuevo valor en el registro A
    return 0  # Código de operación ejecutado