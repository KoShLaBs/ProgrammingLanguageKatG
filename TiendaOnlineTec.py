productos = ["laptop", "mouse", "teclado", "audifonos","monitor"]
precios = [2500, 50, 120, 80, 300]

carrito = []

def mostratProductos():
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - ${precios[i]}")

def agregarAlCarrito():
    mostratProductos()
    opcion = int(input("Seleccione el número del producto que desea agregar al carrito: ")) - 1
    if opcion >= 0 and opcion < len(productos):
        carrito.append(precios[opcion])
        print(f"{productos[opcion]} ha sido agregado al carrito.")
    else:
        print("Opción no válida.")
        

def verCarrito():
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        total = sum(carrito)
        print(f"Total a pagar: ${total}")



def menu():
    while True:
        print("Bienvenido a la Tienda Online Tec")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            mostratProductos()
        elif opcion == 2:
            agregarAlCarrito()
        elif opcion == 3:
            verCarrito()
        elif opcion == 4:
            print("Gracias por visitar la Tienda Online Tec")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            
menu()

