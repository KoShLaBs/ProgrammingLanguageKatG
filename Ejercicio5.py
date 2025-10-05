'''
### **Promedio de calificaciones con aprobación**

**Objetivo:**Leer 5 notas (0 a 5), validar y promediar.

**Entradas:**5 notas (usar`for`) con validación en`while`hasta que estén en`[0,5]`.

**Reglas de aprobación:**aprueba si`prom >= 3.0`**y****ninguna**nota`< 2.0`.

**Salida:**promedio (2 decimales) y estado:`Aprobado`/`Requiere refuerzo`.
'''

#Info usuario
print("Kat at college")
print("Promedio de notas\n")

#Inicializacion de variables
promedio = 0.0
sumaNotas = 0.0
validacionNota = 0

#Validación notas >0 and <=5
for nota in range(1, 5+1):
    while True:
        try:
            notas = float(input(f"Dame la nota {nota} (entre 0 y 5, separados por punto de ser necesario): "))
            if (notas < 0 or notas > 5):
                print("Recuerde que debe ser entre 0(cero) y 5(cinco)")
                continue
            pass
        except Exception as e:
            print("Ingrese un numero valido")
            raise e
        if (notas >= 2.0):
            validacionNota += 1
        else:
            validacionNota +=0
            pass
        sumaNotas += notas
        break
        
#Calculo promedio
promedio = sumaNotas / 5

#Salida
if (promedio >= 3.0 and validacionNota == 5):
    print(f"Resultado----\nPromedio: {promedio:.2f}\nEstado: Aprobado")
elif (promedio >= 3.0 and validacionNota != 5):
    print(f"Resultado----\nPromedio: {promedio:.2f}\nEstado: Requiere refuerzo debido a que tiene alguna por debajo de dos(2)")
else:
    print(f"Resultado----\nPromedio: {promedio:.2f}\nEstado: Requiere refuerzo")