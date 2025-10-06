'''
### **Consumo eléctrico mensual**

**Objetivo:** Leer consumo diario por 30 días y calcular factura.

**Entradas:** 30 lecturas en kWh (usa `for` y valida `>=0`).

**Tarifa:**

- Hasta 200 kWh: $600/kWh
- 201–500: $700/kWh
- 500: $850/kWh**Extra:** contar días “alto consumo” (`> 25 kWh`) y si `total > 600` **y** `dias_altos >= 5`, recomendar “Auditoría de consumo”.**Salida:** total kWh, costo final y advertencias.
'''

#Info Usuario
print("Consumo EnergiKat⚡")

#Inicializar variables
totalKwh = 0
costoFinal = 0
diasAltos = 0

#Ciclo para 30 días
for dias in range(1,30+1):
    #Validar consumo
    validar = True
    while validar:
        try:
            consumo = float(input(f"🔢 Ingrese consumo del día {dias} en kWh: "))
            if (consumo < 0):
                print("⚠️ Ingresar número mayor a cero")
                continue
            pass
        except Exception as e:
            print("❌ Número invalido")
            raise e
        validar = False
        
        #Calcular dias alto consumo
        if (consumo > 25):
            diasAltos += 1
        
        #Sumar consumo total
        totalKwh += consumo
        
    pass


#Calcular costo final
if (totalKwh <= 200):
    costoFinal = totalKwh * 600
elif (totalKwh >= 201 and totalKwh <= 500):
    costoFinal = totalKwh * 700
elif (totalKwh > 500):
    costoFinal = totalKwh * 850

#Salida
print(f"\n⚡ Su consumo total fue de {totalKwh:.2f}kWh, con un costo final de ${costoFinal:.0f} 💸")
if (totalKwh > 600 and diasAltos >= 5):
    print(f"🚨 Se recomienda realizar una Auditoría de consumo debido a que tuvo {diasAltos} dias de alto consumo 🔍")