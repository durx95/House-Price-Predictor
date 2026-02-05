import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="House price predictor",page_icon="🏠",layout= "centered"
)
st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict the price")

# User inputs (example features)
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", min_value=300, max_value=5000, value=1500)
total_rooms = st.number_input("Total Rooms", min_value=2, max_value=15, value=6)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000)

# Input dataframe (VERY IMPORTANT: column names same hone chahiye)
input_data = pd.DataFrame({
    "OverallQual": [overall_qual],
    "GrLivArea": [gr_liv_area],
    "TotRmsAbvGrd": [total_rooms],
    "YearBuilt": [year_built]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: $ {prediction:,.0f}")