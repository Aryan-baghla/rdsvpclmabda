import boto3
import os
import pymysql
import logging


# Retrieve database credentials from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_NAME = os.environ.get("DB_NAME")
# Hardcoded username and password
DB_USERNAME = "user"
DB_PASSWORD = "9[IA0$6yDjb15)+6[-~HM9L{nSCl"

def get_secret():
    return {
        'username': DB_USERNAME,
        'password': DB_PASSWORD
    }

def connect_to_db():
    secret = get_secret()
    connection = pymysql.connect(
        host=DB_HOST,
        user=secret['username'],
        password=secret['password'],
        database=DB_NAME,
        port=DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def create_table():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # SQL query to create the table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    """
    
    try:
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'data' created successfully!")
    except Exception as e:
        print("Error:", e)
        connection.rollback()
    finally:
        connection.close()

def insert_dummy_data():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # SQL query to insert dummy data
    insert_query = "INSERT INTO data (name, age) VALUES (%s, %s)"
    dummy_data = [("John", 30), ("Alice", 25), ("Bob", 35)]  # Example dummy data
    
    try:
        cursor.executemany(insert_query, dummy_data)
        connection.commit()
        print("Dummy data inserted successfully!")
    except Exception as e:
        print("Error:", e)
        connection.rollback()
    finally:
        connection.close()

def show_tables():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # SQL query to show tables
    show_tables_query = "SHOW TABLES"
    
    try:
        cursor.execute(show_tables_query)
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            table_name = table.get('Tables_in_sqldb')  # Safely retrieve table name
            if table_name:
                print(table_name)
    except Exception as e:
        logging.error("Error fetching tables: %s", str(e))
    finally:
        cursor.close()  # Close the cursor
        connection.close()
        
def handler(event, context):
    create_table()
    insert_dummy_data()
    show_tables()
