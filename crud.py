import sqlite3  

DATABASE = 'test.db'  

def create_user(name, email):  
    connection = sqlite3.connect(DATABASE)  
    cursor = connection.cursor()  
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))  
    connection.commit()  
    connection.close()  

def read_users():  
    connection = sqlite3.connect(DATABASE)  
    cursor = connection.cursor()  
    cursor.execute("SELECT * FROM users")  
    users = cursor.fetchall()  
    connection.close()  
    return users  

def update_user(user_id, name, email):  
    connection = sqlite3.connect(DATABASE)  
    cursor = connection.cursor()  
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))  
    connection.commit()  
    connection.close()  

def delete_user(user_id):  
    connection = sqlite3.connect(DATABASE)  
    cursor = connection.cursor()  
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))  
    connection.commit()  
    connection.close()  