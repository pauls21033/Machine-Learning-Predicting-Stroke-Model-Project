import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


# Database Setup

engine = create_engine("sqlite:///stroke_analysis.sqlite")

#reflect an existing database into a new mocel
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)