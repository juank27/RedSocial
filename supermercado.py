def tipo_producto():
	producto = 0
	while True:
		print("----------------------------")
		print('''
		1. Alimentos
		2. Aseo
		3. Bebidas
		''')
		print("----------------------------")
		producto = int(input('Seleccione el tipo de producto: '))
		if producto == 1 or producto == 2 or producto == 3:
			break
		else :
			print("Opcion no valida")
	return producto

def agregar_producto(producto, productos):
	productos.append(producto)
	return True

def buscar_producto(producto, productos):
	for p in productos:
		if p == producto:
			return p
	return None

def elimina_producto(producto, productos):
	for p in productos:
		if p == producto:
			productos.remove(p)
			return True
	return False

def mostrar_productos(productos):
	for p in productos:
		print(p)

def menu():
	opcion = 0
	while opcion == 0:
		print("----------------------------")
		print('''
		1. Agregar producto
		2. Buscar producto
		3. Eliminar producto
		4. Mostrar productos
		5. Salir
		''')
		print("----------------------------")
		opcion = int(input('Seleccione una opcion: '))
		if opcion != 1 or opcion != 2 or opcion != 3 or opcion != 4 or opcion != 5:
			print("Opcion no valida")
			opcion = 0
		else :
			break
	return opcion

def main():
	alimentos = []
	aseo = []
	bebidas = []
	productos = alimentos + aseo + bebidas
	while True:
		opcion = menu()
		print("----------------------------")
		print(f"Opcion seleccionada: {opcion}")
		print("----------------------------")
		if opcion == 1:
			producto = tipo_producto()
			if producto == 1:
				agregar_producto(producto, alimentos)
			elif producto == 2:
				agregar_producto(producto, aseo)
			else :
				agregar_producto(producto, bebidas)
		elif opcion == 2:
			#producto = tipo_producto() #elegir el tipo de producto
			producto = input("Ingrese el producto a buscar: ")
			p = buscar_producto(producto, productos)
			if p:
				print("Producto encontrado")
			else:
				print("Producto no encontrado")
		elif opcion == 3:
			producto = tipo_producto()
			p = elimina_producto(producto, productos)
			if p:
				print("Producto eliminado")
				if	producto == 1:
					elimina_producto(producto, alimentos)
				elif producto == 2:
					elimina_producto(producto, aseo)
				else :
					elimina_producto(producto, bebidas)
			else:
				print("Producto no encontrado")
		elif opcion == 4:
			mostrar_productos(productos)
		elif opcion == 5:
			break

if __name__ == '__main__':
	main()