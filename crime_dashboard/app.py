import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 Warwickshire Crime Dashboard")
st.markdown("---")

st.header("1. Monthly Trends of Top 5 Crime Types")
st.image("top 5 crime types.png", use_column_width=True)

st.header("2. Top 20 Locations with Most Crimes")
st.image("top 20 locations with most crimes.png", use_column_width=True)

st.header("3. Confusion Matrix for Model Performance")
st.image("confusion matrix.png", use_column_width=True)

st.header("4. Total Crime Count by Type")
st.image("total crime count.png", use_column_width=True)

st.header("5. Boxplot of Monthly Crime Counts")
st.image("boxplot.png", use_column_width=True)

st.header("6. Monthly Crime Counts by Type")
st.image("monthly crime counts by type.png", use_column_width=True)

st.header("7. Monthly Crime Trends by Crime Type")
st.image("monthly crime type in.png", use_column_width=True)

st.header("8. Crime Type Distributions")
st.image("crime type distributions.png", use_column_width=True)
