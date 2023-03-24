import numpy as np
from flask import Flask, request
from utils import House_Price_Predictor

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Helloooo"
# app.run()

@app.route("/", methods =["POST"])
def get_prediction():
    data = request.form
    print(data)
    bhk = eval(data["bhk"]) 
    total_sqft = eval(data["total_sqft"]) 
    bath = eval(data["bath"]) 
    balcony = eval(data["balcony"]) 
    location = data["location"]
    instance = House_Price_Predictor(bhk,total_sqft,bath,balcony,location)

    price  = instance.get_price()

    return str(price[0])

app.run(debug=True)