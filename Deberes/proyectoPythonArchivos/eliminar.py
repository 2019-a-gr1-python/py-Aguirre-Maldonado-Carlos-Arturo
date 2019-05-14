from Videojuego import Videojuego
import os

#path = "./registro_videojuegos.txt"

def eliminar_videojuego(path):
	#os.system ("cls")
	os.system ("clear") #MAC
	print('\n********** Eliminar Videojuego ***********')
	print('\nIngrese el nombre del videojuego a eliminar')
	nombre = input('\nNombre: ')
	#os.system ("cls")
	os.system ("clear") #MAC
	archivo_abierto = open(path,"r")
	lineas_archivo = archivo_abierto.readlines()
	vaciar_archivo(path)
	archivo_abierto = open(path, "a")
	
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		if linea_leida[0] != nombre:
			archivo_abierto.write(str(linea))
	
	archivo_abierto.close()
	return

def eliminar_genero(path):
	#os.system ("cls")
	os.system ("clear") #MAC
	print('\n********** Eliminar Genero ***********')
	print('\nIngrese el nombre del genero a eliminar')
	nombre = input('\nNombre: ')
	#os.system ("cls")
	os.system ("clear") #MAC
	lineas_archivo = leer_archivo(path)

	eliminar_videojuegos_de_genero(nombre[:3], './registro_videojuegos.txt')

	vaciar_archivo(path)

	archivo_abierto = open(path, "a")
	
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		if linea_leida[1] != nombre:
			archivo_abierto.write(str(linea))
	
	archivo_abierto.close()
	return

def eliminar_videojuegos_de_genero(genero, path):
	lineas_archivo = leer_archivo(path)

	vaciar_archivo(path)

	archivo_abierto = open(path, "a")
	
	for linea in lineas_archivo:
		linea_leida = linea.split(";")
		if linea_leida[1] != genero:
			archivo_abierto.write(str(linea))
	
	archivo_abierto.close()

def vaciar_archivo(path):
	archivo = open(path,"w")
	archivo.write("")
	archivo.close()

def leer_archivo(path):
	archivo = open(path,"r")
	return archivo.readlines()


def menu_eliminar():
	
	elemento_elegido = ''
	path = ''
	
	while(True):
		print('\n**************** Eliminar ***************')
		print('\nElementos que se pueden eliminar')
		print('\n1. Genero')
		print('\n2. Videojuego')
		print('\n\n3. Salir')

		numero_opcion = int(input('\nEscriba el numero de la opcion escogida: '))
		

		if numero_opcion is 1:
			eliminar_genero('./registro_genero.txt')
		elif numero_opcion is 2:
			eliminar_videojuego('./registro_videojuegos.txt')
		elif numero_opcion is 3:
			return
		else:
			#os.system ("cls")
			os.system ("clear") #MAC
			print('Opcion no existe, ingrese un numero valido')
			
	return