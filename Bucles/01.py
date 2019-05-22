'''Bubles: Ejercicio 01
    Programa que determine la raiz cuadrada de un numero
'''
import math
n = int(input("Digite un Numero -> "))
while ( n < 0):
    print("Ingrese Numero Positivo")
    n = int(input("Digite un Numero -> "))
print(f"\nLa Rais Cuadrada es:{math.sqrt(n):.2f}")