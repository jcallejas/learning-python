''' Ejercicio 03
    Programa que pida 1 caracter y determine si es una vocal o no.
'''

char = input("Digite caracter -> ").lower()

if char in ('a','e','i','o','u'):
    print(f"{char} es una vocal\n")
else:
    print(f"{char} no es una vocal\n")