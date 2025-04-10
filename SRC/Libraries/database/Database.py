from pymongo import MongoClient, UpdateOne
from dotenv import load_dotenv
from Libraries.utils.config import *
from Libraries.utils.Excel import print_to_sheet
import os
import json

load_dotenv()

# Load credentials from environment
MONGO_URI = os.getenv("MONGO_URI")  # Format: mongodb+srv://<user>:<pass>@cluster.mongodb.net/<db>?retryWrites=true&w=majority
DB_NAME = os.getenv("DB_NAME") 
COLLECTION_NAME = os.getenv("COLLECTION_NAME") 

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
damages_collection = db[COLLECTION_NAME]

# Drop the collection if needed
def drop_dot_collection():
    try:
        damages_collection.drop()
        print("Collection dropped successfully.")
    except Exception as e:
        print(f"Error dropping collection: {e}")

# Save or update document in the database
def save_to_database(result, category):
    if print_name_when_saving:
        print(result)
    if print_to_sheet_when_saving:
        print_to_sheet(result)

    name = result.name
    values = result.dot.tolist()

    document = {
        "category": category,
        "dot": values
    }

    try:
        damages_collection.update_one(
            {"description": name},
            {"$set": document},
            upsert=True
        )
        print(f"Upsert successful for {name}")
    except Exception as e:
        print(f"Error saving to database: {e}")