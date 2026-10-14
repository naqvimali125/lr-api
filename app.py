import random
from flask import Flask, request, jsonify

REG_NO = "SP23-BAI-048"
SEED = REG_NO

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok", "use": "/predict?x1=2&x2=3&x3=1"})

@app.route("/predict")
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])
    except (KeyError, ValueError):
        return jsonify({"error": "send numeric x1, x2, x3"}), 400
    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({"registration number": REG_NO, "prediction": round(y, 2)})
