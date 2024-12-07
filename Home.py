import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

def add_bg_from_local(image_file):
    try:
        image_path = Path(image_file).resolve()
        with open(image_path, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        
        # Simplified CSS without gradient overlay
        return f'''
        <style>
        .stApp {{
            background-image: url(data:image/jfif;base64,{b64_encoded});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Style for main text content */
        .main-text {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
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

# Page configuration
st.set_page_config(
    page_icon=":sparkles:",
)

# Add background image
image_path = Path("images") / "aaron douglas - from slavery to recognition.jfif"
st.markdown(add_bg_from_local(image_path), unsafe_allow_html=True)

# Center the title
st.markdown(
    """
    <h1 style="text-align: center;">Welcome to our Project!</h1>
    """, 
    unsafe_allow_html=True
)

# Add a break in between title and JS
st.markdown("<br>", unsafe_allow_html=True)

# Importing the TypeIt JS library with updated styling
typeit_html = """
    <div style="text-align: center; font-size: 24px; font-family: Arial, sans-serif; color: white; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">
        <span id="typeit-text"></span>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/typeit@8.0.7/dist/index.umd.js"></script>
    <script>
        new TypeIt("#typeit-text", {
            strings: ["An In-Depth Data Analysis by Students of WWU", "Explore Our Insights on Inclusivity", "Discovering Trends in Art Representation"],
            speed: 50,
            breakLines: false,
            loop: true
        }).go();
    </script>
"""

# Render the typing animation
components.html(typeit_html, height=100)

# Main content of page with styling
st.markdown("""
    <div class="main-text">
    We're using data to see if big art institutions are walking the talk on inclusivity since the Black Lives Matter movement. From artist representation to mission statements, and comparing trends with smaller museums, we're breaking down what progress (or gaps) really look like. Check out About for our mission, Research for the process, Findings for the story in the data, and Contact to reach out. Let's dive in!
    </div>
    """, 
    unsafe_allow_html=True)