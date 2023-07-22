import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the web app
st.title('Basic Streamlit App')

# Add some text
st.write('Welcome to this simple Streamlit app!')

# Generate some random data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a DataFrame with the data
data = pd.DataFrame({'x': x, 'y': y})

# Display the data table
st.write('Data Table:')
st.dataframe(data)

# Plot the data using matplotlib
st.write('Data Plot:')
plt.plot(x, y)
st.pyplot()

# Add a footer with some additional text
st.write('This is a basic example of a Streamlit app.')
st.write('Feel free to modify and extend it for your own projects!')
