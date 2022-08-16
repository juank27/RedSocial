def agregar_contacto(contactos, phone, name):
	contactos[phone] = name
	return True

def buscar_contacto(contactos, phone):
	return contactos.get(phone, "Contacto no encontrado")

def mostrar_contactos(contactos):
	for phone, name in contactos.items():
		print(f"{phone} - {name}")

def elimina_contacto(contactos, phone):
	contactos.pop(phone, "Contacto no encontrado")

def menu():
	while True:
		print("----------------------------")
		print('''
			1. Agregar contacto
			2. Buscar contacto
			3. Eliminar contacto
			4. Mostrar contactos
			5. Salir
		''')
		print("----------------------------")
		opcion = int(input('Seleccione una opcion: '))
		if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
			break
		else :
			print("Opcion no valida")
	return opcion

def main():
	contactos = {}
	while True:
		opcion = menu()
		print("----------------------------")
		print(f"Opcion seleccionada: {opcion}")
		print("----------------------------")
		if opcion == 1:
			phone = input("Ingrese el telefono: ")
			name = input("Ingrese el nombre: ")
			agregar_contacto(contactos, phone, name)
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
			break

if __name__ == '__main__':
	main()
