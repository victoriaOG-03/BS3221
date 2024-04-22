import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
# import requests
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from werkzeug.urls import url_quote_plus  # Importing the correct function


app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Define route handler function to fetch pets data from MongoDB API
@app.route('/get_pets', methods=['GET'])
def get_pets():
    # MongoDB API endpoint URL
    url = "https://eu-west-2.aws.data.mongodb-api.com/app/data-xpfztyu/endpoint/data/v1/action/findOne"
    
    # Payload for the API request
    payload = json.dumps({
        "collection": "pets",
        "database": "woof_walk",
        "dataSource": "Waqq--ly",
        "projection": {
            "_id": 1
        }
    })
    
    # Headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': os.environ.get('MONGODB_API_KEY')  # Use environment variable for API key
    }
    
    # Send POST request to MongoDB API
    # response = requests.post(url, headers=headers, data=payload)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch pets data'}), 500

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
