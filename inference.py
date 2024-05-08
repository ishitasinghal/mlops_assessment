import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)

model = tf.keras.models.load_model('my-model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (28, 28))
        img = np.invert(img)
        img = img.reshape(1, 28, 28, 1)
        prediction = model.predict(img)
        return jsonify({'prediction': int(np.argmax(prediction))}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
