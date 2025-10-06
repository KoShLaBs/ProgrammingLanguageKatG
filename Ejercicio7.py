'''
### **Descuentos en tienda (membresía + cupón)**

**Objetivo:**Calcular el total de una compra con reglas comerciales.

**Entradas:**precio base, ¿membresía? (`s/n`), ¿cupón? (`s/n`), ¿producto en oferta? (`s/n`).

**Reglas:**

- Membresía aplica 10%. - compra total
- Cupón aplica 15%**solo si**el producto**no**está en oferta. - producto
- **No**se pueden combinar cupón**y**oferta (si ambos`s`, solo oferta).
- Si precio final > 300000**y**es miembro, aplicar envío gratis. - total comopra
    
    **Salida:**total final y si incluye envío gratis.
'''
#------Adicional: Agregue menu para mejor entendimiento del programa

#Inicializar variables
totalCompra = 0
producto = 0
descuento = 0
cantidadProductos = 0

print("🛒 Tiendas Kat 🛒")
do = True

while do:
    try:
        membresia = input("👤 Ingresar 's' si el cliente cuenta con membresía o 'n' si no la tiene: ").lower()
        if (membresia != "s" and membresia != "n"):
            print("⚠️ Error de digitacion, eliga alguna de las opciones")
            continue
        pass
    except Exception as e:
        print("❌ Valor erroneo")
        raise e
    print("✅ Gracias por el dato")
    do = False

do = True
#Menu, agregar prodcutos
while do:
    #Menu
    print("\n1️⃣) Agregar producto\n2️⃣) Total compra\n3️⃣) Salir\n")
    #match case 
    try:
        opcion = int(input("👉 Elige una opción: "))
        if opcion not in [1,2,3,4]:
            print("⚠️ Ingrese un número válido, rango de 1(uno) a 3(tres)\n")
            continue
        pass
    except Exception as e:
        print("❌ Error en la entrada, inténtalo de nuevo.")
        raise e
    match opcion:
        case 1:
            #Validaciones
            validar = True
            while validar:
                try:
                    compra = float(input("💰 Ingrese valor producto: "))
                    if (compra < 0):
                        print("⚠️ Ingresar número mayor a cero")
                        continue
                    pass
                except Exception as e:
                    print("❌ Número invalido")
                    raise e
                validar = False
            #Cupon y oferta
            validar = True
            while validar:     
                try:
                    cupon = input("🎟️ Ingresar 's' si cuenta con cupon o 'n' si no tiene: ").lower()
                    if (cupon != 's' and cupon != 'n'):
                        print("⚠️ Error de digitacion, eliga alguna de las opciones")
                        continue
                    pass
                except Exception as e:
                    print("❌ Valor erroneo")
                    raise e
                validar = False
            #Oferta
            valiordar = True
            while valiordar:
                try:
                    oferta = input("🏷️ Ingresar 's' si cuenta con oferta o 'n' si no tiene: ").lower()
                    if (oferta != 's' and oferta != 'n'):
                        print("⚠️ Error de digitacion, eliga alguna de las opciones")
                        continue
                    if(oferta == 's'):
                        validarDos = True
                        while validarDos:
                            try:
                                valorOferta = int(input("📉 Ingresar valor de la oferta, solo el número del porcentaje: "))
                                if (valorOferta <= 0 and valorOferta > 100):
                                    print("⚠️ Ingresar número entre 1 y 100")
                                    continue
                                pass
                            except Exception as e:
                                print("❌ Número invalido")
                                raise e
                            validarDos = False
                    pass
                    pass
                except Exception as e:
                    print("❌ Valor erroneo")
                    raise e
                valiordar = False
            
            #calculos
            if (oferta == 's' and cupon == 's'):
                descuento = (compra * valorOferta) / 100
            elif (oferta == 'n' and cupon == 's'):
                descuento = (compra * 15) / 100
            elif (oferta == 's' and cupon == 'n'):
                descuento = (compra * valorOferta) / 100
            else:
                descuento = 0
            producto = compra - descuento
            totalCompra += producto
            cantidadProductos += 1
            print(f"✅ Producto agregado. Total actual: {totalCompra:.0f} 🛍️")
        case 2:
            if (cantidadProductos == 0):
                print("⚠️ No se han agregado productos")
                continue
            if (totalCompra > 300000 and membresia == 's'):
                print(f"🧾 Total compra: {totalCompra:.0f}, con un total de {cantidadProductos} productos, incluye 🚚 envío gratis")
            elif (membresia == 'n'):
                totalCompra += (totalCompra * 10) / 100
                print(f"🧾 Total compra: {totalCompra:.0f}, con un total de {cantidadProductos} productos, no incluye 🚚 envío gratis")
            else:
                print(f"🧾 Total compra: {totalCompra:.0f}, con un total de {cantidadProductos} productos, no incluye 🚚 envío gratis")
            print("Gracias por su compra, vuelva pronto 😊")
            do = False
        case 3:
            do = False



    