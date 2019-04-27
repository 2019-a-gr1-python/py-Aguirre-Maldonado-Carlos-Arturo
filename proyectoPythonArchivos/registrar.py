from Videojuego import Videojuego
from Genero import Genero
import os
import buscar

path = "./registro_videojuegos.txt"

def ingresar_genero():	
	os.system ("cls")
	#os.system ("clear") #MAC
	print('\n********** Nuevo Genero de Videojuego *********')
	print('\nIngrese los siguientes datos: ')
	
	nombre_genero = input('\nNombre: ')
	descripcion_genero = input('\nDescripcion: ')

	os.system ("cls")
	#os.system ("clear") #MAC

	return Genero(nombre_genero[:3],nombre_genero, descripcion_genero)


def ingresar_videojuego():
	buscar.lista_generos
	buscar.llenar_lista_genero()
	os.system ("cls")
	#os.system ("clear") #MAC
	print('\n********** Nuevo Videojuego *********')
	print('\nIngrese los siguientes datos del videojuego: ')

	nombre = input('\nNombre: ')
	buscar.imprimir_lista_genero()
	posicion_genero = int(input('\nGenero: '))
	#censura = input('\nCensura: ')
	precio = input('\nPrecio(ejemplo: $5.00): $')
	#plataforma = input('\nPlataforma: ')
	os.system ("cls")
	#os.system ("clear") #MAC


	genero = buscar.lista_generos[posicion_genero-1].get_codigo()

	buscar.lista_generos.clear()
	
	#return videojuego = Videojuego(nombre, genero, censura, precio, plataforma)
	return Videojuego(nombre, genero, precio)


def menu_registrar():
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
			#os.system ("clear") #MAC
			print('Opcion no existe, ingrese un numero valido')

	return


def registrar(path, objeto):
	file = open(path, "a")
	file.write("\n"+objeto.__str__())
	file.close()

