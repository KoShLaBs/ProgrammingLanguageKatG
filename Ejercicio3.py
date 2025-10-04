'''
### **Control de calidad en línea de producción**

**Objetivo:**Inspeccionar 50 piezas.

**Entradas:**por pieza:`ok`o`def`y, si`def`, tipo:`leve`/`critico`.

**Reglas:**

- Sumar`ok`,`def leves`y`def críticos`.
- Si aparece un`def critico`,**detener**la línea inmediatamente (usa`break`).
    
    **Salida:**totales y si la línea fue detenida por defecto crítico.
'''

#Info usuario
print("Control de calidad para la producccion de Kat's")

#Inicializar variables
defectuosas = 0
danioLeve = 0
danioCritico = 0
buenEstado = 0

#Entrada, saber tipo de pieza
for pieza in range(1, 50+1):
    while True:
        piezas = input(f"La pieza {pieza} que va a ingresar si la pieza esta defestuosa (def) o si esta en buen estado (ok) ")
        if (piezas.lower() == "ok"):
            buenEstado += 1
            break
        elif (piezas.lower() == "def"):
            defectuosas +=1
            defecto = input("Ingrese leves o criticos dependiendo del tipo de defecto que tenga la pieza: ") 
            if (defecto.lower() == "leves"):
                danioLeve += 1
                break
            elif (defecto.lower() == "criticos"):
                print("Proceso detenido por defecto critico")
                danioCritico += 1
                break
            else:
                print("Ingrese información valida")
                continue
        else:
            print("Ingrese un dato valido")
            continue

#Calculo
sumaTotalPiezas = buenEstado + defectuosas

#Salida de información
print("---Informe de calidad de las piezas---")
print(f"Total de piezas: {sumaTotalPiezas}\nPiezas en buen estado: {buenEstado} \nPiezas defectuosas: {defectuosas} \nPiezas con daño leve: {danioLeve} \nPiezas con daño critico y eventualmente detenido por su defecto: {danioCritico}")