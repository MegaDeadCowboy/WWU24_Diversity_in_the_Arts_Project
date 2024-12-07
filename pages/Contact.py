import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_icon=":speech_balloon:",
)


def add_bg_from_local(image_file):
    try:
        image_path = Path(image_file).resolve()
        with open(image_path, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        
        return f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(data:image/jfif;base64,{b64_encoded});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Enhanced text visibility */
        .stMarkdown, .stMarkdown p, .stMarkdown li {{
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            line-height: 1.6 !important;
        }}
        
        /* Headers and text */
        h1, h2, h3, .subheader, .stCaption {{
            color: rgb(255, 255, 255) !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-weight: 700 !important;
        }}
        
        /* Team member cards */
        .team-member-card {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
        }}
        
        /* Image containers */
        .stImage {{
            border-radius: 10px;
            border: 2px solid rgba(255, 255, 255, 0.2);
            overflow: hidden;
        }}
        
        /* Social icons container */
        .social-icons {{
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }}
        
        /* Social icons */
        .social-icons img {{
            transition: transform 0.2s;
        }}
        
        .social-icons img:hover {{
            transform: scale(1.1);
        }}
        
        /* Caption styling */
        .stCaption {{
            font-size: 1rem !important;
            opacity: 0.9;
            margin: 8px 0;
        }}
        </style>
        """
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return ""


# Add background image
image_path = r"images/aaron douglas - song of the tower.jfif"  # Update this path to match your image location
st.markdown(add_bg_from_local(image_path), unsafe_allow_html=True)

st.title("Get in Touch")
st.write("Questions, ideas, or just want to connect? Reach out through our socials or email—we’d love to hear from you! Check out our contact info and photos below. Looking forward to connecting!")

# Team member dictionary with relevant information
team_members = [
    {
        "name": "Takira Boltman",
        "major": "Data Science",
        "minor": "Mathematics",
        "linkedin": "https://www.linkedin.com/in/takira-boltman",
        "email": "boltmat@wwu.edu"
    },
    {
        "name": "Maddie Knappenberger",
        "major": "Data Science",
        "minor": "Mathematics",
        "linkedin": "https://www.linkedin.com/in/maddie-knappenberger",
        "email": "knappem@wwu.edu"
    },
    {
        "name": "Carver Rasmussen",
        "major": "Data Science",
        "minor": "Mathematics",
        "linkedin": "https://www.linkedin.com/in/carver-rasmussen",
        "email": "rasmusa4@wwu.edu"
    },
    {
        "name": "Theron Hamlin",
        "major": "Data Science",
        "minor": "Mathematics",
        "linkedin": "https://www.linkedin.com/in/theron-hamlin-3246a3239/",
        "email": "hamlint2@wwu.edu"
    },
    {
        "name": "Abigail Gedney",
        "major": "Data Science",
        "minor": "Mathematics",
        "linkedin": "https://www.linkedin.com/in/abigail-gedney-856120303/",
        "email": "gedneya@wwu.edu"
    },
    {
        "name": "Dr. Monique Kerman",
        "role": "Professor of Fine Arts, African Studies",
        "linkedin": "https://www.linkedin.com/in/monique-kerman-24349464/",
        "email": "fowlerm6@wwu.edu"
    }
]

# Temporary placeholder image variable
placeholder_image = "images/placeholder.png"

# Updated display_member function with better styling
def display_member(member):
    with st.container():
        st.markdown("""
            <div class="team-member-card">
        """, unsafe_allow_html=True)
        
        st.subheader(member["name"])
        st.image(placeholder_image, width=200)
        
        if "major" in member and "minor" in member:
            st.caption(f"{member['major']} Major, {member['minor']} Minor")
        elif "role" in member:
            st.caption(member["role"])
        
        st.markdown(
            f"""
            <div class="social-icons">
                <a href="{member['linkedin']}" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="24">
                </a> &nbsp;
                <a href="mailto:{member['email']}">
                    <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" width="24">
                </a>
            </div>
            """, unsafe_allow_html=True
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

# Display team members in a 2-column layout
for i in range(0, len(team_members), 2):
    cols = st.columns(2)
    
    with cols[0]:
        display_member(team_members[i])
    
    if i + 1 < len(team_members):
        with cols[1]:
            display_member(team_members[i + 1])
    
    st.markdown("<br>", unsafe_allow_html=True)