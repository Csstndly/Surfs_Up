# IMPORT DEPENDCIES
import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#SETUP DATABASE (enables access to the SQLite db)
engine = create_engine("sqlite:///hawaii.sqlite")

#REFLECT DB INTO THE CLASSES
Base = automap_base()
Base.prepare(engine, reflect=True) #.prepare reflects the tables into the alchemy

#SAVE REFERENCES TO EACH TABLE
Measurement = Base.classes.measurement
Station = Base.classes.station

#CREATE A SESSION LINK
session = Session(engine)

#DEFINE THE FLASK APP
app = Flask(__name__)

#DEFINE THE WELCOME ROUTE/ STARTING POINT
@app.route("/")

#CREATE FUNCTION WITH ALL THE ROUTES INSIDE A RETURN STATEMENT
def welcome():
    return( #/api/v1.0/ this convention signifies that this is verios 1 and can be updates
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation 
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

##CREATE THE PRECIPITATION ROUTE
    #building route to be able to access analysis in real time with just URL

#DEFINE THE ROUTE
@app.route("/api/v1.0/precipitation")


#CREATE THE FUNCTION
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    returngit