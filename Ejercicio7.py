'''
Costo de entrada a un cine:
Según la edad del cliente, el precio es:
Menores de 5 años: no pueden entrar.
5 a 12 años: $10.000.
13 a 17 años: $15.000.
18 a 59 años: $20.000.
60 o más: $12.000.
'''

print("Bienvenidos a CineKat")
edad = int(input("Digite la edad de quien va a ingresar: "))

if edad < 5 and edad > 0:
    print("¡Este bebé no puede ingresar!")
elif edad >= 5 and edad <= 12:
    print("El valor es de $10.000.")
elif edad >= 13 and edad <= 17:
    print("El valor es de $15.000.")
elif edad >= 18 and edad <= 59:
    print("El valor es de $20.000.")
elif edad >= 60:
    print("El valor es de $12.000.")
else:
    print("Edad invalida")