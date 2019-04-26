from Videojuego import Videojuego
import os

#path = "./registro_videojuegos.txt"

def eliminar(elemento, path):
	print('\n********** Eliminar ' + elemento + ' ***********')
	print('\nIngrese el nombre del ' + elemento.lower() + ' a eliminar')
	nombre = input('\nNombre: ')
	os.system ("cls")
	archivo_abierto = open(path,"r")
	lineas_archivo = archivo_abierto.readlines()
	archivo_abierto = open(path,"w")
	archivo_abierto.write("")
	archivo_abierto = open(path, "a")
	
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] != nombre:
			archivo_abierto.write(str(linea))
	
	archivo_abierto.close()
	return

def eliminar_elemento():
	
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
			elemento_elegido = 'Genero'
			path ='./registro_genero.txt'
			break
		elif numero_opcion is 2:
			elemento_elegido = 'Videojuego'
			path ='./registro_videojuegos.txt'
			break
		elif numero_opcion is 3:
			return
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')
	eliminar(elemento_elegido, path)
	return