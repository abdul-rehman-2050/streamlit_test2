import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Set the title of the web app
st.title('Image Processing with Streamlit')

# Add some text
st.write('Welcome to this simple image processing app!')

# Upload Image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Read the uploaded image
    image_bytes = uploaded_image.read()
    image_array = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_array, 1)

    # Resize the image to 220x220
    resized_image = cv2.resize(image, (220, 220))

    # Convert the resized image to grayscale
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(grayscale_image, threshold1=100, threshold2=200)

    # Display the uploaded image
    st.image(resized_image, channels="BGR", caption="Uploaded Image (Resized to 220x220)")

    # Display the Canny edge-detected image
    st.image(edges, caption="Canny Edge Detection Result")
