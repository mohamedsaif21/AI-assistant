# search_auth.py
import mysql.connector
from face_auth import authenticate_face

def store_search_history(user, query):
    conn = mysql.connector.connect(
        host="localhost",
        user="youruser",
        password="yourpassword",
        database="search_history_db"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (user, query) VALUES (%s, %s)", (user, query))
    conn.commit()
    conn.close()

def access_history(user):
    if authenticate_face():
        conn = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpassword",
            database="search_history_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT query FROM history WHERE user = %s", (user,))
        for row in cursor.fetchall():
            print(row[0])
        conn.close()
    else:
        print("Face authentication failed!")

if __name__ == "__main__":
    user = "JohnDoe"
    store_search_history(user, "Iron Man suit design")
    access_history(user)
