'''
### **Estacionamiento por horas**

**Objetivo:**Calcular cobro por vehículo hasta escribir`fin`.

**Entradas:**horas estacionadas (float) y tipo:`oficial`/`discap`/`normal`.

**Reglas:**

- Si`discap`**o**(`oficial`**y**horas`<= 0.5`) →**gratis**.
- Si`normal`: tarifa base $3000/h. Si horas > 8**o**fin de semana (`s/n`), aplicar tope $20000.
- Validar horas > 0.
    
    **Salida:**cobrar cada ticket, acumulado del día y cuántos fueron gratuitos.
'''

#Info usuario
print("Bienvenido al estacionamiento KatPark")

#Variables inicializadas
horasEstacionadas = 0.0
tarifaDia = 0.0
totalGratuitos = 0
acumuladoDia = 0.0

#Ciclo para ingresar datos
while True:
    tipoVehiculo = input("Ingrese tipo de vehiculo: 'oficial', 'discap', 'normal' o 'fin' para terminar: ").lower()
    if tipoVehiculo == "fin":
        break
    if tipoVehiculo not in ["oficial", "discap", "normal"]:
        print("Tipo de vehiculo no valido. Intente de nuevo. (asegurese de no agregar espacios)")
        continue
    try:
        horasEstacionadas = float(input("Ingrese las horas estacionadas (número mayor a 0 separado por coma de ser necesario): "))
        if horasEstacionadas <= 0:
            print("Ingrese un numero mayor a 0")
            continue
    except Exception as e:
        print("Ingrese un numero valido")
        raise e
    if tipoVehiculo == "discap" or (tipoVehiculo == "oficial" and horasEstacionadas <= 0.5):
        tarifaDia = 0.0
        totalGratuitos += 1
        print(f"\nEl cobro por el ticket es: ${tarifaDia:.0f} (gratuito)\n")
    elif tipoVehiculo == "normal":
        tarifaDia = horasEstacionadas * 3000
        if horasEstacionadas > 8:
            tarifaDia = min(tarifaDia, 20000)
        else:
            diaSemana = input("Es fin de semana? 's' (si) 'n' (no): ").lower()
            if diaSemana == 's':
                tarifaDia = min(tarifaDia, 20000)
        print(f"\nEl cobro por el ticket es: ${tarifaDia:.0f}\n")
        #Agregar adicional oficial para evitar error si hay "oficial" mayor a 0.5 horas <si oficial no es menor o igual a 0.5 horas, entonces hacer calculo normal mas tope de 20000>
    elif tipoVehiculo == "oficial":
        tarifaDia = horasEstacionadas * 3000
        if horasEstacionadas > 8:
            tarifaDia = min(tarifaDia, 20000)
        print(f"\nEl cobro por el ticket es: ${tarifaDia:.0f}\n")
    acumuladoDia += tarifaDia
    
#Salida de información
print(f"\n---Informe del dia en KatPark---\nTotal acumulado del día: ${acumuladoDia:.0f}\nTotal de vehiculos con tarifa gratuita: {totalGratuitos}")


