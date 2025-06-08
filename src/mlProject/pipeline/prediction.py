import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from mlProject.utils.common import load_bin

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        print('Got the model ') 
   
   
    def predict(self, data):
       
        prediction = self.model.predict(data)

        return prediction
    
    
