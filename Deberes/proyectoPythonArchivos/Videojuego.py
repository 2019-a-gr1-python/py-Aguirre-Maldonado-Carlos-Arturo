class Videojuego:
	nombre = ''
	genero = 0
	precio = 0.00
	
	def __init__(self, nombre, genero, precio):
		self.nombre = nombre
		self.genero = genero
		self.precio = precio

	def __str__(self):
		cadena = ''
		cadena = f'{self.nombre};{self.genero};{self.precio}'
		return cadena
		
	def imprimir_datos(self):
		cadena = ''
		cadena = f'Nombre: {self.nombre}\nGenero: {self.genero}\nPrecio: ${self.precio}\n'
		return cadena

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_genero(self, genero):
		self.genero = genero

	def set_precio(self, precio):
		self.precio = precio

	def get_nombre(self):
		return self.nombre

	def get_genero(self):
		return self.genero

	def get_precio(self):
		return self.precio
