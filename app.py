# Importing necessary libraries
from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

# Creating an instance of Flask app
app = Flask(__name__)

# Function to connect with MongoDB and get the database
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["eagle_db"]
    return db

# Defining a route for the home page
@app.route('/')
def get_stored_eagles():
    # Calling the function to get the database
    db = get_db()
    # Retrieving data from the eagle_tb collection
    _eagles = db.eagle_tb.find()
    
    # Concatenating the name and description of each eagle to a list
    eagles_names = [eagle['name']+": " + eagle['description'] for eagle in _eagles]
    
    # Joining the list of eagles' names and descriptions with line breaks
    eagle_list = '\n'.join(eagles_names)
    
    # Creating a hyperlink to the acknowledgements page
    acknowledgements_link = f"<a href='http://localhost:5000/acknowledgements'>Click here to see our Acknowledgements</a>"
    
    # Creating a string of text to be displayed on the home page
    first_line = "These are the most common eagles that belong to Asia and African continents. The serpent eagles are popular species that hunt and go after reptiles and snakes. These eagles come with very sharp and powerful beaks, clear and distant vision, and are silent too. These characteristics of being sharp, clear, powerful in nature make them distinct from other species in being excellent hunters. They aren’t, however, enormous like other species of eagles when compared."
    text = f"{first_line}\n\n{eagle_list}\n\n{acknowledgements_link}"
    
    # Wrapping the text in a pre tag to preserve whitespace and prevent overflow
    final_text = "<pre style='white-space: pre-wrap; max-width: 100%;'>" + text + "</pre>"
    
    # Returning the text to display on the home page
    return final_text

# Defining a route for the acknowledgements page
@app.route('/acknowledgements')
def ping_server():
    # Reading the contents of the acknowledgements.txt file
    with open('acknowledgements.txt', 'r') as f:
        acknowledgements = f.read()

    # Creating a hyperlink to the home page
    back_main = f"<a href='http://localhost:5000/'>Back to the home page.</a>"
    
    # Wrapping the acknowledgements text and hyperlink in a pre tag to preserve whitespace and prevent overflow
    return "<pre style='white-space: pre-wrap; max-width: 100%;'>" + str(acknowledgements) + f"\n\n{back_main}</pre>"

# Starting the Flask app
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)