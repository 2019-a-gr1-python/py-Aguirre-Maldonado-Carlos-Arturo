import os
from Videojuego import Videojuego
from Genero import Genero

path = "./registro_videojuegos.txt"

lista_videojuegos = []
lista_generos = []

def llenar_arreglo_videojuego():
	archivo_abierto = open("./registro_videojuegos.txt")
	lineas_archivo = archivo_abierto.readlines()
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		print(lista_videojuegos)
		lista_videojuegos.append(Videojuego(linea_leida[0], linea_leida[1],linea_leida[2]))
		
def llenar_arreglo_genero():
	archivo_abierto = open("./registro_genero.txt")
	lineas_archivo = archivo_abierto.readlines()
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		lista_generos.append(Genero(linea_leida[1], linea_leida[2]))	

def recorrer_lista(lista_objetos, nombre):
	for objeto in lista_objetos:
		if objeto.get_nombre() == nombre:
			return objeto.imprimir_datos()
			#break

def buscar_elemento_por_nombre(elemento, path):
	
	while(True):
		os.system ("cls")
		print('\n********** Buscar '+ elemento +' por nombre ***********')
		print('\nIngrese el nombre del ' + elemento + ' a buscar')
		nombre = input('\nNombre: ')
		os.system ("cls")
		
		if 	elemento == 'Videojuego':
			print(recorrer_lista(lista_videojuegos, nombre))
		else:
			print(recorrer_lista(lista_generos, nombre))

		respuesta = input ('\n\n¿Desea realizar otra búsqueda? (Y/N): ')
		
		if respuesta is 'Y':
			return True
		elif respuesta is 'N':
			os.system ("cls")
			return False		

def buscar_videojuego_por_genero():

	while(True):
		os.system ("cls")
		print('\n********** Buscar videojuego por genero ***********')
		imprimir_lista_genero()
		posicion_genero = input('\nGenero: ')
		os.system ("cls")

		imprimir_lista_videojuego_por_genero(posicion_genero)

		videojuego = input('\nVideojuego: ')

		print(recorrer_lista(lista_videojuegos))

		if 	elemento == 'Videojuego':
			print(recorrer_lista(lista_videojuegos, nombre))
		else:
			print(recorrer_lista(lista_generos, nombre))

def imprimir_videojuegos_por_genero():
	for genero in lista_generos:
		print('\n' + genero.get_nombre())
		for videojuego in lista_videojuegos:
			if videojuego.get_genero == genero.get_nombre:
				print('\n 	'+videojuego.get_nombre)
		print('\n')

def imprimir_lista_genero():
	print('\nEscoja el genero del videojuego de la siguiente lista:')
	for elemento in lista_generos:
		print('\n'+str(lista_generos.index(elemento)+1) + '. ' + elemento.get_nombre())

#def imprimir_lista_videojuego_por_genero(genero):
	#print('\nEscoja el videojuego de la siguiente lista:')
	#i = 1
	#for elemento in lista_videojuegos:
		#if elemento.get_genero() == genero:
			#print('\n'+ str(i) + '. ' + elemento.get_nombre())
			#i = i+1

def menu_buscar():

	llenar_arreglo_genero()
	llenar_arreglo_videojuego()


	elemento_elegido = ''
	path = ''
	flag = True
	while flag:
		os.system("cls")	
		print('\n********** Buscar ***********')
		print('\nMenu de opciones de busqueda: ')
		print('\n1. Buscar videojuego por nombre')
		print('\n2. Buscar genero por nombre')
		print('\n3. Buscar videojuego por genero')
		print('\n4. Imprimir videojuego por genero')
		print('\n5. Salir')

		opcion_busqueda = int(input('\nIngrese el numero de la opcion escogida: '))


		if opcion_busqueda is 1:
			elemento_elegido = 'Videojuego'
			path = './registro_videojuegos.txt'
			#break
		elif opcion_busqueda is 2:
			elemento_elegido = 'Genero'
			path = './registro_genero.txt'
			#break
		elif opcion_busqueda is 4:
			imprimir_videojuegos_por_genero()
			#break
		elif opcion_busqueda is 5:
			break
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')

		flag = buscar_elemento_por_nombre(elemento_elegido, path)


	