#Create menu and functions to interact with the user
from FuntionsPrint import menu, createTask, readTasks, updateTask, deleteTask

menu()

validar = True
while validar:
    try:
        option = input("\nIngresa una opción: ")
        optionNum = int(option)
        if (optionNum < 0 and optionNum > 4):
            print("⚠️ Opción invalida, ingrese un número del 0 al 4.")
            continue
        pass
    except Exception as e:
        print("❌ Opción invalida. Ingrese un número de las opciones")
        validar = False
        raise e
    match option:
        case "1":
            createTask()
        case "2":
            readTasks()
        case "3":
            updateTask()
        case "4":
            deleteTask()
        case "0":
            print("\nNos vemos la proxima!\n")
            break

