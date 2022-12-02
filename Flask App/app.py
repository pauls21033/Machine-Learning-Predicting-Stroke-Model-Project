from flask import Flask, request, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#from flask_marshmallow import Marshmallow
import os
import pickle

basedir = os.path.abspath(os.path.dirname(__file__))
# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + 
 #   os.path.join(basedir, '..Resources/stroke_analysis.sqlite'))
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
engine = create_engine("sqlite:///stroke_analysis.sqlite", echo=True)
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

stroke_db = Base.classes.stroke_analysis

app = Flask(__name__)
model = pickle.load(open('ML_Test.pkl', 'rb')) 

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)