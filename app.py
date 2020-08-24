from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.ext import automap
from sqlalchemy import inspect
from sqlalchemy import func
import numpy as np
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap.automap_base()
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"*****Welcome to Hawaii API*****<br/>"
        f"<br/>"
        f"Select The Available Routes :<br/>"
        f"********************************** <br/>"
        f"********************************** <br/>"
        f"For Precipitation Data :<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"********************************** <br/>"
        f"For Station List :<br/>"
        f"/api/v1.0/stations<br/>"
        f"********************************** <br/>"
        f"For tobs for the previous year <br/>"
        f"/api/v1.0/tobs_MostActiveStation<br/>"
        f"********************************** <br/>"
        f"For TMIN, TAVG, and TMAX for all data >= Given Start Date <br/>"
        f"Replace Start Between Range 2016-08-23 to 2017-08-23 <br/>"
        f"/api/v1.0/start date<br/>"
        f"********************************** :<br/>"
        f"For TMIN, TAVG, and TMAX between Given range of date Including end Date <br/>"
        f"Replace Start and end Date Between range 2016-08-23 to 2017-08-23<br/>"
        f"/api/v1.0/start date/end date"
    )

