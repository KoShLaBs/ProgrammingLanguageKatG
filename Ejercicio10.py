'''
### **Turnero de banco con saltos**

**Objetivo:** Emitir turnos del 1 al `N`, omitiendo números “no servibles”.

**Entradas:** `N` y regla: **saltar** turnos múltiplos de 13 **o** que terminen en 4 (usa `continue`).

**Reglas:**

- Mostrar cada turno válido.
- Si el contador llega a un turno “de cierre” (por ejemplo, 100) **o** si se han emitido 50 turnos válidos, detener (`break`).
    
    **Salida:** listado de turnos servidos y cuántos fueron omitidos.
'''

#Info Usuario
print("Turnero Kat🏦")  

#Inicializar variables
turnos = 0
omitidos = 0    
validos = 0
turnoCierre = 100   

#Validar N
validar = True
while validar:
    try:
        turno = int(input("Ingrese el número máximo de turnos a emitir: "))
        if (turno <= 0):
            print("Ingresar número mayor a cero")
            continue
        pass
    except Exception as e:
        print("Número invalido")
        raise e
    validar = False
    pass
    pass
#Ciclo para N turnos
for turnos in range(1, turno +1):
    #Condición multiplos o terminados en 4
    if (turnos % 13 == 0 or str(turnos).endswith('4')):
        omitidos += 1
        continue
    #Mostrar turno válido
    print(f"Turno: {turnos}")
    validos += 1
    
    #Condición de cierre
    if (turnos == turnoCierre or validos == 50):
        break
    pass

#Salida
print(f"\nSe emitieron {validos} turnos válidos y se omitieron {omitidos} turnos")  

