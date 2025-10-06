'''### **Cajero automático con PIN y menú**

**Objetivo:**Simular operaciones básicas con intentos de PIN.

**Entradas:**PIN correcto predefinido; el usuario tiene**3 intentos**(`while`) para acertar.

**Menú (en bucle):**1) Depositar 2) Retirar 3) Consultar 4) Salir

**Reglas:**

- Depósitos y retiros deben ser`> 0`; retiro solo si`saldo >= retiro`.
- Bloquear si falla el PIN 3 veces (terminar).
    
    **Salida:**operaciones realizadas y saldo final.
'''
#Generación de PIN predefinido
pin = "2089"

#Variables predefinidads
intentos = 0
dinero = 0
print("\nCajero automatico KatCash🤑")
# Validar PIN
while intentos < 4:
    pinIngresado = input("🔒 Digite su PIN: ")
    if (pinIngresado == pin):
        intentos = 4
        # MENU infinito hasta "salir" Una vez el PIN sea correcto
        do = True
        while do:
            # Menu
            print("\n🏦 Cajero automatico KatCash🤑")
            print("1️⃣ Depositar\n2️⃣ Retirar\n3️⃣ Consultar\n4️⃣ Salir\n")
            try:
                opcion = int(input("👉 Elige una opción: "))
                if opcion not in [1,2,3,4]:
                    print("⚠️ Ingrese un número valido, rango de 1️⃣ a 4️⃣\n")
                    continue
            except Exception as e:
                print("❌ Error en la entrada, intentalo de nuevo.")
                raise e
            match opcion:
                case 1:
                    try:
                        depositar = float(input("💰 Ingrese cuanto dinero desea depositar: "))
                        if (depositar < 0):
                            print("⚠️ Error al ingresar monto, solo números mayores a cero.\n")
                            continue
                    except Exception as e:
                        print("❌ Monto invalido")
                        raise e
                    print("✅ Dinero agregado exitosamente 🤑")
                    dinero += depositar
                case 2:
                    try:
                        retirar = float(input("💸 Ingrese cuanto dinero desea retirar: "))
                        if (retirar < 0):
                            print("⚠️ Error al ingresar monto, solo números mayores a cero.\n")
                            continue
                        elif (retirar > dinero or dinero < retirar):
                            print("🚫 Saldo insuficiente.\n")
                            continue
                    except Exception as e:
                        print("❌ Monto invalido")
                        raise e
                    print("✅ Dinero retirado exitosamente, tomelo de la cajita ")
                    dinero -= retirar
                case 3:
                    print(f"💳 Su saldo es {dinero:.0f} 🤑")
                case 4:
                    print("👋 Gracias por usar KatCash! Hasta luego.")
                    do = False
    else:
        intentos += 1
        print("❌ PIN inválido")
    if (intentos == 3):
        print("🔒 CUENTA BLOQUEADA POR INTENTOS FALLIDOS 🚫")
        break
    elif (intentos == 4):
        break
