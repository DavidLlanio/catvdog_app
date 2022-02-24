import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array

current_path = os.getcwd()

# Load the catdog model
model = load_model(os.path.join(current_path, "static/catdog_model"))

def predict_catdog(img_path):
    
    img = load_img(img_path, target_size=(150,150))
    img = img_to_array(img)
    img = np.expand_dims(img,axis = 0)

    prediction = int(model.predict(img))

    return prediction
