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
    return

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365) #add line of code calculating date
    return

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all() # add code line writing query filtering for date and rain for prev yr
   return

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation} # creating dictionary with date as key, precipitation as value
   return jsonify(precip) #formatting to json (better for clean/filter/sort/visualize data)


##CREATE THE STATION ROUTE
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all() #allows to retrieve all stations in db
    stations = list(np.ravel(results)) #convert aarry to a list with results as the parameter
    return jsonify(stations=stations)


##CREATE THE MONTHLY TEMPERATURE ROUTE
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all() # query primary station for all temp observs
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


##CREATE THE STATISTICS ROUTE
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>") #have to provide the start and end dates separately
def stats():
    return


def stats(start=None, end=None): # need to add parameters
    return

def stats(start=None, end=None):
    #creating a query to select min.max, avg temps as a lsit
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end: # need to determine start and end date
        results = session.query(*sel).\ #* states there'll be multiple results
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\ # now calculating the min,avg,max with start and end dates
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#flask run

