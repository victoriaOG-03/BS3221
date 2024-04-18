import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from werkzeug.urls import url_quote_plus  # Importing the correct function

# instantiating new object with "name"
app: Flask = Flask(__name__)

# the initial form page
@app.route('/')
def index():
    return "Hi!"
