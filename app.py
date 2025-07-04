import streamlit as st
import joblib
import pandas as pd
import base64

# load model and files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")
columns = joblib.load("columns.pkl")

# Custom CSS for background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html = True
    )
add_bg_from_local('bato-damdinov-ewqR2xI1apk-unsplash.jpg')

# UI
st.image("abigail-lynn-9y8c_YDUrYA-unsplash.jpg", use_container_width = True)
st.set_page_config(page_title = "Crop Recommendation", layout = "centered")
st.title("🌾 Crop Recommendation")
st.markdown("<h4 style='text-align: center;'>Get the best crop suggestion based on soil and climate conditions</h4>", unsafe_allow_html = True)


# input
nitrogen = st.number_input('Nitrogen (N)')
phosphorus = st.number_input('Phosphorus (P)')
potassium = st.number_input('Potassium (K)')
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)')
ph = st.number_input('pH Level')
rainfall = st.number_input('Rainfall (mm)')

# dataframe
input_df = pd.DataFrame({
    "N": [nitrogen],
    "P": [phosphorus],
    "K": [potassium],
    "temperature": [temperature],
    "humidity": [humidity],
    "ph": [ph],
    "rainfall": [rainfall]
})

# input scaling
input_scaled = scaler.transform(input_df)

# predictions
if st.button("Recommend Crop"):
    crop = model.predict(input_scaled)[0] # predict
    crop_name = encoder.inverse_transform([crop])[0]  # Decoding from encoder
    st.markdown(f"""
        <div style='background-color: #e8f5e9; padding: 20px; border-radius: 10px; border: 2px solid #4caf50;'>
            <h3 style='text-align: center; color: #2e7d32;'>--- Recommended Crop ---</h3>
            <h1 style='text-align: center; color: #1b5e20;'>🌾: {crop_name}</h1>
        </div>
    """, unsafe_allow_html = True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with Streamlit by <b>thetensorcraft</b></p>", unsafe_allow_html = True)
