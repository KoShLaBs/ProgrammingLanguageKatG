'''
### **Entregas de paquetería por franja horaria**

**Objetivo:** Registrar hasta 10 entregas o hasta que se escriba `fin`.

**Entradas:** por entrega: hora prometida (entero 0–23), hora real (0–23).

**Reglas:**

- “A tiempo” si `hora_real <= hora_prometida` **o** (hora real ≤ prometida + 1 **y** cliente VIP `s/n` = `s`).
- Si se completan 10 entregas **o** son las 20:00 (hora del sistema ingresada) y faltan 2 repartos **y** no hay tiempo, terminar con `break`.
    
    **Salida:** entregas a tiempo, tardías y tasa de cumplimiento.
'''

#Info Usuario
print("Entregas Kat📦")

#Inicializar varibles
aTiempo = 0
tarde = 0
tasa = 0.0
entregas = 0

do = True
while do:
    print("1) Registrar entrega\nEscribir 'fin' para acabar")
    #Validar
    validar = True
    do = validar
    try:
        opcion = input("Dame una opcion").lower()
        if opcion not in ["1","fin"]:
            print("Ingrese un dato válido, uno(1) o 'fin'\n")
            continue
        pass
    except Exception as e:
        print("Error en la entrada, inténtalo de nuevo.")
        raise e
    validar = False
    
    
    #Menu    
    match opcion:
        case "1":
            entregas += 1
            validar = True
            #Validar VIP
            do = validar
            try:
                vip = input("Digitar 's' si es usuario VIP o 'n' si no lo es: ").lower()
                if vip not in ["s","n"]:
                    print("Ingrese un dato válido, 's' o 'n'\n")
                    continue
                pass
            except Exception as e:
                print("Error en la entrada, inténtalo de nuevo.")
                raise e
            validar = False
            
            validar = True
            print(f"Entrega {entregas}")
            #Hora prometida
            do = validar
            try:
                prometido = int(input("Digite la hora prometida (0-23): "))
                if prometido < 0 and prometido > 23:
                    print("Error en el valor ingresado")
                    continue
                pass
            except Exception as e:
                print("Dato invalido")
                raise e
            validar = False
            
            #Hora actual
            validar = True
            do = validar
            try:
                actual = int(input("Digite la hora actual (0-23): "))
                if actual < 0 and actual > 23:
                    print("Error en el valor ingresado")
                    continue
                pass
            except Exception as e:
                print("Dato invalido")
                raise e
            validar = False
            
            #Validar a tiempo o retraso 
            if (actual <= prometido or (actual <= prometido + 1 and vip == 's')):
                print("Entrega a tiempo\n")
                aTiempo += 1
            else:
                print("Entrega con retraso\n")
                tarde += 1
            
            #Validar si se puede seguir entregando
            if (entregas == 10):
                print("Se han completado las 10 entregas")
                do = False
            elif (actual == 20 and (10 - entregas) >= 2):
                print("No hay tiempo para completar las entregas restantes")
                do = False
            
        case "fin":
            do = False

#Calcular tasa de cumplimiento
if (entregas > 0):
    tasa = (aTiempo / entregas) * 100
    
#Salida
print(f"\nEntregas a tiempo: {aTiempo}\nEntregas con retraso: {tarde}\nTasa de cumplimiento: {tasa:.2f}%")