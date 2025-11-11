from flask import Flask,render_template,request
import numpy as np 
import pandas as pd 
import sklearn 
import matplotlib.pyplot as plt 
import pickle 
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route('/')
def fun():
    return render_template('index.html')

@app.route("/predict",methods = ['GET','POST'])
def fun3():
    a = [float(i) for i in request.form.values()]
    b = [np.array(a)]
    print(type(b))
    sol = pickle.load(open("SLRH.pkl",'rb'))
    predictions = sol.predict(b)
    predictions = predictions[0]
    return render_template('index.html',prediction_text = predictions)

if __name__ == "__main__":
    app.run(debug=True)