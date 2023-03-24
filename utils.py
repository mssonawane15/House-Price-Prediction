import numpy as np
import json
import pickle


class House_Price_Predictor:
    def __init__(self,bhk,total_sqft,bath,balcony,location):
        self.bhk = bhk
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.location = location

    def load(self):
        self.model = pickle.load(open("model.pkl", "rb"))
        self.columns = json.load(open("columns.json","r"))

    def get_price(self):
        self.load()
        location_index = self.columns["columns"].index(self.location)
        arr = np.zeros(len(self.columns["columns"]))
        arr[0] = self.bhk
        arr[1] = self.total_sqft
        arr[2] = self.bath
        arr[3] = self.balcony
        arr[location_index] = 1
      
        prediction = self.model.predict([arr])
        return prediction

        