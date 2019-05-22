##Listas
#lista =[1,2,3,4,5]
#lista2 =[6,7,8,"pepe","juan",6,7,8,6]

##Agregar elemento al Final
#lista.append(6)

##Insertar en la posicion 2
#lista.insert(2,"Juan")

##Concatener una lista
#lista.extend([6,7,8])
#lista3 = lista+lista2

##devuelve un valor booleano
#print(10 in lista)

##devuelve en que posision esa el elemento 8
#print(lista2.index(8))

##cuenta cutas veces se repite el numero 6
#print(lista2.count(6))

##Le pasamos el indice, Elimina un elemento de la lista, 
#print(lista2.pop(3))
#print(lista2)

##Le pasamos el valor, Elimina un elemento de la lista, 
#lista2.remove("pepe")
#print(lista2)

##Conjuntos
conjunto = set()
conjunto = {1,2,3}
conjunto2 = {3,4,5}
print(f"Conjutno1 {conjunto}")
print(f"Conjutno2 {conjunto2}")
#conjunto.add(5)
#conjunto.add("juan")
#print(conjunto)
#conjunto.discard("juan")
#print(conjunto)
##union de conjuntos
c = conjunto | conjunto2
print(f"Union de Conjunto {c}")

##intercepcion de conjuntos
c = conjunto & conjunto2
print(f"Intercepcion de Conjunto {c}")

##Diferencia de conjuntos
c = conjunto - conjunto2
print(f"Diferencia de Conjunto {c}")

##Diferencia Simetrica de conjuntos
c = conjunto ^ conjunto2
print(f"Diferencia de Conjunto {c}")