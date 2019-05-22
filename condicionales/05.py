''' Ejercicio 05
    Programa que simule a un cajero automatico, con un saldo unicial 
    de Bs.100.-, y tendra el siguiente menu de opciones
    
    1. Ingrese dinero en la Cta.
    2. Retire dinero de la Cta.
    3. Mostrar dinero disponible.
    4. Salir
'''
saldo = 100

print("\t.:MENU:.")
print("Digite 1 Para Ingresar Dinero.")
print("Digite 2 Para Retirar Dinero.")
print("Digite 3 Para Mostrar Disponible.")
print("Digite 4 Para Salir")

opt = int(input("Digite Opcion -> "))

if opt == 1:
    extra = int(input("Digite Monto-> "))
    print(f"Su saldo actual es: {saldo+extra} \n")
elif opt == 2:
    retiro = int(input("Digite Monto-> "))
    print(f"Su saldo actual es: {saldo-retiro} \n")
elif opt == 3:    
    print(f"Su saldo disponible: {saldo} \n")
elif opt == 4:    
    print("Gracias por utilizar nuestros servicios\n")
else:
    print("Digite una opcion Validad\n")