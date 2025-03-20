import sqlite3  

connection = sqlite3.connect('test.db')  

cursor = connection.cursor()  
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS users (  
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT NOT NULL,  
        email TEXT NOT NULL UNIQUE  
    )  
''')  

# Insert sample data  
cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")  
cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com')")  

connection.commit()  
connection.close()  