import numpy as np
import pickle
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
model = pickle.load(open(r"C:\Users\yuvar\OneDrive\Desktop\Genetic classification\Genetic-classification.pkl",'rb'))
#column= pickle.load(open(r"C:\Users\yuvar\OneDrive\Desktop\Genetic classification\column G.pkl",'rb'))
@app.route('/')# route to display the home page
def Home():
  return render_template('index.html') #rendering the home page
@app.route('/About')#redering to about page
def About():
   return render_template('About.html')
@app.route('/Prediction')#rendering to Prediction page
def Prediction():
   return render_template('Prediction.html')
@app.route('/Prediction',methods=["POST","GET"])# route to showinput_feature=[float(x) for x in request.form.values() ] the predictions in a web UI
def prediction():

    x = [float(x) for x in request.form.values()]
    x=np.array(x)
  
    prediction=model.predict([x])
   
    if (prediction==0):
      return render_template("Prediction.html",predict="Clinical variant Classification")
    else:
      return render_template("Prediction.html",predict=" Confliting variant classification")
     
if __name__=="__main__":
   app.run(debug = True,port = 1234)
