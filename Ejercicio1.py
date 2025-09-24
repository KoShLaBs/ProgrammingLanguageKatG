'''
Tarifa de agua por estrato:
El gobierno cobra tarifas de agua diferentes según el estrato:
Estrato 1: $20.000
Estrato 2: $40.000
Estrato 3: $60.000
Estrato 4: $80.000
Estrato 5: $100.000
Estrato 6: $120.000
Pedir el estrato y mostrar cuánto debe pagar un usuario.
'''

print("Bienvenido al gobierno Kat, vamos a ver cuanto toca pagar este mes por el servicio del agua")
estrato = int(input("Dame el estrato en el que resides del uno(1) al seis(6): "))

if estrato == 1:
    print(f"Siendo del estrato {estrato} toca pagar $20.000 por el servicio del agua")
elif estrato == 2:
    print(f"Siendo del estrato {estrato} toca pagar $40.000 por el servicio del agua")
elif estrato == 3:
    print(f"Siendo del estrato {estrato} toca pagar $60.000 por el servicio del agua")
elif estrato == 4:
    print(f"Siendo del estrato {estrato} toca pagar $80.000 por el servicio del agua")
elif estrato == 5:
    print(f"Siendo del estrato {estrato} toca pagar $100.000 por el servicio del agua")
elif estrato == 6:
    print(f"Siendo del estrato {estrato} toca pagar $120.000 por el servicio del agua")
else:
    print("estrato invalido")