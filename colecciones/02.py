''' Colecciones: Ejercicio 02
    Programa que tenga 2 lista, y a continuacion cree las 
    siguiente listas (en las que no tiene que haber repetidos):

    -Lista de elementos que aparecen en las 2 listas
    -Lista de elementos que aparecen en la primera lista, pero no en la segunda
    -Lista de elementos que aparecen en la segunda lista, pero no en la primera
    -Lista de elementos que aparecen en ambas listas
'''
l1 = [1,2,3,4,5,4,3,2,2,1,5]
l2 = [4,5,6,7,8,4,5,6,7,7,8]

print(f"\nLista1:{l1}\nLista2:{l2}")
l1 = set(l1)
l2 = set(l2)
print(f"\nSin Repetidos:\nLista1:{l1}\nLista2:{l2}")
print(f"\nElementos en ambas listas: {list(l1|l2)}")
print(f"Elementos en la Primera lista: {list(l1-l2)}")
print(f"Elementos en la Segunda lista: {list(l2-l1)}")
print(f"Elementos en ambas lista: {list(l1&l2)}")
