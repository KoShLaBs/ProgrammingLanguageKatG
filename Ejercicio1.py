'''
**1) Caja del día - ventas hasta “cerrar”**

**Objetivo:** Registrar ventas hasta que el cajero escriba `cerrar`.

**Entradas:**montos de venta uno a uno.

**Reglas:**

- Solo aceptar montos`> 0`y`<= 1_000_000`(si no, ignorar con`continue`).
- Parar con la palabra`cerrar`(usa`while True`+`break`).
- Meta diaria: `>= 500000` **y** al menos `5` transacciones.
    
    **Salida:** total del día, número de ventas, ticket promedio y mensaje: “Meta cumplida” o “Meta no cumplida”.
'''

#Info usuario
print("Cajero automatico KatCash")
print("Registre sus ventas del día")

#Definir variables
totalDia = 0.0
numeroVentas = 0
promedioGanancia = 0.0

#Condicional ciclo.
while True:
    data = input(f"Ingresa monto (sin comas ni puntos para montos mayor a mil) o digite 'cerrar' para parar: ")
    if data.lower() == "cerrar":
            break
    try:
        dataN = float(data)
        if dataN >= 0 and dataN <= 100000:
            totalDia += dataN
            numeroVentas += 1
        else: 
            print ("invalido")
            print("RANGO: entre 0 y 1_000_000")
            continue
    except Exception as e:
        print("Ingresar números en el rango pedido.")
        raise e
    pass

#Calcular 
promedioGanancia = totalDia / numeroVentas

#Salida
if numeroVentas >= 5 and totalDia >= 500000:
    print(f"\nMeta cumplida! \n Ganacia de {totalDia} con un promedio de {promedioGanancia:.0f} y {numeroVentas} transaciones exitosas")
else:
    if numeroVentas < 5:
        print(f"\nMeta no cumplida :c \n numero de ventas: {numeroVentas}")
        pass
    elif totalDia < 500000:
        print(f"\nMeta no cumplida :c \n total del dia: {totalDia:.0f}")
        pass
    pass

