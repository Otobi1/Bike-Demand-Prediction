from typing_extensions import runtime
import numpy as np
from Flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('./model_files/model.bin', 'rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    """
    For rendering results on HTML GUI
    """
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text = 'The bike demand is ${}'.format(output))

    if __name__ == '__main':
        app.run(debug = True)

