# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import requests
import json

st.image('https://i.ibb.co/RGmb4FKk/1781072041102.png', width=200)

st.title('Weather App')

city = st.text_input('Enter city name')

if city:
    try:
        url = f'http://wttr.in/{city}?format=j1'
        response = requests.get(url)
        data = json.loads(response.text)
        current_condition = data['current_condition'][0]
        st.write(f'Current temperature: {current_condition["temp_C"]}°C')
        st.write(f'Humidity: {current_condition["humidity"]}%')
        st.write(f'Weather conditions: {current_condition["weatherDesc"][0]["value"]}')
    except Exception as e:
        st.error('City not found')

st.markdown('Made with GrishteSync | Suryasticsai | <a href="https://suryasticsai.github.io/GrishteSync">https://suryasticsai.github.io/GrishteSync</a>')