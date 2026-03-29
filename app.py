from flask import Flask, request,jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline



app = Flask(__name__)
CORS(app)

# Route for a home page

@app.route('/')
def home():
    return "Student Performance Prediction API is running successfully"


@app.route('/predict', methods=['POST'])
def predict_datapoint():
    try:
        data = request.get_json()

        data = CustomData(
            gender=data.get('gender'),
            race_ethnicity=data.get('race_ethnicity'),
            parental_level_of_education=data.get('parental_level_of_education'),
            lunch=data.get('lunch'),
            test_preparation_course=data.get('test_preparation_course'),
            reading_score=float(data.get('reading_score')),
            writing_score=float(data.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        return jsonify({
            "prediction": float(result[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=10000)