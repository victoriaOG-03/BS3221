import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from werkzeug.urls import url_quote_plus  # Importing the correct function

# acces to my MongoDB Atlas Cluster
load_dotenv()
connection_string: str = os.environ.get("CONNECTION_STRING")
mongo_client: MongoClient = MongoClient(connection_string)


# adding in the database
database: Database = mongo_client.get_database("woof-walk")

#adding in the collections
user_profile_collection: Collection = database.get_collection("user_profile")
pets_collection: Collection = database.get_collection("pets")
dog_walkers_collection: Collection = database.get_collection("dog_walkers")
service_requests_collection: Collection = database.get_collection("service_requests")
collection: Collection = database.get_collection("user_profile")

pet = {"name": "Lily", "breed": "Doberman", "age": 7, "size": "Large", "medicalHistory": "None"}
collection.insert_one(pet)

# instantiating new object with "name"
app: Flask = Flask(__name__)

# the initial form page
@app.route('/')
def index():
    return "Hello!"
