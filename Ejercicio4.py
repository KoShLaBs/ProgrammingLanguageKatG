'''
Nota final de un estudiante:
Según la nota obtenida (0 a 100):
90 a 100: “Excelente”.
70 a 89: “Aprobado”.
50 a 69: “Habilita examen”.
Menor a 50: “Reprobado”.
'''

print("Escuela Kat")
print("Califiquemos la nota final de la materia de lenguaje de programación")

notaFinal = float(input("Nota final del estudiante de cero(0) a cien(100): "))

if notaFinal <= 100 and notaFinal >= 90:
    print("¡Excelente!✨")
elif notaFinal <= 89 and notaFinal >= 70:
    print("Aprobado 😊")
elif notaFinal <= 69 and notaFinal >= 50:
    print("Habilita examen 😖")
elif notaFinal <= 50 and notaFinal >= 0:
    print("Reprobado 😔")
else:
    print("⚠ Nota no valida ⚠")
