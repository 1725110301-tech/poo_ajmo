class Perro:
    def __init__(self, raza, color, tamano, peso, no_patas, pelaje, recistencia,
                 temperamento, sexo, agilidad):
        self.raza= raza
        self.color= color
        self.tamano=tamano
        self.peso=peso
        self.no_patas=no_patas
        self.pelaje= pelaje
        self.recistencia=recistencia
        self.temperamento=temperamento
        self.sexo=sexo
        self.agilidad=agilidad

        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamano}")
        print(f"Peso: {self.peso}")
        print(f"No Patas: {self.no_patas}")
        print(f"Pelaje: {self.pelaje}")
        print(f"Recistencia: {self.recistencia}")
        print(f"Temperamento: {self.temperamento}")
        print(f"Sexo: {self.sexo}")
        print(f"Agilidad: {self.agilidad}")

perro = Perro(
    "Pastor Alemán",
    "Negro con café",
    "Grande",
    "35 kg",
    4,
    "Corto",
    "Alta",
    "Protector",
    "Macho",
    "Muy rápida"
)