from flask import Flask, request, render_template
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
engine = create_engine("sqlite:///stroke_analysis.sqlite3", echo=True)
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

stroke_db = Base.classes.stroke_analysis

app = Flask(__name__)
model = pickle.load(open('ML_Test.pkl', 'rb')) 

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/data.html")
def data():
    return render_template('data.html')

@app.route('/prediction.html',methods=['POST'])
def predict():
    Age = int(request.form["Age"])
    Gender = request.form["Gender"]
    gender_dict = {'Male': 0, 'Female': 1}
    Gender_int = Gender.replace({'gender': gender_dict})
    Blood_Pressure = int(request.form["Blood Pressure"])
    Glucose = int(request.form["Glucose"])
    #Smoking = request.form["Smoking"]
    #Smoking_dict = {'No': 0, 'Former': 1, 'Current': 2}
    #Smoking_int = Smoking.replace{'Smoking': Smoking_dict}
        
    #prediction = model.predict([[rooms, distance]]) 
    #output = round(prediction[0], 2) 

    return render_template('prediction.html', prediction_text=f'{Age}, {Gender_int}, {Blood_Pressure}, {Glucose}')    
    #return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)