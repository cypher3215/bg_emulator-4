class Memory:
    def __init__(self):
        # Define áreas de memoria
        self.memory_map = {
            "ROM": (0x0000, 0x1FFFFF),  # 2 MB
            "VRAM": (0x8000, 0x9FFF),   # 8 KB
            "WRAM": (0xC000, 0xDFFF),   # 32 KB
            "SRAM": (0xA000, 0xBFFF),   # 128 KB
        }

        # Inicializa memoria total (2 MB)
        self.memory = [0] * 0x200000  # 2 MB
        self.rom_loaded = False

    def load_rom(self, rom_data):
        """Carga la ROM en la memoria."""
        if len(rom_data) > self.memory_map["ROM"][1] + 1:
            raise ValueError(f"ROM demasiado grande: {len(rom_data)} bytes.")

        self.memory[:len(rom_data)] = rom_data
        self.rom_loaded = True
        print(f"ROM cargada: {len(rom_data)} bytes")

    def memory_usage(self):
        """Calcula el uso de memoria por áreas y devuelve un informe."""
        used_rom = sum(1 for byte in self.memory[self.memory_map["ROM"][0]:self.memory_map["ROM"][1]+1] if byte != 0)
        total_rom = self.memory_map["ROM"][1] - self.memory_map["ROM"][0] + 1
        rom_percentage = (used_rom / total_rom) * 100 if total_rom > 0 else 0

        # Comprobar uso de las otras áreas de memoria
        used_vram = sum(1 for byte in self.memory[self.memory_map["VRAM"][0]:self.memory_map["VRAM"][1]+1] if byte != 0)
        total_vram = self.memory_map["VRAM"][1] - self.memory_map["VRAM"][0] + 1
        vram_percentage = (used_vram / total_vram) * 100 if total_vram > 0 else 0

        used_sram = sum(1 for byte in self.memory[self.memory_map["SRAM"][0]:self.memory_map["SRAM"][1]+1] if byte != 0)
        total_sram = self.memory_map["SRAM"][1] - self.memory_map["SRAM"][0] + 1
        sram_percentage = (used_sram / total_sram) * 100 if total_sram > 0 else 0

        # Resumen del uso de memoria
        return {
            "ROM": {"used": used_rom, "total": total_rom, "percentage": rom_percentage},
            "VRAM": {"used": used_vram, "total": total_vram, "percentage": vram_percentage},
            "SRAM": {"used": used_sram, "total": total_sram, "percentage": sram_percentage},
        }

    def __repr__(self):
        """Representación de la memoria, incluyendo estadísticas de uso."""
        if not self.rom_loaded:
            return "<Memory: ROM no cargada>"
        
        usage = self.memory_usage()

        return (
            f"<Memory: {len(self.memory)} bytes total, "
            f"ROM cargada: {usage['ROM']['used']} bytes / {usage['ROM']['total']} bytes ({usage['ROM']['percentage']:.2f}% utilizada), "
            f"VRAM: {usage['VRAM']['used']} bytes / {usage['VRAM']['total']} bytes ({usage['VRAM']['percentage']:.2f}% utilizada), "
            f"SRAM: {usage['SRAM']['used']} bytes / {usage['SRAM']['total']} bytes ({usage['SRAM']['percentage']:.2f}% utilizada)>"
        )

    def read_byte(self, address):
        """Lee un byte desde una dirección específica de la memoria."""
        if 0 <= address < 0x200000:
            return self.memory[address]
        else:
            raise ValueError(f"Dirección fuera de rango: {address:#04x}")

    def write_byte(self, address, value):
        """Escribe un byte en una dirección específica de la memoria."""
        for area, (start, end) in self.memory_map.items():
            if start <= address <= end:
                if area == "ROM":
                    raise ValueError(f"No se puede escribir en la ROM: {address:#04x}")
                self.memory[address] = value
                return

        raise ValueError(f"Dirección fuera de un área válida de memoria: {address:#04x}")
