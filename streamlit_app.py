import streamlit as st
import requests

st.title("🌦 Weather App")
st.write("Heelo")

city = st.text_input("Enter City Name")

API_KEY = "4d3a1522de33d815285ebc73b0f3441b"

if st.button("Get Weather"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        st.success(f"Temperature: {temp} °C")
        st.info(f"Humidity: {humidity}%")
        st.write(f"Weather: {weather}")
        
    else:

        st.error("City not found")
