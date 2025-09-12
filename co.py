import mysql.connector
from mysql.connector import Error

def get_connection():

    try:
        conn = mysql.connector.connect(
            host="localhost",       
            user="root",  
            password="Malkhed@123", 
            database="soilrecommendation"  
        )
        if conn.is_connected():
            print("✅ Successfully connected to the database")
            return conn
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None
