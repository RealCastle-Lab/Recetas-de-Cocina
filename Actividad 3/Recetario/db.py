import sqlite3

def get_db_connection():
    conn = sqlite3.connect('recetario.db')
    conn.row_factory = sqlite3.Row
    return conn

def execute_sql(query, args=(), commit=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    if commit:
        conn.commit()
        return True
    return cursor.fetchall()
