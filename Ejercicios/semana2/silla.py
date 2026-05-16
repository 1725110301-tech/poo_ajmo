class Silla:
    def __init__(self, material, ergonomia, portabilidad, no_patas, color, altura,
                 reclinable, tamano, peso, diseno):
        self.material= material
        self.ergonomia= ergonomia
        self.portabilidad= portabilidad
        self.no_patas=no_patas
        self.color=color
        self.altura=altura
        self.reclinable=reclinable
        self.tamano=tamano
        self.peso=peso
        self.diseno=diseno
        
        print(f"Material: {self.material}")
        print(f"Ergonomia: {self.ergonomia}")
        print(f"Portabilidad: {self.portabilidad}")
        print(f"No de patas: {self.no_patas}")
        print(f"Color: {self.color}")
        print(f"Altura: {self.altura}")
        print(f"Reclinable: {self.reclinable}")
        print(f"Tamaño: {self.tamano}")
        print(f"Peso: {self.peso}")
        print(f"Diseño: {self.diseno}")
 
silla_gamer = Silla(
    "Cuero","Alta","Media",
    5,"Negro con rojo","120 cm",True,"Grande",
    "20 kg", "Gamer"
)