'''
### **Pase de lista de empleados (turno)**

**Objetivo:**Contar asistencia d`Nempleados.

**Entradas:**número`N`y, por cada empleado,`p`(presente),`t`(tarde),`a`(ausente).

**Reglas:**

- Un empleado “cumple” si está`presente`**o**(`tarde`**y**con justificación`s/n`=`s`).
- Usa`for`para iterar`1..N`.
    
    **Salida:**presentes, tardes, ausentes, y cuántos “cumplen”. Si`cumplen/N >= 0.9`, mostrar “Turno óptimo”.
'''

#Info usuario
print("---Pasando lista en el cuartel kat de los empleados---")
print("Registre la asistencia del turno")

#Definir variables
totalEmpleados = 0
empleadosPresentes = 0
empleadosTarde = 0
empleadosAusentes = 0
empleadosCumplen = 0
empleadosNoCumplen = 0

#Entrada numero de empleados
while True:
    try:
        totalEmpleados = int(input("Ingrese el numero de empleados en el turno: "))
        if totalEmpleados > 0:
            break
        else:
            print("Ingresar un numero mayor a 0")
            continue
    except Exception as e:
        print("Ingresar un numero valido!")
        raise e
    pass

#Condicional validar datos
for empleado in range(1, totalEmpleados + 1):
    while True:
        asistencia = input(f"\nEmpleado {empleado}: Ingrese 'p' (presente), 't' (tarde) o 'a' (ausente): ").lower()
        if asistencia == 'p':
            empleadosPresentes += 1
            empleadosCumplen += 1
            break
        elif asistencia == 't':
            justificacion = input("Tiene justificación? Ingrese 's' (si) 'n' (no): ").lower()
            empleadosTarde += 1
            if justificacion == 's':
                empleadosCumplen += 1
            else:
                empleadosNoCumplen += 1
            break
        elif asistencia == 'a':
            empleadosAusentes += 1
            empleadosNoCumplen += 1
            break
        else:
            print("Entrada inválida. Por favor, ingrese 'p', 't' o 'a'.")
            continue
        pass
    pass

#Calculo adicional de promedio
promedioDia = empleadosCumplen / totalEmpleados
if promedioDia >= 0.9:
    turnoOptimo = "Turno óptimo"
else:
    turnoOptimo = "Turno no óptimo"
    pass

#Imprimir datos
print("\nFinal del turno-----")
print(f"Empleados presentes: {empleadosPresentes}\n Empleados tarde: {empleadosTarde}\nEmpleados ausentes: {empleadosAusentes}\nEmpleados que cumplen: {empleadosCumplen}\nEmpleados que no cumplen: {empleadosNoCumplen}")
print(f"{turnoOptimo} con un promedio de: {promedioDia:.2f}")



