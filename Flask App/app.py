from flask import Flask, request, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
import os
import pickle

basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine("sqlite:///stroke_analysis.sqlite3", echo=True)
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

stroke_db = Base.classes.stroke_analysis

app = Flask(__name__)
model = pickle.load(open('ML_Test.pkl', 'rb')) 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/data")
def data():
    return render_template('data.html')


#,methods=['POST']
@app.route('/prediction',methods=['POST'])
def predict():
    age = int(request.form["Age"])
    gender = int(request.form["Gender"])
    blood_pressure = int(request.form["Blood Pressure"])
    glucose = int(request.form["Glucose"])
    smoking = int(request.form["Smoking"])
    bmi = int(request.form["BMI"])
    cholesterol = int(request.form["Cholesterol"])
        
    prediction = model.predict([[age, gender, blood_pressure, glucose, smoking, bmi, cholesterol]]) 
    output = round(prediction[0], 2) 

    return render_template('prediction.html', prediction_text=f'{output}')  

#@app.route("/result")  
#def result():
 #   prediction = model.predict([[age, gender, blood_pressure, glucose, smoking, bmi, cholesterol]]) 
  #  output = round(prediction[0], 2) 
   # return render_template('result.html', prediction_text= f'{output}')
    

if __name__ == "__main__":
    app.run(debug=True)