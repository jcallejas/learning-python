''' Ejercicio 02
    Programa que pida 3 numeros y determine cual de ellos es el mayor.
'''

num1 = int(input("Digite el primer numero -> "))
num2 = int(input("Digite el segundo numero -> "))
num3 = int(input("Digite el tercer numero -> "))

if (num1 > num2) and (num1 > num3):
    print(f"\nEl numero: {num1} es el Mayor\n")
elif (num2 > num1) and (num2 > num3):
    print(f"\nEl numero: {num2} es el Mayor\n")
elif (num3 > num1) and (num3 > num2):
    print(f"\nEl numero: {num3} es el Mayor\n")