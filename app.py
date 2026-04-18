import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Delhi AQI Prediction App")

pm25 = st.slider("PM2.5", 0, 500)
pm10 = st.slider("PM10", 0, 500)
no2 = st.slider("NO2", 0, 200)
so2 = st.slider("SO2", 0, 200)
co = st.slider("CO", 0.0, 10.0)
o3 = st.slider("O3", 0, 200)

if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(input_data)

    st.success(f"Predicted AQI: {prediction[0]:.2f}")