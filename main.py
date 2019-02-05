import os
from flask import Flask, jsonify, request
from mlflow.pyfunc import load_pyfunc
from mlflow.utils import get_jsonable_obj
import pandas as pd



app = Flask(__name__)

def init():
    global model
    model = load_pyfunc("model")

@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
    try:
        data = request.get_json()
    except ValueError:
        return jsonify("Please enter a json.")

    input_df = pd.DataFrame(data['values'])

    return jsonify(model.predict(input_df).tolist()) #jsonify(lin_reg.predict(years_of_experience).tolist())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    init()
    app.run(host='0.0.0.0', port=port, debug=False)