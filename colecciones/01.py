''' Colecciones: Ejercicio 01
    Programa que tenga una lista, y a continuacion elimine los elementos repetidos
'''
lista = [1,2,3,4,5,"juan",1,2,"juan"]

print(f"\nLista inicial: {lista} \n")
lista = list(set(lista))
print(f"Lista Final sin Repetidos: {lista} \n")