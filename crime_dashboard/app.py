import streamlit as st
import os

# Basic layout and page title
st.set_page_config(layout="wide", page_title="Warwickshire Crime Dashboard")
st.title("📊 Warwickshire Crime Dashboard")

# Intro panel (public-facing, plain English, purpose, scope, source)
st.markdown(
    "This dashboard uses Warwickshire Police data from May 2022 to April 2025. "
    "It shows local crime patterns and a simple predictive model. "
    "The aim is to make trends easy to understand for the public and local media."
)
st.markdown("---")

# Optional sidebar with simple guidance (no technical jargon)
st.sidebar.header("About")
st.sidebar.info(
    "Designed for the general public and local media. "
    "Each section has a short caption that explains what the chart shows."
)

# Base folder for exported images used in the report
IMG_DIR = "crime_dashboard"

# Helper to render a header, image, and caption in one place
def render_figure(num: int, title: str, filename: str, caption: str):
    st.header(f"{num}. {title}")
    st.image(os.path.join(IMG_DIR, filename), use_container_width=True)
    st.caption(caption)

# 1. Monthly trends of top 5 crime types
render_figure(
    1,
    "Monthly Trends of Top 5 Crime Types",
    "figure1.png",
    "Shows how the five most common crime types changed each month."
)

# 2. Top 20 locations with most crimes
render_figure(
    2,
    "Top 20 Locations with Most Crimes",
    "figure2.png",
    "Highlights the Warwickshire locations with the highest total number of reported crimes. "
    "Location names were cleaned to remove duplicates and vague entries."
)

# 3. Crime type distributions in parking areas
render_figure(
    3,
    "Crime Type Distributions in Parking Areas",
    "figure3.png",
    "Shows which crime types are most common in parking areas."
)

# 4. Monthly crime trends in parking areas
render_figure(
    4,
    "Monthly Crime Trends in Parking Areas",
    "figure4.png",
    "Shows how different crime types in parking areas change across months. "
    "Useful for spotting seasonal patterns."
)

# 5. Monthly crime counts by type
render_figure(
    5,
    "Monthly Crime Counts by Type",
    "figure5.png",
    "Compares the number of reported crimes by category for each month."
)

# 6. Boxplot of monthly crime counts by type
render_figure(
    6,
    "Boxplot of Monthly Crime Counts by Type",
    "figure6.png",
    "Summarises variation in monthly crime counts across types. Wider boxes mean more fluctuation."
)

# 7. Total crime count by type
render_figure(
    7,
    "Total Crime Count by Type",
    "figure7.png",
    "Ranks crime types by overall totals for the full period."
)

# 8. Model prediction results (confusion matrix)
st.header("8. Model Prediction Results (XGBoost)")
st.image(os.path.join(IMG_DIR, "figure8.png"), use_container_width=True)
st.caption(
    "Compares the model predictions with the actual crime types. "
    "Darker colours mean more cases and lighter colours mean fewer cases. "
    "Overall accuracy is about 37.8 percent."
)

# Footer with sources and alignment reminder
st.markdown("---")
st.markdown(
    "Source: Warwickshire Police. Dataset provided by the University of East Anglia. "
    "Period covered: May 2022 to April 2025. "
    "Built in Python and deployed with Streamlit."
)
st.caption(
    "The dashboard matches the figures and wording used in the written report to keep a one to one alignment."
)
