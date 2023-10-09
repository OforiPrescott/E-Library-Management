# database/setup.py

import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('database/library.db')
cursor = conn.cursor()

# Define a function to create the database tables
def create_database_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available BOOLEAN DEFAULT TRUE
        )
    ''')
    conn.commit()

# Call the function to create the database tables
create_database_tables()
