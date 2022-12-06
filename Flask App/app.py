from flask import Flask, request, render_template, jsonify
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
@app.route('/prediction')
def predict():
    #age = int(request.form["age"])
    #gender = int(request.form["Gender"])
    #s_blood_pressure = int(request.form["Sys blood pressure"])
    #d_blood_pressure = int(request.form["Dia blood pressure"])
    #glucose = int(request.form["glucose"])
    #smoking = int(request.form["Smoking"])
    #bmi = int(request.form["bmi"])
    #cholesterol = int(request.form["cholesterol"])
        
    #prediction = model.predict([[age, gender, s_blood_pressure, d_blood_pressure, glucose, smoking, bmi, cholesterol]]) 
    #output = round(prediction[0], 2) 

    return render_template('prediction.html')  

@app.route("/api/predict", methods=['GET','POST'])  
def result():
    survey = {}
    #print(request.form)
    #x = request.form.split("=")
    #print(x[0])
    data = request.form
    #print(data.get('age'))
    age = data.get('age')
    gender = data.get('Gender')
    s_blood_pressure = data.get('Sys blood pressure')
    d_blood_pressure = data.get('Dia blood pressure')
    glucose = data.get('glucose')
    smoking = data.get('Smoking')
    bmi = data.get('bmi')
    cholesterol = data.get("cholesterol")
    survey = {"age": age, "gender": gender, "s_blood_pressure": s_blood_pressure, "d_blood_pressure": d_blood_pressure, "glucose": glucose, "smoking": smoking, "bmi": bmi, "cholesterol": cholesterol}
    #prediction = model.predict([[age, gender, s_blood_pressure,d_blood_pressure, glucose, smoking, bmi, cholesterol]]) 
    #output = round(prediction[0], 2) 
    return jsonify(survey)

@app.route('/api/prediction',methods=['POST'])
def prediction():
    age = request.form('age')
    gender = request.form('Gender')
    s_blood_pressure = request.form('Sys blood pressure')
    d_blood_pressure = request.form('Dia blood pressure')
    glucose = request.form('glucose')
    smoking = request.form('Smoking')
    bmi = request.form('BMI')
    cholesterol = request.form("Cholesterol")
    prediction = model.predict([[age, gender, s_blood_pressure, d_blood_pressure, glucose, smoking, bmi, cholesterol]])
    output = prediction[0]
    return jsonify(output)

    return render_template('result.html', prediction_text=f'You are at risk for a level {output} stroke')

if __name__ == "__main__":
    app.run(debug=True)