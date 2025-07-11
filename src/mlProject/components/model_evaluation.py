import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
from mlProject.utils.common import save_json
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub
from mlProject.entity.config_entity import ModelEvaluationConfig





class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        dagshub.init(repo_owner='preetdhanani', repo_name='MLOps', mlflow=True)

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
    
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=self.config.metric_file_name, data=scores)
            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
    
