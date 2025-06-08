from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import traceback
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Get user input from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Create a list with the user input
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]

            # Convert the list to a numpy array
            data = np.array(data).reshape(1, 11)
            print('The input data is: ', data)
            # Create an instance of the PredictionPipeline
            obj = PredictionPipeline()
          
            # Make predictions using the predict method
            predict = obj.predict(data)
            

            print('The prediction is: ', predict)
            return render_template('results.html', prediction=predict[0])


        except Exception as e:
            print('The Exception message is:', e)
            traceback.print_exc()  # Add this line
            return 'Something went wrong'
        

    else:
        return render_template('index.html')
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
