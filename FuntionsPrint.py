#Funtions with expections for inputs and prints

#importing functions from FuntionsDB
from FuntionsDB import create, read, update, delete

# Function to add a new task with input
def createTask():
    #loop to validate inputs witgh an expection
    validar = True
    while validar:
        try:
            name = input("\nIngrese el nombre de la tarea: ")
            if name == "":
                print("⚠️ El nombre de la tarea no puede estar vacío.")
                continue
            pass
        except Exception as e:
            print("❌ Nombre invalido, ingrese letras.")
            validar = False
            raise e
        
        validar = True
        try:
            month = input("\nIngrese el mes de la tarea (MM): ")
            if not (1 <= int(month) <= 12):
                print("⚠️ Mes invalido, ingrese un número entre 01 y 12.")
                continue
            pass
        except Exception as e:
            print("❌ Mes invalido, ingrese números.")
            validar = False
            raise e
        
        validar = True
        try: 
            day = input("\nIngrese el día de la semana de la tarea (DD): ")
            if not (1 <= int(day) <= 7):
                print("⚠️ Día invalido, ingrese un número entre 01 y 07.")
                continue
            pass
        except Exception as e:
            print("❌ Día invalido, ingrese números.")
            validar = False
            raise e
        create(name, month, day)
        print("Tarea agregada exitosamente.")
    

def readTasks():
    print("\nLista de tareas:")
    read()
    
def updateTask():
    validar = True
    while validar:
        try:
            id_task = int(input("\nIngrese el ID de la tarea a completar: "))
            if id_task <= 0:
                print("⚠️ ID invalido, ingrese un número entero positivo.")
                continue
        except Exception as e:
            print("❌ ID invalido, ingrese un número entero.")
            validar = False
            raise e
        update(id_task)
        print("¡Tarea completada!✅.")        

def deleteTask():
    validar = True
    while validar:
        try:
            id_task = int(input("\nIngrese el ID de la tarea a eliminar: "))
            if id_task <= 0:
                print("⚠️ ID invalido, ingrese un número entero positivo.")
                continue
        except Exception as e:
            print("❌ ID invalido, ingrese un número entero.")
            validar = False
            raise e
        delete(id_task)
        print("¡Tarea eliminada!🗑️.")
        

def menu():
    print("\n=== Task Manager ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")

