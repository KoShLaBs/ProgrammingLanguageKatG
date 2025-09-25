'''
Costo de envío por peso:
Una empresa cobra según el peso del paquete:
Menos de 2 kg: $10.000.
De 2 a 5 kg: $20.000.
De 6 a 10 kg: $30.000.
Más de 10 kg: $50.000.
'''

print("InterKatidisimo")
peso = float(input("¿Cuanto pesa el paquete que va a enviar?: "))

if peso < 2 and peso > 0:
    print("El envio te sale por $10.000.")
elif peso >= 2 and peso < 6:
    print("El envio te sale por $20.000.")
elif peso >= 6 and peso <= 10:
    print("El envio te sale por $30.000.")
elif peso > 10:
    print("El envio te sale por $50.000.")
else:
    print("Peso invalido")