class Videojuego:
	nombre = ''
	genero = ''
	#censura = 0
	precio = 0.00
	#plataforma = ''

	def __init__(self, nombre, genero, #censura, 
		precio, #plataforma
		):
		self.nombre = nombre
		self.genero = genero
		#self.censura = censura
		self.precio = precio
		#self.plataforma = plataforma

	def __str__(self, modo):
		cadena = ''
		if modo is 'w':	
			#return f'{self.nombre};{self.genero};{self.censura};{self.precio};{self.plataforma}'
			cadena = f'{self.nombre};{self.genero};{self.precio}'
			return cadena

		else:
			cadena = f'Nombre: {self.nombre}\nGenero: {self.genero}\nPrecio: ${self.precio}\n'
			return cadena

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_genero(self, genero):
		self.genero = genero

	def set_precio(self, precio):
		self.precio = precio

