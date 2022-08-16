#no good
def functionn(h):
	a = (13/5) -(2*4)
	result = (h^3) * a
	return result

print(functionn(5))

name = " Juan "
print("Hello World",name,"lastname")
print(f"Hello World{name}lastname")

#good
def algoritmo(a,b,c):
	result = (a**3 * (b**2 - 2*(a*c)))/(2 * b)
	return result
print(algoritmo(3,2,1))
import math
print(3**3)
print(math.pow(3, 3))

# Ejerccio 1 de notas
parciales = [50,50,50,50]
proyecto_final  = 50
nota_final = 50

def porcentajeNota(nota , porcentaje):
	return (nota * porcentaje) / 100

def definitiva	(parciales, proyecto_final, nota_final):
	sum = 0
	for parcial in parciales:
		sum += parcial
	print(sum)
	sum = sum/len(parciales)
	print(sum)
	return porcentajeNota(sum, 55) + porcentajeNota(nota_final, 15) + porcentajeNota(proyecto_final, 30)

print("------------- Definitiva de Notas -------------")
print(f"parciales: {parciales}")
print(f"proyecto_final: {proyecto_final}")
print(f"nota_final: {nota_final}")
print(f"La definitiva es : {definitiva(parciales, proyecto_final, nota_final)}")
print("----------------------------------------------")

# Ejerccio 2
# Definir si es par o impares
def par(a, b):
	if a % 2 == 0 and b % 2 == 0:
		print("Ambos son pares")
	elif a % 2 == 0:
		print("El primer numero es par")
	elif b % 2 == 0:
		print("El segundo numero es par")
	else:
		print("Ambos son impares")

par(1,1)

# Ejerccio 3
# definir si es una vocal
def vocal(a):
	if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
		print("Es una vocal")
	else:
		print("No es una vocal")

vocal("x")
# ------------------ Listas ------------------
lista = [1,2,3,4,5]
print(lista[-4])
lista.append(6) #agregar al final
lista.insert(0, 0) #corre los elementos
lista.extend([6,7,8,9,10]) #agrega al final
lista.pop() #elimina el ultimo elemento
lista.pop(0) #elimina el elemento en la posicion 0
print(lista.index(3)) #devuelve la posicion del elemento
print(lista.count(3)) #devuelve la cantidad de veces que se repite el elemento
lista.sort(reverse=True) #ordena la lista de mayor a menor
lista.reverse() #invierte la lista
lista2 = lista.copy() #copia la lista
lista.clear() #elimina todos los elementos de la lista

print(lista)

# ------------------ tuplas ------------------
tupla = (1,2,3,4,5)
print(tupla[0])
print(tupla[-1])
print(tupla[1:3])
lista = list(tupla) #convierte la tupla en lista
tupla = tuple(lista) #convierte la lista en tupla

# ------------------ diccionarios ------------------
diccionario = {
	"nombre": "Juan",
	"apellido": "Perez",
	"edad": 25
}
print(diccionario.keys()) #devuelve las llaves


print(diccionario["nombre"]) #devuelve el valor de la llave
print(diccionario.get("nombre", "no se encuetra")) #devuelve el valor de la llave, y si no mensaje de error
print("nombre" in diccionario) #devuelve true o false si existe la llave
diccionario["nombre"] = "Juan Carlos" #cambia el valor de la llave
diccionario["telefono"] = "123456" #agrega una nueva llave
print(diccionario)
diccionario.pop("telefono") #elimina la llave
del(diccionario["nombre"]) #elimina la llave
diccionario.popitem() #elimina la ultima llave
print(diccionario)
print(diccionario.keys()) #devuelve las llaves
print(diccionario.values()) #devuelve los valores
print(diccionario.items()) #devuelve las llaves y los valores
diccionario2 = diccionario.copy() #copia el diccionario
diccionario.clear() #elimina todos los elementos del diccionario