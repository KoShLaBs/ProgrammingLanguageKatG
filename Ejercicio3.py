'''
Promoción en supermercado:
Un supermercado aplica descuentos según el valor de la compra:
Menor a $50.000: sin descuento.
Entre $50.000 y $100.000: 5%.
Entre $100.001 y $200.000: 10%.
Mayor a $200.000: 20%.
Mostrar el valor final con descuento aplicado.
'''

aux = 0

print("Bienvenidos al supermercado Kat")
totalCompra = int(input("Valor total de su compra (sin comas ni puntos): "))

if totalCompra <= 50000 and totalCompra > 0:
    print(f"Valor a pagar: {totalCompra:.0f}. Muchas gracias por su compra, que tenga buen día.")
elif totalCompra > 50000 and totalCompra <= 100000:
    aux = totalCompra - (totalCompra * 0.05)
    print(f"Valor a pagar: {aux:.0f}. Muchas gracias por su compra, que tenga buen día ")
elif totalCompra > 100001 and totalCompra <= 200000:
    aux = totalCompra - (totalCompra * 0.10)
    print(f"Valor a pagar: {aux:.0f}. Muchas gracias por su compra, que tenga buen día ")
elif totalCompra > 200000 :
    aux = totalCompra - (totalCompra * 0.20)
    print(f"Valor a pagar: {aux:.0f}. Muchas gracias por su compra, que tenga buen día ")
else:
    print("Numero invalido")