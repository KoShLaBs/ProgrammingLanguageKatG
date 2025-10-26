#Listas, funciones, menus y expeciones

tasks = []

#Necesitamos que sea incrementario para asignar IDs

ids = 1

#Funciones

#Menu principal
def menu():
    print("Task List")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

#Listar tareas
def listar():
    if not tasks:
        print("No hay tareas.")
        return
    
    print("\n ID | ESTADO | TITULO")
    
    for task in tasks:
        estado = "OK" if task[2] else "NOT"
        print(f" {task[0]}  |  {estado}  | {task[1]}")

#Agregar tarea
def agregar():
    global ids
    titulo = input("Titulo: ".strip())
    if not titulo:
        print("El titulo no puede estar vacio.")
        return
    tasks.append([ids, titulo, False])
    ids += 1
    print("Tarea agregada.")
    

#Marcar tarea como completada
def marcarTarea():
    if not tasks:
        print("No hay tareas.")
        return
    try:
        id = int(input("ID de la tarea a marcar como completada: ".strip()))
    except ValueError:
        print("ID invalido. Digite valores numericos.")
        return
    
    for task in tasks:
        if task[0] == id:
            task[2] = True
            print("Tarea marcada como completada.")
            return
    
    print("Tarea no encontrada.")
    
    
#Eliminar tarea
def eliminar():
    if not tasks:
        print("No hay tareas.")
        return
    try:
        id = int(input("ID de la tarea a eliminar: ".strip()))
    except ValueError:
        print("ID invalido. Digite valores numericos.")
        return
    
    for contar, task in enumerate(tasks):
        if task[0] == id:
            del tasks[contar]
            print("Tarea eliminada.")
            return
    
    print("Tarea no encontrada.")
    
    
    

#Main loop

while True:
    menu()
    opcion = input("Seleccione una opcion: ".strip())
    
    if opcion == "1":
        agregar()
    elif opcion == "2":
        listar()
    elif opcion == "3":
        marcarTarea()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")


    