import os
from Videojuego import Videojuego
from Genero import Genero

path = "./registro_videojuegos.txt"

lista_videojuegos = []
lista_generos = []

def llenar_lista_videojuego():
	archivo_abierto = open("./registro_videojuegos.txt")
	lineas_archivo = archivo_abierto.readlines()
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		lista_videojuegos.append(Videojuego(linea_leida[0], linea_leida[1],linea_leida[2]))
		
def llenar_lista_genero():
	archivo_abierto = open("./registro_genero.txt")
	lineas_archivo = archivo_abierto.readlines()
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		lista_generos.append(Genero(linea_leida[0], linea_leida[1], linea_leida[2]))	

def recorrer_lista(lista_objetos, nombre):
	for objeto in lista_objetos:
		if objeto.get_nombre() == nombre:
			return lista_objetos.index(objeto)
	return 
			
def buscar_elemento_por_nombre(elemento, path):
	
	while(True):
		os.system ("cls")
		#os.system ("clear") #MAC
		print('\n********** Buscar '+ elemento +' por nombre ***********')
		print('\nIngrese el nombre del ' + elemento + ' a buscar')
		nombre = input('\nNombre: ')
		os.system ("cls")
		#os.system ("clear") #MAC

		if 	elemento == 'Genero':
			try: 
				print(lista_generos[recorrer_lista(lista_generos, nombre)].imprimir_datos())
			except (TypeError) as nombre_Error:
				print("\nGenero de videojuego no existe\n\nIngrese el nombre de un genero existente")
				return

		else:
			try: 
				videojuego = lista_videojuegos[recorrer_lista(lista_videojuegos, nombre)]
				print('Nombre: '+ videojuego.get_nombre())

				for genero in lista_generos:
					if genero.get_codigo() == videojuego.get_genero():
						print('Genero: ' + genero.get_nombre())
						break

				print('Precio: $'+videojuego.get_precio()) 

			except (TypeError) as nombre_Error:
				print("\nVideojuego no existe\n\nIngrese el nombre de un videojuego existente")
				return

		return
		
		
def imprimir_videojuegos_por_genero():
	for genero in lista_generos:
		print('\n' + genero.get_nombre())
		for videojuego in lista_videojuegos:
			if videojuego.get_genero() == genero.get_codigo():
				print(' 	'+videojuego.get_nombre())

def nueva_busqueda():
	respuesta = input ('\n\n¿Desea realizar otra búsqueda? (Y/N): ')
	if respuesta is 'Y':
			return True
	elif respuesta is 'N':
			os.system ("cls")
			#os.system ("clear") #MAC
			return False	


def imprimir_lista_genero():
	print('\nEscoja el genero del videojuego de la siguiente lista:')
	for elemento in lista_generos:
		print('\n'+str(lista_generos.index(elemento)+1) + '. ' + elemento.get_nombre())

def menu_buscar():

	llenar_lista_genero()
	llenar_lista_videojuego()

	elemento_elegido = ''
	path = ''
	flag = True
	while flag:
		os.system("cls")
		#os.system ("clear") #MAC	
		print('\n********** Buscar ***********')
		print('\nMenu de opciones de busqueda: ')
		print('\n1. Buscar videojuego por nombre')
		print('\n2. Buscar genero por nombre')
		#print('\n3. Buscar videojuego por genero')
		print('\n3. Imprimir videojuego por genero')
		print('\n4. Salir')

		opcion_busqueda = int(input('\nIngrese el numero de la opcion escogida: '))


		if opcion_busqueda is 1:
			buscar_elemento_por_nombre('Videojuego', './registro_videojuegos.txt')
		elif opcion_busqueda is 2:
			buscar_elemento_por_nombre('Genero', './registro_genero.txt')
		elif opcion_busqueda is 3:
			imprimir_videojuegos_por_genero()
		elif opcion_busqueda is 4:
			break
		else:
			os.system ("cls")
			#os.system ("clear") #MAC
			print('Opcion no existe, ingrese un numero valido')

		flag = nueva_busqueda()

	lista_generos.clear()
	lista_videojuegos.clear()

	