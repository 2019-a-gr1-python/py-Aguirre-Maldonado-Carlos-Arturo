class Genero:
	codigo = ''
	nombre = ''
	descripcion = ''

	def __init__(self, nombre, descripcion):
		self.codigo = nombre[:3]
		self.nombre = nombre
		self.descripcion = descripcion
		
	def __str__(self):
		cadena = ''
		cadena = f'{self.codigo};{self.nombre};{self.descripcion}'
		return cadena

	def imprimir_datos(self):
		cadena = ''
		cadena = f'Nombre: {self.nombre}\nDescripcion: {self.descripcion}\n'
		return cadena

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_descripcion(self, descripcion):
		self.descripcion = descripcion

	def get_nombre(self):
		return self.nombre

	def get_codigo(self):
		return self.codigo
