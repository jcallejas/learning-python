''' Ejercicio 05
    Una tienda ofrece un descuento del 15 % sobre el total de la compra,
    y un cliente desea saber cuanto deberia pagar por su compra
'''

precio = float(input("Digite el precio -> "))
descuento = precio * 0.15

print(f"El monto a pagar es: {precio-descuento:.2f}")