import mysql.connector
import hashlib

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="",        # XAMPP default has no password
        database="chatbot"
    )

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hash_password(password)))
        conn.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hash_password(password)))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None
