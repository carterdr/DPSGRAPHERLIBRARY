from google.cloud.sql.connector import Connector
from google.oauth2 import service_account
from Libraries.config import print_to_sheet_when_saving, print_name_when_saving
from Libraries.Excel import print_to_sheet
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the Cloud SQL Connector
credentials_path = "key.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)
connector = Connector(credentials=credentials)

# Replace with your instance connection name
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

# Database connection details
db_config = {
    "dbname": os.getenv("DB_NAME"),  # Replace with your database name
    "user": os.getenv("DB_USER"),        # Replace with your database username
    "password": os.getenv("DB_PASSWORD"),    # R
}


table_query = '''CREATE TABLE IF NOT EXISTS Damages (
                description TEXT PRIMARY KEY NOT NULL,
                category TEXT NOT NULL,
                dot INT[]
                );'''

def get_connection():
    # Use the Cloud SQL Connector to create a secure connection
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=db_config["user"],
        password=db_config["password"],
        db=db_config["dbname"],
    )
    return conn
def reset_table():
    query = """
            TRUNCATE TABLE damages;
            """
    try:
        # Establish a connection
        conn = get_connection()
        try:
            # Create a cursor
            cursor = conn.cursor()

            # Test the connection
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"Connected to PostgreSQL version: {version[0]}")

            # Execute the query
            cursor.execute(query)
            conn.commit()  # Commit the transaction
            print(f"Successfully cleared Table")
        finally:
            # Ensure the cursor and connection are closed
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error: {e}")
def save_to_database(result, category):
    if print_name_when_saving:
        print(result)
    if print_to_sheet_when_saving:
        print_to_sheet(result)
    name = result.name
    values = result.dot.tolist()

    query = """
            INSERT INTO Damages (description, category, dot)
            VALUES (%s, %s, %s)
            ON CONFLICT (description)
            DO UPDATE SET
            category = EXCLUDED.category,
            dot = EXCLUDED.dot;
            """
    try:
        # Establish a connection
        conn = get_connection()
        try:
            # Create a cursor
            cursor = conn.cursor()

            # Test the connection
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"Connected to PostgreSQL version: {version[0]}")

            # Execute the query
            cursor.execute(query, (name, category, values))
            conn.commit()  # Commit the transaction
            print(f"Upsert successful for {name}")
        finally:
            # Ensure the cursor and connection are closed
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error: {e}")
