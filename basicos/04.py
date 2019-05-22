''' Ejercicio 04
    Hacer un programa para ingresar el radio de un circulo 
    y se reporte su area y longitud de la circunferencia..
'''
import math

r = float(input("radio -> "))
area = math.pi * r**2
longitud = 2 * math.pi * r
print(f"El area es: {area:.2f}")
print(f"La longitud es: {longitud:.2f}")