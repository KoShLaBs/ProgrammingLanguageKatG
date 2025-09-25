'''
Impuesto de vehículos:
Calcular el impuesto a pagar por un vehículo según su valor:
Menor a $20.000.000: no paga impuesto.
Entre $20.000.000 y $50.000.000: 5% del valor.
Entre $50.000.001 y $100.000.000: 10%.
Mayor a $100.000.000: 15%.
'''

print("Bienvenido al gobierno Kat, vamos a ver cuanto toca pagar este año por el impuesto vehicular 🚗🚙🛵")

valor = int(input("Digite el valor de su vehiculo (sin puntos ni comas): "))
aux = 0

if valor < 20000000 and valor > 0:
    print("No se preocupe, no debe pagar impuestos por ese vehiculo")
elif valor >= 20000000 and valor <= 50000000:
    aux = valor * 0.05
    print(f"Usted debe pagar {aux:.0f} en impuesto por su vehiculo 💰")
elif valor > 50000001 and valor < 100000000:
    aux = valor * 0.10
    print(f"Usted debe pagar {aux:.0f} en impuesto por su vehiculo 💰")
elif valor >= 100000000:
    aux = valor * 0.15
    print(f"Usted debe pagar {aux:.0f} en impuesto por su vehiculo 💰")
else:
    print("⚠ Numero invalido ⚠")