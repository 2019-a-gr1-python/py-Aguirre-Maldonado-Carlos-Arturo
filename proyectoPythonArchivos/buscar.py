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

	archivo_abierto.close()
	return

