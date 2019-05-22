''' Ejercicio 04
    Programa que pida 1 caracter y determine si es una vocal o no.
'''

n1 = int(input("Digite primer numero  -> "))
n2 = int(input("Digite segundo numero -> "))

char = input("Digite caracter (S,R,M,D) -> ").lower()

if char =='s':
    print(f"la suma es: {n1+n2} \n")
elif char =='r':
    print(f"la resta es: {n1-n2} \n")
elif char =='m':
    print(f"la muntiplicacion es: {n1*n2} \n")
elif char =='d':
    print(f"la division es: {(n1/n2):.2f} \n")
else:
        print("Tienen que ingresar caracter valido: \n")