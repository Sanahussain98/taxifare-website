import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
This is a simple web interface to predict **Taxi Fares** 💸

You can enter ride details and get a fare prediction from an API.
''')

'''
## Enter ride details
'''

# 1️⃣ Date and time
date = st.date_input("Pickup date")
time = st.time_input("Pickup time")

# 2️⃣ Pickup longitude and latitude
pickup_longitude = st.number_input("Pickup longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup latitude", value=40.748817)

# 3️⃣ Dropoff longitude and latitude
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.748817)

# 4️⃣ Passenger count
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=1)

# Combine date and time into one datetime string
pickup_datetime = datetime.combine(date, time)

# API URL (Le Wagon’s default)
url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Using Le Wagon’s public API.')

'''
## Call the API
'''

# Build the parameters dictionary
params = {
    "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# Button to trigger API call
if st.button('Get fare prediction 💰'):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Predicted fare: ${round(prediction['fare'], 2)}")
    else:
        st.error(f"Error from API: {response.status_code}")


import pandas as pd
df = pd.DataFrame({'lat':[pickup_latitude], 'lon':[pickup_longitude]})
st.map(df)
