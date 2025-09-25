#Descripción del ejercicio
'''
Descuento por membresía de gimnasio:
Según el tipo de membresía:
Básica: $80.000.
Premium: $120.000.
VIP: $200.000.
Además, si el cliente es estudiante, se aplica 10% de descuento adicional.
'''

#Información para usuario
print("GYM Kat")

#Información pedida param saber quer membresia desea adquirir
membresia = input("Digame el tipo de membresia que quiere (Basica, premium, VIP): ")

#Variable vacia para calcular el total
membresiaTotal = 0

#Condicional con .lower() que permite transformar la variable y comparar 
if membresia.lower() == "basica":
    #Pedir información de si es o no un estudiante
    estudiante = input("¿es usted estudiante? (si o no): ")
    #Otro condicional que permite saber si es o no estudiante y si aplica o descuento o no
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $80.000.")
    elif estudiante.lower() == "si":
        membresiaTotal = 80000 - 80000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $80.000.")
elif membresia.lower() == "premium":
    #Pedir información de si es o no un estudiante
    estudiante = input("¿es usted estudiante? (si o no): ")
    #Otro condicional que permite saber si es o no estudiante y si aplica o descuento o no
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $120.000")
    elif estudiante.lower() == "si":
        membresiaTotal = 120000 - 120000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $120.000")
elif membresia.lower() == "vip":
    #Pedir información de si es o no un estudiante
    estudiante = input("¿es usted estudiante? (si o no): ")
    #Otro condicional que permite saber si es o no estudiante y si aplica o descuento o no
    if estudiante.lower() == "no":
        print(f"Su membresia {membresia} le sale por un valor de: $200.000.")
    elif estudiante.lower() == "si":
        membresiaTotal = 200000 - 200000 * 0.10
        print(f"Su membresia {membresia} le sale por un valor de: ${membresiaTotal:.0f}")
    else:
        print(f"No fuiste especifico si estudias o no, por eso su membresia {membresia} le sale por un valor de: $200.000.")
else:
    print("Membresia invalida")