from pynput.keyboard import Key, Listener

#Mapeo de teclas a botones de la Game Boy
teclas_gameboy = {
    'w': 0x40,  # Arriba
    's': 0x20,  # Abajo
    'a': 0x10,  # Izquierda
    'd': 0x08,  # Derecha
    'j': 0x01,  # A
    'k': 0x02,  # B
    'enter': 0x08,  # Start
    'space': 0x04,  # Select
}

#Mapa de teclas presionadas en hexadecimal
teclas_presionadas = 0x00

#Función que se llama cuando una tecla es presionada
def on_press(key):
    global teclas_presionadas
    try:
        if hasattr(key, 'char') and key.char in teclas_gameboy:
            teclas_presionadas |= teclas_gameboy[key.char]
        elif key == Key.enter:
            teclas_presionadas |= teclas_gameboy['enter']
        elif key == Key.space:
            teclas_presionadas |= teclas_gameboy['space']
        print(f"Teclas presionadas: {hex(teclas_presionadas)}")
    except AttributeError:
        pass

#Función que se llama cuando una tecla es soltada
def on_release(key):
    global teclas_presionadas
    try:
        if hasattr(key, 'char') and key.char in teclas_gameboy:
            teclas_presionadas &= ~teclas_gameboy[key.char]
        elif key == Key.enter:
            teclas_presionadas &= ~teclas_gameboy['enter']
        elif key == Key.space:
            teclas_presionadas &= ~teclas_gameboy['space']
        print(f"Teclas presionadas: {hex(teclas_presionadas)}")
    except AttributeError:
        pass

#Función principal para iniciar el escuchador de teclado
def iniciar_escuchador():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

#Iniciar el escuchador de teclas
iniciar_escuchador()