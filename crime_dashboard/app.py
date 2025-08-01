import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 Warwickshire Crime Dashboard")
st.markdown("---")

st.header("1. Monthly Trends of Top 5 Crime Types")
st.image("top_5_crime_types.png", use_container_width=True)

st.header("2. Top 20 Locations with Most Crimes")
st.image("top_20_locations_with_most_crimes.png", use_container_width=True)

st.header("3. Confusion Matrix for Model Performance")
st.image("confusion_matrix.png", use_container_width=True)

st.header("4. Total Crime Count by Type")
st.image("total_crime_count.png", use_container_width=True)

st.header("5. Boxplot of Monthly Crime Counts")
st.image("boxplot.png", use_container_width=True)

st.header("6. Monthly Crime Counts by Type")
st.image("monthly_crime_counts_by_type.png", use_container_width=True)

st.header("7. Monthly Crime Trends by Crime Type")
st.image("monthly_crime_type_in.png", use_container_width=True)

st.header("8. Crime Type Distributions")
st.image("crime_type_distributions.png", use_container_width=True)
