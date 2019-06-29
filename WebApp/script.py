import os
import numpy as np
import json
import flask
import pickle
from flask import Flask, render_template, request


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/')
#     @app.route('/index')
#     def index():
#         return flask.render_template('index.html')
    
    
#     def ValuePredictor(to_predict_list):
#         to_predict = np.array(to_predict_list).reshape(1,12)
#         loaded_model = pickle.load(open("model.pkl","rb"))
#         result = loaded_model.predict(to_predict)
#         return result[0]
    
#     @app.route('/result',methods = ['POST', 'GET'])
#     def result():
#         if request.method == 'POST':
#             to_predict_list = request.form.to_dict()
#             to_predict_list=list(to_predict_list.values())
#             to_predict_list = list(map(int, to_predict_list))
#             result = ValuePredictor(to_predict_list)
#             if int(result)==1:
#                 prediction='Income more than 50K'
#             else:
#                 prediction='Income less that 50K'
#             return render_template("result.html",prediction=prediction)

#     return app

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result)==1:
            prediction='Income more than 50K'
        else:
            prediction='Income less that 50K'
        return render_template("result.html",prediction=to_predict_list)

@app.route('/predictsalary',methods=['POST'])
def SalaryPrediction():
    
    #Country: Create meta-data
    Country = {}
    with open("files/Country.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Country[str(key)] = int(val)
    #print (Country)

    #Education: Create meta-data
    Education = {}
    with open("files/Education.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Education[str(key)] = int(val)
    #print (Education)

    #Gender: Create meta-data
    Gender = {}
    with open("files/Gender.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Gender[str(key)] = int(val)
    #print (Gender)
    
    #MaritalStatus: Create meta-data
    MaritalStatus = {}
    with open("files/MaritalStatus.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            MaritalStatus[str(key)] = int(val)
    #print (MaritalStatus)

    #Occupation: Create meta-data
    Occupation = {}
    with open("files/Occupation.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Occupation[str(key)] = int(val)
    #print (Occupation)

    #Race: Create meta-data
    Race = {}
    with open("files/Race.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Race[str(key)] = int(val)
    #print (Race)

    #Relationship: Create meta-data
    Relationship = {}
    with open("files/Relationship.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            Relationship[str(key)] = int(val)
    #print (Relationship)

    #WorkingClass: Create meta-data
    WorkingClass = {}
    with open("files/WorkingClass.csv") as f:
        for line in f:
            (key, val) = line.split(':')
            WorkingClass[str(key)] = int(val)
    #print (WorkingClass)

    print (request.is_json)
    content = request.get_json()
    print (content)
    
    # update the status
    to_predict_list = content
    to_predict_list['WorkingClass'] = WorkingClass.get(to_predict_list['WorkingClass'])
    to_predict_list['Relationship'] = Relationship.get(to_predict_list['Relationship'])
    to_predict_list['Race'] = Race.get(to_predict_list['Race'])
    to_predict_list['Occupation'] = Occupation.get(to_predict_list['Occupation'])
    to_predict_list['MaritalStatus'] = MaritalStatus.get(to_predict_list['MaritalStatus'])
    to_predict_list['Education'] = Education.get(to_predict_list['Education'])
    to_predict_list['Gender'] = Gender.get(to_predict_list['Gender'])
    to_predict_list['Country'] = Country.get(to_predict_list['Country'])
    print (to_predict_list)
    to_predict_list=list(to_predict_list.values())
    to_predict_list = list(map(int, to_predict_list))
    result = ValuePredictor(to_predict_list)
    if int(result)==1:
        prediction='Income more than 50K'
    else:
        prediction='Income less that 50K'
    return prediction
    
