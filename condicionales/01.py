''' Ejercicio 01
    Programa que pida 2 numeros y determine cual de ellos es par, o ambos lo son.
'''

num1 = int(input("Digite el primer numero -> "))
num2 = int(input("Digite el segundo numero -> "))

if (num1%2 == 0) and (num2%2 == 0):
    print(f"El numero: {num1} y el numero: {num2} son pares")
elif (num1%2 == 0) and (num2%2 != 0):
    print(f"El numero: {num1} es par")
    print(f"El numero: {num2} es impar")
elif (num1%2 != 0) and (num2%2 == 0):
    print(f"El numero: {num2} es par")
    print(f"El numero: {num1} es impar")
else:
    print(f"El numero: {num1} y el numero: {num2} son impares")