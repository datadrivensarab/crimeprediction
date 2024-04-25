import streamlit as st
from predict import show_predict_page

# def main():
    
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
