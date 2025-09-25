'''
Categoría de salario:
Un empleado recibe un salario y se clasifica así:
Menos de $1.000.000: “Bajo”.
Entre $1.000.000 y $3.000.000: “Medio”.
Entre $3.000.001 y $7.000.000: “Alto”.
Más de $7.000.000: “Directivo”.
'''

print("Categoria de salario 💰")
salario = int(input("Cuanto salrio gana(COP)(sin comas ni puntos): "))

if salario < 1000000 and salario > 0:
    print("Bajo")
elif salario >= 1000000 and salario <= 3000000:
    print("Medio")
elif salario >= 3000001 and salario < 7000000:
    print("Alto")
elif salario >= 7000000:
    print("Directivo")
else:
    print("⚠ Salario invalido ⚠")