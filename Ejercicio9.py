#Descripción del ejercicio
'''
Clasificación de IMC:
Pedir peso y estatura de una persona y calcular el Índice de Masa Corporal (IMC = peso / estatura²). Según el IMC:
Menor a 18.5: Bajo peso.
Entre 18.5 y 24.9: Normal.
Entre 25 y 29.9: Sobrepeso.
30 o más: Obesidad.
'''

#Información para usuario
print("MediKat 🩺")
print("Clasificación de IMC (Índice de Masa Corporal)")

#Información pedida al usuario
peso = float(input("Deme su peso: "))
estatura = float(input("Deme su estatura (separado por punto): "))

#Calculo del imc de acuerdo a formula
imc = peso / estatura ** 2

#Condicional para presentar la información por pantalla de acuerdo al resultado del IMC
if imc < 18.5 and imc > 0:
    print(f"Tu IMC es de: {imc:.0f}. Es decir, Bajo de peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Tu IMC es de: {imc:.0f}. Es decir, Normal")
elif imc >= 25 and imc <= 29.9:
    print(f"Tu IMC es de: {imc:.0f}. Es decir, Sobrepeso")
elif imc >= 30:
    print(f"Tu IMC es de: {imc:.0f}. Es decir, Obesidad")
else:
    print("⚠ Peso o estatura invalida ⚠")