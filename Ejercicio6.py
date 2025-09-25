#Descripción del ejercicio
'''
Categoría de edad:
Pedir la edad de una persona y clasificarla:
Menor de 12: Niño.
12 a 17: Adolescente.
18 a 29: Joven.
30 a 59: Adulto.
60 o más: Adulto mayor.
'''

#Información para usuario
print("Clasificación de edad 🔢")
edad = int(input("Digite su edad: "))

#Condicional para saber que categoria cumple la edad digitada por usuario
if edad < 12 and edad > 0:
    print("Usted es un niño 🧒🏻👧🏻👶🏻")
elif edad >= 12 and edad <= 17:
    print("Usted es un adolescente 🧑🏻👧🏻") 
elif edad >= 18 and edad <= 29:
    print("Usted es un joven 👨🏻👩🏻") 
elif edad >= 30 and edad <= 59:
    print("Usted es un adulto 👨🏻👩🏻") 
elif edad >= 60:
    print("Usted es un adulo mayor 👵🏻👴🏻") 
else:
    print("⚠ edad invalida ⚠")