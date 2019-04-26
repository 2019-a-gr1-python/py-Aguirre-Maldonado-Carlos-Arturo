from Videojuego import Videojuego
from Genero import Genero
import os

path = "./registro_videojuegos.txt"

def ingresar_genero():
	os.system ("cls")
	print('\n********** Nuevo Genero de Videojuego *********')
	print('\nIngrese los siguientes datos: ')
	
	nombre_genero = input('\nNombre: ')
	descripcion_genero = input('\nDescripcion: ')

	os.system ("cls")

	return Genero(nombre_genero, descripcion_genero)


def ingresar_videojuego():
	os.system ("cls")
	print('\n********** Nuevo Videojuego *********')
	print('\nIngrese los siguientes datos del videojuego: ')

	nombre = input('\nNombre: ')
	genero = input('\nGenero: ')
	#censura = input('\nCensura: ')
	precio = input('\nPrecio(ejemplo: $5.00): $')
	#plataforma = input('\nPlataforma: ')
	os.system ("cls")
	
	#return videojuego = Videojuego(nombre, genero, censura, precio, plataforma)
	return Videojuego(nombre, genero, precio)


def registrar_elemento():
	while(True):
		print('\n**************** Registro ***************')
		print('\nLista de elementos que se pueden ingresar')
		print('\n1. Genero')
		print('\n2. Videojuego')
		print('\n\n3. Salir')

		numero_opcion = int(input('\nEscriba el numero de la opcion escogida: '))

		if numero_opcion is 1:
			registrar("./registro_genero.txt", ingresar_genero())
			break
		elif numero_opcion is 2:
			registrar("./registro_videojuegos.txt", ingresar_videojuego())
			break
		elif numero_opcion is 3:
			break
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')

	return


def registrar(path, objeto):
	file = open(path, "a")
	file.write(objeto.__str__('w') + "\n")
	file.close()