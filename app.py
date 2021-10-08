# Routes (tricky to build) are a core Flask concept.Routes are different pathways that a search can take.
# Welcome, Precipitation, Stations, Monthly Temperature, and Statistics are the routes to be created"

# import dependencies
from flask import Flask

#Create an Flask App Instance (singular version of something)
    #the _name_ var denotes the name of the function. Can determine of code is ran from command line or imported
    #into another piece of code. this is a magic methods var

app = Flask(__name__)

#Create Flask Routes

#1.define the starting point or the root. the / states to put the data at the root of the routes.
    # Its the highest level hierarchy
@app.route('/')

#2. create a function.
def hello_world():
    return 'Hello world'

# this code will be ran in the command line using anaconda powrshell enter: set FLASK_APP=app.py
# then run the app enter: flask run
# a line stating "Running on http:........ (localhost address and port number)
#Copy paste localhost adress in web browser