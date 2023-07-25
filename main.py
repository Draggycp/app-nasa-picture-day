import requests
import streamlit as st

# Sets the API key and the URL
api_key = "iiDbo2adc8IDbc7MlGjmjeRGHxeFcTybOIBzMxYR"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Requests the content and data from the URL
request = requests.get(url)
content = request.json()

# Sets the variables for each content
title = content["title"]
image_url = content["hdurl"]
explanation = content["explanation"]

# Saves the image from the website
image_filepath = "img.png"
image_data = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(image_data.content)

# Shows the information that was setup above
st.header(title)

st.image(image_filepath)

st.write(explanation)