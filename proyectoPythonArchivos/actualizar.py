from Videojuego import Videojuego
import os

path = "./registro_videojuegos.txt"

def actualizar_videojuego():
	print('\n********** Actualizar Videojuego *********')
	nombre = input('\nNombre:  ')
	archivo_abierto = open(path,"r")
	lineas_archivo = archivo_abierto.readlines()
	archivo_abierto.close()
	archivo_nuevo = open(path,"w")
	archivo_nuevo.write("")
	archivo_nuevo.close()
	file = open(path, "a")
	lineas_archivo_nuevo = []
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] != nombre:
			file.write(str(linea))
		else:
			linea_leida = linea.split(";")
			videojuego = Videojuego(linea_leida[0], linea_leida[1],linea_leida[2])
			os.system ("cls")
			flag = True
			while (flag == True):
				print('\n**************** Actualizar Videojuego *******************')
				print('\nEscoja el dato que desee actualizar:')
				print('\n1. Nombre')
				print('\n2. Genero')
				print('\n3. Precio')
				print('\n\n4. Cancelar')

				dato_a_actualizar = int(input('\nIngrese el numero de la opcion escogida: '))

				if dato_a_actualizar is 1:
					nombre = input('\nIngrese nuevo nombre: ')
					videojuego.set_nombre(nombre)
					file.write(videojuego.__str__('w'))
				elif dato_a_actualizar is 2:
					genero = input('\nIngrese nuevo genero: ')
					videojuego.set_genero(genero)
					file.write(videojuego.__str__('w'))
				elif dato_a_actualizar is 3:
					precio = input('\nIngrese nuevo precio: ')
					videojuego.set_precio(precio)
					file.write(videojuego.__str__('w'))
				elif dato_a_actualizar is 4:
					break
	file.close()
	
	return