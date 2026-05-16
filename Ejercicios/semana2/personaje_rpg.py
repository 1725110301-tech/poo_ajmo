class PersonajeRPG:
    def __init__(self, nombre, clase, nivel,vida, mana,fuerza, defensa,velocidad,arma,oro):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida = vida
        self.mana = mana
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.arma = arma
        self.oro = oro
    def atacar(self):
        print(self.nombre, "ataca con ", self.arma)
    def defender(self):
        print(self.nombre, "defiende con su escudo")
    def usarHabilidad(self):
        print(self.nombre, "usa su habilidad especial")
    def subirNivel(self):
        print(self.nombre, "sube al nivel ", self.nivel)
    def mostrarEstado(self):
        print("Nombre: ", self.nombre)
        print("Clase: ", self.clase)
        print("Nivel: ", self.nivel)
        print("Vida: ", self.vida)
        print("Mana: ", self.mana)
        print("Fuerza: ", self.fuerza)
        print("Defensa: ", self.defensa)
        print("Velocidad: ", self.velocidad)
        print("Arma: ", self.arma)
        print("Oro: ", self.oro)
personaje1 = PersonajeRPG("Arthas", "Guerrero", 10, 100, 50, 20, 15, 10, "Espada", 100)
personaje1.mostrarEstado()
personaje1.atacar()
personaje1.defender()
personaje1.usarHabilidad()
personaje1.subirNivel()
