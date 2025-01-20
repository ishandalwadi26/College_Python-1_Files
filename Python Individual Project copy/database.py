# database.py
import mysql.connector
from config import DB_CONFIG

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor(dictionary=True)
            print("Database connection successful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def __del__(self):
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Database connection closed")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            print("hi")
            self.conn.commit()
            print("hi")
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()
            return None