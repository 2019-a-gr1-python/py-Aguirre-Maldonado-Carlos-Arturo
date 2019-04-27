from Videojuego import Videojuego
import os
import buscar
import registrar
import eliminar


def menu_actualizar():
	#os.system ("cls")
	#os.system ("clear") #MAC
	while(True):
		print('\n********** Actualizar  *********')
		print('\nElementos que se pueden eliminar')
		print('\n1. Genero')
		print('\n2. Videojuego')
		print('\n\n3. Salir')

		numero_opcion = int(input('\nEscriba el numero de la opcion escogida: '))

		if numero_opcion is 1:
			actualizar_genero()
			break
		elif numero_opcion is 2:
			actualizar_videojuego()
			break
		elif numero_opcion is 3:
			return
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')

def actualizar_videojuego():
	path = "./registro_videojuegos.txt"
	buscar.lista_videojuegos
	buscar.llenar_lista_videojuego()
	print('\n********** Actualizar Videojuego  *********')
	nombre = input('\nNombre:  ')
	posicion = 0
	
	for videojuego in buscar.lista_videojuegos:
		if videojuego.get_nombre() == nombre:
			posicion = buscar.lista_videojuegos.index(videojuego)

	os.system ("cls")
	#os.system ("clear") #MAC

	
	flag = True

	try:
		videojuego = buscar.lista_videojuegos[posicion]
	except (IndexError) as nombre_Error:
		cadena_error = "\nVideojuego no existe\n\nIngrese el nombre de un videojuego existente"
		print(cadena_error)
		flag = False

	while (flag == True):
		os.system ("cls")
		#os.system ("clear") #MAC
		print('\n**************** Actualizar Videojuego *******************')
		print('\nEscoja el dato que desee actualizar:')
		print('\n1. Nombre')
		print('\n2. Genero')
		print('\n3. Precio')
		print('\n\n4. Cancelar')

		dato_a_actualizar = int(input('\nIngrese el numero de la opcion escogida: '))

		if dato_a_actualizar is 1:
			nombre = input('\nIngrese nuevo nombre: ')
			buscar.lista_videojuegos[posicion].set_nombre(nombre)
		elif dato_a_actualizar is 2:
			buscar.imprimir_lista_genero()
			posicion_genero = int(input('\nGenero: '))
			buscar.lista_videojuegos[posicion].set_genero(buscar.lista_generos[posicion_genero-1].get_codigo())
		elif dato_a_actualizar is 3:
			precio = input('\nIngrese nuevo precio: ')
			buscar.lista_videojuegos[posicion].set_precio(precio)
		elif dato_a_actualizar is 4:
			break

	if cadena_error != '':
		return

	eliminar.vaciar_archivo(path)

	archivo_abierto = open(path, 'a')

	for videojuego in buscar.lista_videojuegos:
		archivo_abierto.write(videojuego.__str__())

	archivo_abierto.close()

	buscar.lista_videojuegos.clear()
	buscar.lista_generos.clear()

	return

def actualizar_genero():
	path = "./registro_genero.txt"
	buscar.lista_generos
	buscar.llenar_lista_genero()
	os.system ("cls")
	#os.system ("clear") #MAC
	print('\n********** Actualizar Genero  *********')
	nombre = input('\nNombre:  ')
	posicion = 0
		
	for genero in buscar.lista_generos:
		if genero.get_nombre() == nombre:
			posicion = buscar.lista_generos.index(genero)

	os.system ("cls")
	#os.system ("clear") #MAC
	flag = True
	while (flag == True):
		os.system ("cls")
		#os.system ("clear") #MAC
		print('\n**************** Actualizar Genero *******************')
		print('\nEscoja el dato que desee actualizar:')
		print('\n1. Nombre')
		print('\n2. Descripcion')
		print('\n\n3. Cancelar')

		dato_a_actualizar = int(input('\nIngrese el numero de la opcion escogida: '))

		if dato_a_actualizar is 1:
			nombre = input('\nIngrese nuevo nombre: ')
			buscar.lista_generos[posicion].set_nombre(nombre)
		elif dato_a_actualizar is 2:
			nombre = input('\nIngrese nueva descripcion: ')
			buscar.lista_generos[posicion].set_descripcion(descripcion)
		elif dato_a_actualizar is 3:
			break
		else:
			os.system ("cls")
			#os.system ("clear") #MAC
			print('Opcion no existe, ingrese un numero valido')

	vaciar_archivo(path)		

	archivo_abierto = open(path, 'a')

	for genero in buscar.lista_generos:
		archivo_abierto.write(genero.__str__())

	archivo_abierto.close()

	buscar.lista_generos.clear()

	return