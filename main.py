import os
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
  if request.method == 'POST':
    try:
        data = request.get_json()

    except ValueError:
        return jsonify("Please enter a json.")

    return jsonify(data) #jsonify(lin_reg.predict(years_of_experience).tolist())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)