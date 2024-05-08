import cv2
import numpy as np
import tensorflow as tf
import gradio as gr

model = tf.keras.models.load_model('my-model.h5')

def predict(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))
    img = np.invert(img)
    img = img.reshape(1, 28, 28, 1)
    prediction = model.predict(img)
    print(prediction)
    return f'Number is: {int(np.argmax(prediction))}'

iface = gr.Interface(fn=predict, inputs="image", outputs="label")
iface.launch(server_name="0.0.0.0")