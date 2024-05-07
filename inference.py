#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# In[3]:


model = tf.keras.models.load_model('my-model.h5')


# In[4]:


image_number = 1
# print(os.path.isfile(f"digits/digit3.png"))
while os.path.isfile(f"digits/{image_number}.png"):
    try:
        img = cv2.imread(f"digits/{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"The number is probably: {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    image_number += 1

