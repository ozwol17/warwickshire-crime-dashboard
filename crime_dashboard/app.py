import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("📊 Warwickshire Crime Dashboard")
st.markdown("---")

# Define base directory where images are stored
img_path = "crime_dashboard"

st.header("1. Monthly Trends of Top 5 Crime Types")
st.image(os.path.join(img_path, "figure1.png"), use_container_width=True)

st.header("2. Top 20 Locations with Most Crimes")
st.image(os.path.join(img_path, "figure2.png"), use_container_width=True)

st.header("3. Crime Type Distributions in Parking Areas")
st.image(os.path.join(img_path, "figure3.png"), use_container_width=True)

st.header("4. Monthly Crime Trends in Parking Areas")
st.image(os.path.join(img_path, "figure4.png"), use_container_width=True)

st.header("5. Monthly Crime Counts by Type")
st.image(os.path.join(img_path, "figure5.png"), use_container_width=True)

st.header("6. Boxplot of Monthly Crime Counts by Type")
st.image(os.path.join(img_path, "figure6.png"), use_container_width=True)

st.header("7. Total Crime Count by Type")
st.image(os.path.join(img_path, "figure7.png"), use_container_width=True)

st.header("8. Confusion Matrix of XGBoost Classifier")
st.image(os.path.join(img_path, "figure8.png"), use_container_width=True)
