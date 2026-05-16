class Banco:
    def __init__(self, no_clientes, no_elementos_seguridad, no_edificios, sistema_informatico,
                 nombre_banco, no_cajeros, fiable, capital, horario_de_atencion,
                 color):
        self.no_clientes=no_clientes
        self.no_elementos_seguridad=no_elementos_seguridad
        self.no_edificios=no_edificios
        self.sistema_informatico=sistema_informatico
        self.nombre_banco=nombre_banco
        self.no_cajeros=no_cajeros
        self.fiable=fiable
        self.capital=capital
        self.horario_de_atencion=horario_de_atencion
        self.color=color

        print(f"No de Clientes: {self.no_clientes}")
        print(f"No de policias: {self.no_elementos_seguridad}")
        print(f"No de edificios: {self.no_edificios}")
        print(f"Sistema informatico: {self.sistema_informatico}")
        print(f"Nombre del Banco: {self.nombre_banco}")
        print(f"No de cajeros: {self.no_cajeros}")
        print(f"Fiable: {self.fiable}")
        print(f"Capital: {self.capital}")
        print(f"Horario de atencion {self.horario_de_atencion}")
        print(f"Color: {self.color}")

bbva = Banco("41 millones", "4 por sucursal", "1641 sucursales", "BBVA","BBVA app", "14,222 cajeros","Muy fiable",
            "2 millones de euros", "8:30am - 4:00pm", "Azul Obscuro") 
        