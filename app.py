import os

from helper import *

import streamlit as st
from PIL import Image

# Markdown with description of app
st.write("""
# Cat and Dog Computer Vision App
Upload a file and my model will try to predict whether it is a cat or a dog
""")
st.write('---')

# Function that will save uploaded image to static/images folder
def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('static/images',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1    
    except Exception as e:
        print(e)
        return 

# Creates button to upload file
uploaded_file = st.file_uploader("Upload Image")

if st.button("Predict"):
    if uploaded_file is not None:
        if save_uploaded_file(uploaded_file):
            # Display the image
            display_image = Image.open(uploaded_file)
            st.image(display_image)

            # Get model prediction of uploaded image
            prediction = predict_catdog(os.path.join('static/images',uploaded_file.name))

            # Remove image after prediction is done
            os.remove(os.path.join('static/images',uploaded_file.name))

            # Display results
            if prediction == 1:
                st.write("""
                ## My model thinks your picture is a...
                # DOG
                """)
            elif prediction == 0:
                st.write("""
                ## My model thinks your picture is a...
                # Cat
                """)
            else:
                st.write("""
                ## Please upload an image
                """)
        else:
            st.write("## There was a problem uploading your file")

