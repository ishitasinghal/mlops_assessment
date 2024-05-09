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


# fastapi
import fastapi
import gradio_client
from pydantic import BaseModel
app = fastapi.FastAPI()

class Image(BaseModel):
    url: str

@app.post("/predict")
def predict(image: Image):
    client = gradio_client.Client("http://192.168.1.206:31238/")
    result = client.predict(
            image= gradio_client.file(image.url),
            api_name="/predict"
    )
    return result
    return image.url

def run_uvicorn_app():
    uvicorn.run(app, host="0.0.0.0", port=5000)
    print("Server is running on http://0.0.0.0:5000")

if __name__ == "__main__":
    import uvicorn
    import threading
    threading.Thread(target=run_uvicorn_app).start()
    iface.launch(server_name="0.0.0.0")
