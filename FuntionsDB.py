#Funtions to interact with the database
#Generate CRUD (create, read, update, delete) operations
import sqlite3

# Function to connect to the database
def connect():
    return sqlite3.connect("tasks.db")

# Function to add a new task
def create(name, month, day):
    conn = connect()
    conn.execute("INSERT INTO tasks (name, month, day) VALUES (?, ?, ?)", (name, month, day))
    conn.commit()
    conn.close()

# Function to list all tasks
def read():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    for i, task in enumerate(cursor.fetchall()):
        estado = "✅" if task[2] else "❌"
        print(f"{i+1}. ID:{task[0]} - {task[1]} - {estado}")
    conn.close()
    

#Function to read per month
def readPerMonth():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    months = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    taskPerMonth = {month: [] for month in months.values()}
    for i, task in enumerate(cursor.fetchall()):
        estado = "✅" if task[2] else "❌"
        monthNum = int(task[3])

        if monthNum in months:
            monthName = months[monthNum]
            taskTxt = f"{i+1}. ID:{task[0]} - {task[1]} - {estado}"
            taskPerMonth[monthName].append(taskTxt)

    conn.close()
    for month, tareas in taskPerMonth.items():
        if tareas:
            print(f"\n--- {month} ---")
            for t in tareas:
                print(t)
                

#Function to read per day of week
def readPerWeek():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    weeks = {
        1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves",
        5: "Viernes", 6: "Sabado", 7: "Domingo"
    }
    taskPerWeek = {week: [] for week in weeks.values()}
    for i, task in enumerate(cursor.fetchall()):
        estado = "✅" if task[2] else "❌"
        weekNum = int(task[4])

        if weekNum in weeks:
            weekName = weeks[weekNum]
            tarea_texto = f"{i+1}. ID:{task[0]} - {task[1]} - {estado}"
            taskPerWeek[weekName].append(tarea_texto)

    conn.close()
    for week, tareas in taskPerWeek.items():
        if tareas:
            print(f"\n--- {week} ---")
            for t in tareas:
                print(t)

# Function to mark a task as completed
def update(id_task):
    conn = connect()
    conn.execute("UPDATE tasks SET complete= 1 WHERE id = ?", (id_task,))
    conn.commit()
    conn.close()

# Function to delete a task
def delete(id_task):
    conn = connect()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id_task,))
    conn.commit()
    conn.close()
