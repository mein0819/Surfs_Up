import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# access and query SQLite Database file
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from Python to database
session = Session(engine)

# define our Flask app
app = Flask(__name__)

# define welcome route
@app.route("/")

# create function welcome() 
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    '''
    )

# create precipitation analysis route
@app.route("/api/v1.0/precipitation")

# create precipitation() function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
     # query to get date and precipitation from prev. year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# create stations route
@app.route("/api/v1.0/stations")

# create stations() function
def stations():
    # query to get all stations from database
    results = session.query(Station.station).all()
    # unravel results into one-dimensional array
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# create temperature observations route
@app.route("/api/v1.0/tobs")

# create temp_monthly() function
def temp_monthly():
    # calculate date one year ago from last date in DB
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # queary primary station for temp. obvservations
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel results into one-dimensional array and convert to list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create stat() function
def stats(start=None, end=None):
    # create list to hold query for min, avg, max temp from DB
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)