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
    for task in cursor.fetchall():
        estado = "✅" if task[2] else "❌"
        print(f"[{task[0]}] {task[1]} - {estado}")
    conn.close()

# Function to mark a task as completed
def update(id_task):
    conn = connect()
    conn.execute("DELETE tasks SET complete= 1 WHERE id = ?", (id_task,))
    conn.commit()
    conn.close()

# Function to delete a task
def delete(id_task):
    conn = connect()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id_task,))
    conn.commit()
    conn.close()
