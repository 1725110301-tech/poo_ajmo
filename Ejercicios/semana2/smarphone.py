class Smartphone:
	def __init__(self, marca, modelo, bateria, almacenamiento, 
			  color, camara, ram, precio, sistema, pantalla):
		self.marca= marca
		self.modelo=modelo
		self.bateria=bateria
		self.almacenamiento=almacenamiento
		self.color= color
		self.camara=camara
		self.ram=ram
		self.precio=precio
		self.sistema=sistema
		self.pantalla=pantalla
	  
		print(f"Marca: {self.marca}")
		print(f"Modelo: {self.modelo}")
		print(f"Bateria: {self.bateria}")
		print(f"Almacenamiento: {self.almacenamiento}")
		print(f"Color: {self.color}")
		print(f"Camara: {self.camara}")
		print(f"RAM: {self.ram}")
		print(f"Precio: {self.precio}")
		print(f"Sistema: {self.sistema}")
		print(f"Pantalla: {self.pantalla}")
iphone14= Smartphone("Apple", "iPhone 14", 95, 128, "Azul", 12, 6, 18000, "iOS", 6.1)


