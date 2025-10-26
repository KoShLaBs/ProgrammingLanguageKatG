import sqlite3

# Crear base de datos
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    complete INTEGER DEFAULT 0,
    month TEXT,
    day TEXT
)
""")

conn.commit()
conn.close()

print("✅ Base de datos y tabla 'tasks' creadas correctamente.")
