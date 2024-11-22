from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    wins = int(data['wins'])
    losses = int(data['losses'])
    
    # Predict probability using the model
    features = np.array([[wins, losses]])
    probability = model.predict_proba(features)[0][1] * 100  # Probability of winning
    
    return jsonify({'probability': probability})

if __name__ == '__main__':
    app.run(debug=True, port=5001)