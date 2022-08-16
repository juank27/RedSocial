def agregar_contacto(contactos, phone, name):
	contactos[phone] = name
	return True

def buscar_contacto(contactos, phone):
	return contactos.get(phone, "Contacto no encontrado")

def mostrar_contactos(contactos):
	for phone, name in contactos.items():
		print(f"{phone} - {name}")

def mostrar_contactos_total(contactos):
	for phone, name,cedula, operador in contactos.items():
		print(f"Telefono - {phone}")
		print(f"Nombre - {name}")
		print(f"Cedula - {cedula}")
		print(f"Operador - {operador}")

def elimina_contacto(contactos, phone):
	contactos.pop(phone, "Contacto no encontrado")

def agregar_Operador(operador, name):
	operador.append(name)
	return True

def mostrar_operador(operador):
	for name in operador:
		print(f"{name}")

def menu():
	while True:
		print("------------------------------------------------------------------")
		print('''
			1. Agregar contacto
			2. Buscar contacto
			3. Eliminar contacto
			4. Mostrar contactos
			5. Agregar operador
			6. Mostrar Operadores
			7. Salir
		''')
		print("------------------------------------------------------------------")
		opcion = int(input('Seleccione una opcion: '))
		if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7:
			break
		else :
			print("Opcion no valida")
	return opcion

def existe_cedula(cedula, cedulas):
	for c in cedulas:
		if c == cedula:
			return True
	return False

def comprobar_celular(celular, contactos):
	if celular in contactos:
		return True
	else:
		return False

def mostrar_operador(operador):
	i = 0
	for name in operador:
		print(str(i) + " " + name)
		i += 1


def main():
	cedulas = (
		11111111,
		22222222,
		33333333,
		44444444,
		55555555,
		66666666,
		77777777,
		88888888,
	)
	operador = ["movistar", "claro", "tigo"]
	contactos = {}
	while True:
		opcion = menu()
		print("----------------------------")
		print(f"Opcion seleccionada: {opcion}")
		print("----------------------------")
		if opcion == 1:
			phone = input("Ingrese el telefono: ")
			name = input("Ingrese el nombre: ")
			cedula = int(input("Ingrese su cedula: "))
			#mostrar_operador(operador)
			#operador_decicion = input("Ingrese el operador: ").lower()
			existe_cedulaa = existe_cedula(cedula, cedulas)
			while True:
				if existe_cedulaa:
					veric_numero = comprobar_celular(phone, contactos)
					if veric_numero:
						print("El numero ya existe")
						break
					else:
						while True:
							mostrar_operador(operador)
							eleccion_operador = input("Ingrese el operador: ").lower()
							if eleccion_operador in operador:
								agregar_contacto(contactos, phone, name)
								print("Contacto agregado")
								break
							else:
								print("Operador no valido")
								mostrar_operador(operador)
				else:
					print("Cedula no valida")
					cedula = int(input("Ingrese su cedula: "))
					existe_cedulaa = existe_cedula(cedula, cedulas)
		elif opcion == 2:
			phone = input("Ingrese el telefono: ")
			contacto = buscar_contacto(contactos, phone)
			if contacto:
				print(contacto)
			else:
				print("El contacto no existe")
		elif opcion == 3:
			phone = input("Ingrese el telefono: ")
			elimina_contacto(contactos, phone)
		elif opcion == 4:
			mostrar_contactos(contactos)
		elif opcion == 5:
			name = input("Ingrese el nombre del operador: ")
			agregar_Operador(operador, name)
		elif opcion == 6:
			mostrar_operador(operador)
		elif opcion == 7:
			break

if __name__ == '__main__':
	main()
