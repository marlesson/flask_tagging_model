import os
from flask import Flask, jsonify, request
import pandas as pd
from joblib import dump, load

# Path do modelo que foi criado
MODEL    = load('model/model.joblib')  # 

# Proprietário da API
OWNER    = 'Quem sou eu?'

app      = Flask(__name__)

# POST /predict 
#
@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
    # Get Data
    try:
        data     = request.get_json()
        df_input = pd.DataFrame(data['instances'])
    except ValueError:
        return jsonify("Please enter a json.")

    # Predict no modelo
    predictions = MODEL.predict(df_input['texto']).tolist()

    return jsonify({"predictions": predictions})

# GET /
#
@app.route("/", methods=['get'])
def owner():
    return jsonify({"App": "FASAM - Turma 2", "Owner": OWNER})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=False)

