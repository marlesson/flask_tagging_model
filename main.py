import os
from flask import Flask, jsonify, request
from mlflow.pyfunc import load_pyfunc
from mlflow.utils import get_jsonable_obj
import pandas as pd

app      = Flask(__name__)
model    = load_pyfunc("model")
features = ["fixed acidity","volatile acidity",
            "citric acid","residual sugar","chlorides",
            "free sulfur dioxide", "total sulfur dioxide",
            "density","pH","sulphates","alcohol"]

@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':

    try:
        data = request.get_json()
    except ValueError:
        return jsonify("Please enter a json.")

    input_df    = pd.DataFrame(data['instances'])
    predictions = model.predict(input_df[features]).tolist()

    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)