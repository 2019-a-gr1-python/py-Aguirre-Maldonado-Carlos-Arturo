import buscar
import registrar
import actualizar
import eliminar
import os

def main():
	
	while True:
		os.system ("cls")
		#os.system ("clear") #MAC
		print('\n**********Bienvenido a la tienda Juego Mania*********')
		print('\nMenu de opciones')
		print('\n1. Resgistrar')
		print('\n2. Actualizar')
		print('\n3. Buscar')
		print('\n4. Eliminar')
		print('\n5. Salir')

		numero_accion = int(input('\nIngrese el numero de la opcion escogida: '))

		os.system ("cls")
		#os.system ("clear") #MAC

		if numero_accion is 1:
			registrar.registrar_elemento()
		elif numero_accion is 2:
			actualizar.actualizar_videojuego()
		elif numero_accion is 3:
			buscar.buscar_videojuego()
		elif numero_accion is 4:
			eliminar.eliminar_elemento()
		elif numero_accion is 5:
			break
		else:
		 print("Accion no valida")


main()