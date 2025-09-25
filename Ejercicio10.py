'''
Descuento por membresía de gimnasio:
Según el tipo de membresía:
Básica: $80.000.
Premium: $120.000.
VIP: $200.000.
Además, si el cliente es estudiante, se aplica 10% de descuento adicional.
'''
print("GYM Kat")
membresia = input("Digame el tipo de membresia que quiere (Basica, premium, VIP): ")
membresiaTotal = 0

if membresia.lower() == "basica":
    estudiante = input("¿es usted estudiante? (si o no): ")
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $80.000.")
    elif estudiante.lower() == "si":
        membresiaTotal = 80000 - 80000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $80.000.")
elif membresia.lower() == "premium":
    estudiante = input("¿es usted estudiante? (si o no): ")
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $120.000")
    elif estudiante.lower() == "si":
        membresiaTotal = 120000 - 120000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $120.000")
elif membresia.lower() == "vip":
    estudiante = input("¿es usted estudiante? (si o no): ")
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $200.000.")
    elif estudiante.lower() == "si":
        membresiaTotal = 200000 - 200000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $200.000.")
else:
    print("Membresia invalida")