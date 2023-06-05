
import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class Diabetes():
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

       
    def load_models(self):
        with open (config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH, 'r') as f:
            self.json_data = json.load(f)    
    
    def get_predicted_result(self):

        self.load_models()                # creating instance of model


        test_array = np.zeros(len(self.json_data["columns"]))

        # Assigning values to the array
        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age
        print("Test Array: ", test_array)

        prediction = self.model.predict([test_array])[0]

        return prediction

if __name__ == "__main__":
    Glucose = 130.000
    BloodPressure = 60.000
    SkinThickness = 37.000
    Insulin = 0.000
    BMI = 35.600
    DiabetesPedigreeFunction = 0.71
    Age = 48.000

    dia_res = Diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    prediction = dia_res.get_predicted_result() 

    if prediction == 1:
        print("The patient is diabetic")
    else:
        print("The patient is not diabetic")