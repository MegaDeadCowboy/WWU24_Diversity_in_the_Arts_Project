import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from pathlib import Path

def add_bg_from_local(image_file):
    # Convert string path to Path object and resolve it
    image_path = Path(image_file).resolve()
    
    try:
        with open(image_path, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        return f'''
        <style>
        .stApp {{
            background-image: url(data:image/jfif;base64,{b64_encoded});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        /* Style for title */
        h1 {{
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 30px !important;
        }}
        </style>
        '''
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return ""

def run():
    # Page configuration
    st.set_page_config(
        page_icon=":grey_exclamation:",
    )
    
    # Add background image - Using raw string for path
    image_path = r"images\aaron douglas - from slavery to recognition.jfif"
    st.markdown(add_bg_from_local(image_path), unsafe_allow_html=True)

    # Page header
    st.title("About")

    # Custom CSS for clean typography and better text visibility
    st.markdown("""
        <style>
        .about-text {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #333333;
            padding: 1em 0;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
        }
        .streamlit-container h1 {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Mission statement
    st.markdown("""<div class='about-text'>
    Our mission is to illuminate and address systemic inequities in the art world through the power of data science. We meticulously collect and analyze data from museums and publications to quantify representation gaps and bring transparency to the art establishment. By tracking key metrics—from the demographic composition of exhibited artists to visitor attendance patterns and institutional mission statements—we aim to create a comprehensive picture of how people of color are represented in and experience arts institutions. Our work transforms raw data into actionable insights, enabling cultural institutions to recognize blind spots and make informed decisions toward creating a more inclusive and equitable art world.
    </div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    run()