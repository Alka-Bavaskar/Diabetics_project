
from flask import Flask, jsonify, render_template, request

from project_app.utils import Diabetes

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Diabetes Prediction System") 
    return render_template("index.html")


@app.route("/predict_result", methods = ["POST", "GET"])
def get_species_type():
    if request.method == "GET":
        print("We are in a GET Method")

        Glucose = float(request.args.get("Glucose"))
        BloodPressure = float(request.args.get("BloodPressure"))
        SkinThickness = float(request.args.get("SkinThickness"))
        Insulin = float(request.args.get("Insulin"))
        BMI = float(request.args.get("BMI"))
        DiabetesPedigreeFunction = float(request.args.get("DiabetesPedigreeFunction"))
        Age = int(request.args.get("Age"))
        
        print("***************Glucose, BloodPressure, Insulin, DiabetesPedigreeFunction, Age **********************\n", Glucose, BloodPressure, Insulin, DiabetesPedigreeFunction, Age)
        
        dia_res = Diabetes(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        prediction = dia_res.get_predicted_result()

        if prediction == 1:
            text = "The patient is diabetic"
        else:
            text = "The patient is not diabetic"

        return render_template("index.html", prediction = text)
        
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters

