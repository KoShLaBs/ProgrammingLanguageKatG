print("---Ejercicio 1️⃣---")

#Creando el vector edades
edades = [15, 37, 30, 25]

# Agregar elemento
edades.append(6)

#Insertar elemento en la poscion 1
edades.insert(1, 2)

#imprimir el vector edades con indices
print(f"Vector edades: {edades}")
print(f"Vector edades con indices (2): {edades[2]}")
print(f"Vector edades con indices (-2): {edades[-2]}")

#Cambiar el valor del indice 1 por 200
edades[1] = 200

#imprimir de nuevo
print(edades)

print("\n---Ejercicio 2️⃣---")

#creando el vector
v = [10, 20, 30, 40, 50, 60]

#slicing v[1:4], v[:5], v[2:], v[::-1], v[::2] y len(v)
print(f"Slicing v[1:4]: {v[1:4]}")
print(f"Slicing v[:5]: {v[:5]}")
print(f"Slicing v[2:]: {v[2:]}")
print(f"Slicing v[::-1]: {v[::-1]}")
print(f"Slicing v[::2]: {v[::2]}") 
print(f"Longitud de v: {len(v)}")

print("\n---Ejercicio 3️⃣---")

#reutilizxando el vector v y mostramos
print(f"Vector: {v}\n")
#eliminando el ultimo elemento
print("Vamos a eliminar")
v.pop()
print(f"Vector despues: {v}\n")

#eliminando el elemento en la posicion 0
print("Vamos a eliminar la posicion 0")
v.pop(0)
print(f"Vector despues: {v}\n")

#eliminando el elemento con valor 30
print("Vamos a eliminar el valor 30")
v.remove(30)
print(f"Vector despues: {v}\n")

#limpiando el vector
v.clear()
print(f"Vector despues de limpiar: {v}")

print("\n---Ejercicio 4️⃣---")
#reutilizando el vector edades
print(f"Vector: {edades}\n")
#Recorres vector por valor e impromir elemento
print("Vector con valor:")
for edad in edades:
    print(f"Edad: {edad}")

#Recorres vector por indice e imprmir elemento
print("\nVector con indice:")
for posicion in range(len(edades)):
    print(f"Edad en posicion {posicion}: {edades[posicion]}")
    
#Recorres vector con enumerate e impriomir indice y valor 
print("\nVector con indice y valor:")
for posicion, edad in enumerate(edades):
    print(f"Edad en posicion {posicion}: {edad}")
    
print("\n---Ejercicio 5️⃣---")

#creando el vector v
v = [3, 7, 2, 9]

#calcular suma, minimo, maximo y promedio
suma = sum(v)
minimo = min(v)
maximo = max(v)
promedio = suma / len(v)

print(f"1-Vector: {v}")
print(f"2-Suma: {suma}")
print(f"3-Minimo: {minimo}")
print(f"4-Maximo: {maximo}")
print(f"5-Promedio: {promedio}")

print("\n---Ejercicio 6️⃣---")

#creando el vector nombres
nombres = ["Ana", "Luis", "Meli"]

#Comprensión para pasar todo a mayúsculas
mayus = [nombre.upper() for nombre in nombres]

#guardar la longitud de cada nombre
largos = [len(nombre) for nombre in nombres]

#verificar si 
#"Mel" está en la lista
existeList = "Mel" in nombres
#"Mel" esta en "Melissa"
existeNombre = "Mel" in "Melissa"

#Imprimir datos
print(f"1-Vector nombres: {nombres}")
print(f"2-Vector mayusculas: {mayus}")
print(f"3-Vector largos: {largos}")
print(f"4-Existe 'Mel' en la lista nombres?: {existeList}")
print(f"5-Existe 'Mel' en el nombre 'Melissa'?: {existeNombre}")

print("\n---Mini-reto 7️⃣---")

#Info usuario
print("Jugemos a un juego!😊")

#vectores vacios
numeros = []
numerosMayor10 = []

#Pedir info a usuario
cantidad = int(input("➡Ingrese la cantidad de numeros que va a ingresar: "))

for numero in (range(cantidad)):
    valor = int(input(f"➡Ingrese el numero {numero + 1}: "))
    numeros.append(valor)

#Calculemos
suma = sum(numeros)
promedio = suma / len(numeros)

for numero in numeros:
    if numero > 10:
        numerosMayor10.append(numero)

hay5 = 5 in numeros

#Mostrar datos
print(f"Lista de numeros: {numeros}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Números mayores a 10: {numerosMayor10}")
print(f"¿Hay un 5 en la lista?: {hay5}")

print("\n---Fin del juego!🎉---")


