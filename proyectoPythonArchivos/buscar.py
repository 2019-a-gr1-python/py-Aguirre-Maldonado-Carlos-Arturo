import os
from Videojuego import Videojuego

path = "./registro_videojuegos.txt"

def recorrer_archivo(lineas_archivo, nombre):
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] == nombre:
			linea_leida = linea.split(";")
			#videojuego = Videojuego(linea_leida[0], linea_leida[1],linea_leida[2],linea_leida[3],linea_leida[4])
			return Videojuego(linea_leida[0], linea_leida[1],linea_leida[2])
			

def buscar_videojuego():
	#flag = True
	while(True):
		os.system ("cls")
		print('\n********** Buscar Videojuego ***********')
		print('\nIngrese el nombre del videojuego a buscar')
		nombre = input('\nNombre: ')
		os.system ("cls")
		archivo_abierto = open(path)
		#lineas_archivo = archivo_abierto.readlines()
	
		#for linea in lineas_archivo:
			#linea_leida = linea.split(";",1)
			#if linea_leida[0] == nombre:
				#linea_leida = linea.split(";")
				#videojuego = Videojuego(linea_leida[0], linea_leida[1],linea_leida[2],linea_leida[3],linea_leida[4])
				#videojuego = Videojuego(linea_leida[0], linea_leida[1],linea_leida[2])
				#break
	
		print(recorrer_archivo(archivo_abierto.readlines(), nombre).__str__('p'))
		respuesta = input ('\n\n¿Desea realizar otra búsqueda? (Y/N): ')
		
		archivo_abierto.close()

		if respuesta is 'Y':
			continue
		elif respuesta is 'N':
			os.system ("cls")
			break

	return



def menu_buscar():
	while True:
		
		print('\n********** Buscar ***********')
		print('\nMenu de opciones de busqueda: ')
		print('\n1. Buscar videojuego por nombre')
		print('\n2. Buscar genero por nombre')
		print('\n3. Buscar videojuego por genero')
		print('\n4. Salir')

		opcion_busqueda = int(input('\nIngrese el numero de la opcion escogida: '))


		if opcion_busqueda is 1:
			buscar_videojuego()
		elif opcion_busqueda is 4:
			break
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')
