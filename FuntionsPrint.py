#Funtions with expections for inputs and prints

#importing functions from FuntionsDB
from FuntionsDB import create, read, update, delete

# Function to add a new task with input
def createTask():
    #loop to validate inputs witgh an expection
    while True:
        try:
            name = input("Ingrese el nombre de la tarea: ")
            if name == "":
                print("⚠️ El nombre de la tarea no puede estar vacío.")
                continue
            else:
                break
        except Exception as e:
            print("❌ Nombre invalido, ingrese letras.")
            continue       
        
    while True:
        try:
            month = input("Ingrese el mes de la tarea (MM): ")
            if not (1 <= int(month) <= 12):
                print("⚠️ Mes invalido, ingrese un número entre 01 y 12.")
                continue
            else:
                break
        except Exception as e:
            print("❌ Mes invalido, ingrese números.")
            continue

    while True:
        try: 
            day = input("Ingrese el día de la semana de la tarea (DD): ")
            if not (1 <= int(day) <= 7):
                print("⚠️ Día invalido, ingrese un número entre 01 y 07.")
                continue
            else:
                break
        except Exception as e:
            print("❌ Día invalido, ingrese números.")
            continue

    create(name, month, day)
    print("\nTarea agregada exitosamente.")


# Function to read and print all tasks
def readTasks():
    print("\nLista de tareas:")
    read()
    
# Function to update a task as completed
def updateTask():
    while True:
        try:
            id_task = int(input("\nIngrese el ID de la tarea a completar: "))
            if id_task <= 0:
                print("⚠️ ID invalido, ingrese un número entero positivo.")
                continue
            else:
                break
        except Exception as e:
            print("❌ ID invalido, ingrese un número entero.")
            continue
        
    update(id_task)
    print("\n¡Tarea completada!✅.")        

# Function to delete a task
def deleteTask():
    while True:
        try:
            id_task = int(input("\nIngrese el ID de la tarea a eliminar: "))
            if id_task <= 0:
                print("⚠️ ID invalido, ingrese un número entero positivo.")
                continue
            else:
                break
        except Exception as e:
            print("❌ ID invalido, ingrese un número entero.")
            continue
    
    #Validar entrada
    
    delete(id_task)
    print("\n¡Tarea eliminada!🗑️.")
        

# Function to print the menu
def menu():
    print("\n=== Task Manager ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")

