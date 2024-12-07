import streamlit as st
from pathlib import Path
import base64

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
        
        /* Brighten all text */
        .stMarkdown, .stMarkdown p, .stMarkdown li {{
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            line-height: 1.6 !important;
        }}
        
        /* Style for headers and text */
        h1, h2, h3, .subheader {{
            color: rgb(255, 255, 255) !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-weight: 700 !important;
        }}
        
        /* Style for tab content */
        .tab-content {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }}
        
        /* Style for introduction text */
        .intro-text {{
            color: rgb(255, 255, 255) !important;
            font-size: 1.2em !important;
            font-weight: 600 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            margin-bottom: 20px;
            line-height: 1.6;
        }}
        
        /* Style for call-to-action section */
        .cta-section {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            color: rgb(255, 255, 255) !important;
        }}
        
        .cta-section h3, .cta-section li {{
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
        }}
        
        /* Make tab labels more visible */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 4px;
            padding: 4px 8px;
            color: #333333;
            font-weight: 500;
        }}
        
        .stTabs [aria-selected="true"] {{
            background-color: rgba(255, 255, 255, 1);
            font-weight: bold;
        }}

        /* Bullet points and lists */
        .stMarkdown ul li::marker {{
            color: rgb(255, 255, 255) !important;
        }}
        
        .stMarkdown ul, .stMarkdown ol {{
            padding-left: 20px;
        }}
        </style>
        """
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return ""

def main():
    st.set_page_config(
        page_title="Solutions for Improved Transparency",
        page_icon="🏛️",
        layout="wide"
    )

    # Add background image
    image_path = r"images\aaron douglas - song of the tower.jfif"
    st.markdown(add_bg_from_local(image_path), unsafe_allow_html=True)

    st.title("Museum Diversity Transparency Framework")
    st.markdown("""<p class="subheader">A Guide for Fine Art Museums</p>""", unsafe_allow_html=True)

    # Introduction with custom styling
    st.markdown("""
    <div class="intro-text">
    This framework provides comprehensive guidelines for fine art museums to enhance transparency 
    around racial diversity in their collections, exhibitions, and operations. It offers practical 
    steps and metrics to help institutions better track, report, and improve their diversity initiatives.
    </div>
    """, unsafe_allow_html=True)

    # Main sections in tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Data Collection & Metrics", 
        "Reporting & Goals",
        "Community & Implementation",
        "Measurement & Improvement"
    ])

    with tab1:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.header("Data Collection & Metrics")
        
        st.subheader("Artist Demographics")
        st.markdown("""
        - Track and publish data on racial and ethnic background
        - Document geographic origin of artists
        - Monitor representation in permanent collections
        - Track temporary exhibition statistics
        - Maintain historical baseline data
        - Document year-over-year changes
        """)

        st.subheader("Acquisition Metrics")
        st.markdown("""
        - Record annual acquisition demographics
        - Monitor purchasing budgets for artists of color
        - Track primary vs. secondary market acquisitions
        - Document donation demographics
        """)

        st.subheader("Exhibition Data")
        st.markdown("""
        - Monitor solo exhibition demographics
        - Track group exhibition representation
        - Document prominent placement statistics
        - Record exhibition duration and resources
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.header("Reporting & Goal Setting")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Public Reporting")
            st.markdown("""
            - Annual diversity reports
            - Quarterly progress updates
            - Year-over-year comparisons
            - Public-facing databases
            """)
        
        with col2:
            st.subheader("Goals & Accountability")
            st.markdown("""
            - Specific diversity targets
            - Timeline-based objectives
            - Department-specific goals
            - Success metrics
            - Oversight committee
            - External review board
            - Third-party audits
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.header("Community Engagement & Implementation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Community Involvement")
            st.markdown("""
            - Community advisory boards
            - Public comment periods
            - Regular community forums
            - Educational programs
            - Curriculum development
            - Docent training
            - Educational partnerships
            """)
        
        with col2:
            st.subheader("Implementation Strategy")
            st.markdown("""
            - Diversity database creation
            - Tracking software implementation
            - Staff training programs
            - Documentation protocols
            - Budget allocation
            - Technology infrastructure
            - Ongoing funding mechanisms
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="tab-content">', unsafe_allow_html=True)
        st.header("Measurement & Continuous Improvement")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Progress Measurement")
            st.markdown("""
            - Key performance indicators
            - Benchmark comparisons
            - Progress scorecards
            - Regular assessments
            - Community response metrics
            - Media coverage tracking
            - Visitor demographics
            - Impact assessment
            """)
        
        with col2:
            st.subheader("Continuous Improvement")
            st.markdown("""
            - Annual framework review
            - Metric updates
            - Goal revision
            - Demographic adaptation
            - Initiative sharing
            - Network participation
            - Industry standard contribution
            - Case study documentation
            """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Call-to-action with custom styling
    st.markdown("""
    <div class="cta-section">
    <h3>Getting Started</h3>
    Museums interested in implementing this framework should begin by:
    <ol>
        <li>Assessing current data collection capabilities</li>
        <li>Establishing baseline metrics</li>
        <li>Setting initial goals</li>
        <li>Engaging with community stakeholders</li>
    </ol>
    For more information or implementation support, please contact our team.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()