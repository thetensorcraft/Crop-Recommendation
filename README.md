# 🌾 Crop Recommendation System

A simple yet powerful **Machine Learning Web App** built with **Streamlit** that recommends the most suitable crop based on soil and climate conditions. This app is designed to assist farmers and agriculturists in making informed decisions for better yield and sustainability.

---

## 🚀 Features
- Predicts the **best crop** using key features:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH Level
  - Rainfall (mm)
- Beautifully designed **interactive web app** using Streamlit
- Scaled inputs and **trained ML model** with high accuracy
- Stylish UI with background image and result display

---

## 📊 Model Details
- Algorithm: Naive Bayes
- Accuracy: ~ 98-99% on test set
- Cross Validation: Accuracy ~ 98-99, Std ~ 0.15
- Dataset: https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset

---

## 🛠️ Technologies Used
- **Python 3** (Programming Language)
- **Scikit-learn** (Model Building & Scaling)
- **Streamlit** (Web App Development)
- **Pandas & Numpy** (Data Manipulation)
- **Joblib** (Model Serialization)

---
## 🚀 Live Test
Link: http://thetensorcraft-crop-recommendation.streamlit.app/

---
## 📦 How to Run Locally

1. Clone the repository:
    ```bash
   git clone https://github.com/thetensorcraft/Crop-Recommendation.git
   cd Crop-Recommendation
    bash```

2. Install required packages:
    ```bash
    uv init
    uv venv --python 3.13.0
    uv install -r requirements.txt
    bash```

3. Run the app
    ```bash
    uv run streamlit run app.py
    bash```
