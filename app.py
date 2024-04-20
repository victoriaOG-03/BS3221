import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from werkzeug.urls import url_quote_plus  # Importing the correct function

# # acces to my MongoDB Atlas Cluster
# load_dotenv()
# connection_string: str = os.environ.get("CONNECTION_STRING")
# mongo_client: MongoClient = MongoClient(connection_string)


# # adding in the database
# database: Database = mongo_client.get_database("woof-walk")

# #adding in the collections
# user_profile_collection: Collection = database.get_collection("user_profile")
# pets_collection: Collection = database.get_collection("pets")
# dog_walkers_collection: Collection = database.get_collection("dog_walkers")
# service_requests_collection: Collection = database.get_collection("service_requests")
# collection: Collection = database.get_collection("user_profile")

# pet = {"name": "Lily", "breed": "Doberman", "age": 7, "size": "Large", "medicalHistory": "None"}
# collection.insert_one(pet)



# instantiating new object with "name"
app: Flask = Flask(__name__)


# Route for the initial form page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Register Dog page
@app.route('/register_dog')
def register_dog():
    return render_template('Pages/registerdog.html')

# Route for Search Dog page
@app.route('/search_dog')
def search_dog():
    return render_template('Pages/searchdog.html')

# Route for Register Dog Walker page
@app.route('/register_dog_walker')
def register_dog_walker():
    return render_template('Pages/registerdogwalker.html')

# Route for Search Dog Walker page
@app.route('/search_dog_walker')
def search_dog_walker():
    return render_template('Pages/searchdogwalker.html')

if __name__ == '__main__':
    app.run(debug=True)

# # the initial form page
# @app.route('/')
# def index():
#     return "Hello!"
