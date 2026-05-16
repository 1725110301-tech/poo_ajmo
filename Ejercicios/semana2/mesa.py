class Mesa:
    def __init__(self, material, ancho, diseno, tamano, tipo, altura, color,
                 portabilidad, soporte, no_patas):
        self.material= material
        self.ancho= ancho
        self.diseno= diseno
        self.tamano= tamano
        self.tipo= tipo
        self.altura= altura
        self.color=color
        self.portabilidad=portabilidad
        self.soporte=soporte
        self.no_patas=no_patas

        print(f"Material: {self.material}")
        print(f"Ancho: {self.ancho}")
        print(f"Diseño: {self.diseno}")
        print(f"Tamaño: {self.tamano}")
        print(f"Tipo: {self.tipo}")
        print(f"Altura: {self.altura}")
        print(f"Color: {self.color}")
        print(f"Portabilidad: {self.portabilidad}")
        print(f"Soporte: {self.soporte}")
        print(f"No Patas: {self.no_patas}")
        
mesa = Mesa(
    "Madera",
    "120 cm",
    "Moderno",
    "Grande",
    "Escritorio",
    "75 cm",
    "Café",
    "Media",
    "Alto peso",
    4
)