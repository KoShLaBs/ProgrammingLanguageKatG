#Funciones
import sqlite3

def conectar():
    return sqlite3.connect("tasks.db")

def agregar(name, month, day):
    conn = conectar()
    conn.execute("INSERT INTO tasks (name, month, day) VALUES (?, ?, ?)", (name, month, day))
    conn.commit()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        estado = "✅" if t[2] else "❌"
        print(f"[{t[0]}] {t[1]} ({t[4]}, {t[3]}) - {estado}")
    conn.close()

def completar(id_tarea):
    conn = conectar()
    conn.execute("UPDATE tasks SET completado = 1 WHERE id = ?", (id_tarea,))
    conn.commit()
    conn.close()

def eliminar(id_tarea):
    conn = conectar()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id_tarea,))
    conn.commit()
    conn.close()

# --- Programa principal ---
while True:
    print("\n=== 📋 GESTOR DE tasks ===")
    print("1. Agregar tarea")
    print("2. Listar tasks")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    opcion = input("→ Opción: ")

    if opcion == "1":
        name = input("name de la tarea: ")
        month = input("month: ")
        day = input("Día de la semana: ")
        agregar(name, month, day)
    elif opcion == "2":
        listar()
    elif opcion == "3":
        listar()
        completar(int(input("ID de la tarea a completar: ")))
    elif opcion == "4":
        listar()
        eliminar(int(input("ID de la tarea a eliminar: ")))
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
