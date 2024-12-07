import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import plotly.graph_objects as go
import base64
from typing import Optional, Dict, Any
import numpy as np

# Cache the data loading to improve performance
@st.cache_data
def load_data() -> Optional[pd.DataFrame]:
    """Load and preprocess the museum data."""
    try:
        data_path = Path('data/Small Museum Data - Sheet1 (1).csv')
        df = pd.read_csv(data_path, skiprows=1, names=['Name', 'Nationality', 'Gender', 'Museum', 'SmallMuseum'])
        
        # Clean the data
        df = df.fillna('Unknown')
        df['Gender'] = df['Gender'].str.strip()
        df['Nationality'] = df['Nationality'].str.strip()
        
        return df
    except FileNotFoundError:
        st.error("⚠️ Data file not found. Please check if the file exists in the data directory.")
        return None
    except Exception as e:
        st.error(f"⚠️ Error loading data: {str(e)}")
        return None

@st.cache_data
def create_continent_map() -> Dict[str, str]:
    """Create mapping of nationalities to continents."""
    return {
        # North America
        "American": "North America",
        "African-American": "North America",
        "Native American": "North America",
        "Mexican": "North America",
        "Mexican-American": "North America",
        "Canadian": "North America",
        "Canadian-American": "North America",
        "Cuban": "North America",
        "Cuban-American": "North America",
        "Bahamian": "North America",
        "Haitian": "North America",
        "American-Haitian": "North America",
        "Dominican": "North America",
        
        # South America
        "Peruvian": "South America",
        "Brazilian": "South America",
        "Brazilian-American": "South America",
        "Venezuelan": "South America",
        "Colombian": "South America",
        
        # Europe
        "German": "Europe",
        "German-American": "Europe",
        "Irish-American": "Europe",
        "Italian": "Europe",
        "Italian-American": "Europe",
        "Dutch": "Europe",
        "Norwegian": "Europe",
        "Swedish": "Europe",
        "Danish": "Europe",
        "Finnish": "Europe",
        "Polish-Ukrainian": "Europe",
        "British": "Europe",
        "British-American": "Europe",
        "French": "Europe",
        "Icelandic-Danish": "Europe",
        "English": "Europe",
        
        # Africa
        "Nigerian": "Africa",
        "Ghanaian": "Africa",
        "Kenyan": "Africa",
        "Ugandan": "Africa",
        "Congolese": "Africa",
        "South African": "Africa",
        
        # Asia
        "Indian": "Asia",
        "Lebanese": "Asia",
        "Turkish": "Asia",
        "Chinese": "Asia",
        "Chinese-American": "Asia",
        "South Korean": "Asia",
        "Japanese": "Asia",
        "Korean": "Asia",
        "American-Korean": "Asia",
        "Palestinian-American": "Asia",
        "Singaporean": "Asia",
        "Asian-American": "Asia",
        
        # Oceania
        "Australian": "Oceania",
        
        # Multinational
        "Canadian-Ukrainian": "Multinational/Other",
        "Haitian Jamaican": "Multinational/Other",
    }

def create_pie_chart(data: pd.DataFrame, names: str, values: str, title: str) -> Optional[go.Figure]:
    """Create an enhanced pie chart with custom styling."""
    try:
        fig = px.pie(
            data,
            names=names,
            values=values,
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            width=800,
            height=600,
            margin=dict(t=30, l=0, r=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate="<b>%{label}</b><br>" +
                         "Count: %{value}<br>" +
                         "Percentage: %{percent}<extra></extra>"
        )
        
        return fig
    except Exception as e:
        st.error(f"⚠️ Error creating pie chart: {str(e)}")
        return None

def create_bar_chart(data: pd.DataFrame, x: str, y: str, title: str) -> Optional[go.Figure]:
    """Create an enhanced bar chart with custom styling."""
    try:
        fig = px.bar(
            data,
            x=x,
            y=y,
            title=title,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_layout(
            showlegend=False,
            xaxis_title="",
            yaxis_title="Count",
            width=800,
            height=600,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        
        return fig
    except Exception as e:
        st.error(f"⚠️ Error creating bar chart: {str(e)}")
        return None


def show_overview(df: pd.DataFrame):
    """Display overview statistics and metrics."""
    st.markdown("""
        <h1 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>
            Museum Artists Demographics Dashboard
        </h1>
    """, unsafe_allow_html=True)
    
    st.write("""
    This dashboard presents demographic information about artists represented in museums.
    Explore different aspects of the data using the tabs below.
    """)
    
    # Add shadow to metrics and set text color to white
    st.markdown("""
        <style>
        div.stMetric {
            background-color: rgba(0, 0, 0, 0.5) !important;
            padding: 15px !important;
            border-radius: 10px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3) !important;
        }
        
        div.stMetric label {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        }
        
        div.stMetric [data-testid="stMetricValue"] {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        }
        
        [data-testid="stMetricValue"] > div {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        }
        
        [data-testid="stMetricLabel"] > div {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Artists", len(df))
    with col2:
        st.metric("Museums Represented", df['Museum'].nunique())
    with col3:
        st.metric("Nationalities", df['Nationality'].nunique())
    
    st.divider()

def render_data_table(df: pd.DataFrame, title: str, height: int = 500):
    """Render a styled dataframe with consistent formatting."""
    st.markdown(f"""
    <div style="background-color: rgba(240, 242, 246, 0.1); padding: 10px; border-radius: 5px; margin-bottom: 10px">
        <h3 style="margin: 0; text-align: center; color: white;">{title}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.dataframe(
        df.style.format({'Count': '{:,.0f}'})
        .set_table_styles([
            {'selector': 'thead', 'props': [('position', 'sticky'), ('top', '0')]},
            {'selector': 'th', 'props': [('background-color', 'rgba(240, 242, 246, 0.1)')]}
        ]),
        height=height
    )

def main():
    # Page configuration
    st.set_page_config(
        page_title="Museum Demographics",
        layout="wide"
    )
    
    # Load background image
    try:
        image_path = Path('images/aaron douglas - song of the tower.jfif')
        with open(image_path, "rb") as f:
            img_data = f.read()
            b64_encoded = base64.b64encode(img_data).decode()
            st.markdown(generate_background_style(b64_encoded), unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Background image could not be loaded: {str(e)}")
    
    # Load and process data
    df = load_data()
    
    if df is not None:
        try:
            show_overview(df)
            
            # Create navigation tabs
            tabs = st.tabs([
                "Nationality",
                "Gender",
                "Continental",
                "Raw Data"
            ])
            
            # Nationality Distribution Tab
            with tabs[0]:
                st.markdown("<h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>Nationality Distribution</h2>", unsafe_allow_html=True)
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    nationality_counts = df['Nationality'].value_counts().reset_index()
                    nationality_counts.columns = ['Nationality', 'Count']
                    
                    min_count = st.number_input(
                        "Minimum count to display",
                        min_value=1,
                        value=1,
                        key="nationality_filter"
                    )
                    
                    filtered_nationality = nationality_counts[
                        nationality_counts['Count'] >= min_count
                    ]
                    
                    fig = create_pie_chart(
                        filtered_nationality,
                        'Nationality',
                        'Count',
                        'Artist Nationality Distribution'
                    )
                    if fig:
                        st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    render_data_table(nationality_counts, "Nationality Data")
            
            # Gender Distribution Tab
            with tabs[1]:
                st.markdown("<h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>Gender Distribution</h2>", unsafe_allow_html=True)
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    gender_counts = df['Gender'].value_counts().reset_index()
                    gender_counts.columns = ['Gender', 'Count']
                    
                    fig = create_pie_chart(
                        gender_counts,
                        'Gender',
                        'Count',
                        'Artist Gender Distribution'
                    )
                    if fig:
                        st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    render_data_table(gender_counts, "Gender Data")
            
            # Continental Distribution Tab
            with tabs[2]:
                st.markdown("<h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>Continental Distribution</h2>", unsafe_allow_html=True)
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    df['Continent'] = df['Nationality'].map(create_continent_map())
                    continent_counts = df['Continent'].value_counts().reset_index()
                    continent_counts.columns = ['Continent', 'Count']
                    
                    fig = create_pie_chart(
                        continent_counts,
                        'Continent',
                        'Count',
                        'Artist Distribution by Continent'
                    )
                    if fig:
                        st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    render_data_table(continent_counts, "Continental Data")
            
            # Raw Data Tab
            with tabs[3]:
                st.markdown("<h2 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>Raw Data</h2>", unsafe_allow_html=True)
                search = st.text_input("Search artists by name or nationality")
                if search:
                    filtered_df = df[
                        df['Name'].str.contains(search, case=False) |
                        df['Nationality'].str.contains(search, case=False)
                    ]
                else:
                    filtered_df = df
                st.dataframe(filtered_df, height=600)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Please check your data format and contents.")

def generate_background_style(b64_encoded: str) -> str:
    """Generate CSS styles for the dashboard with enhanced accessibility."""
    return """
        <style>
        .stApp {
            background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(data:image/jfif;base64,""" + b64_encoded + """);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        
        /* Enhanced text visibility */
        .stMarkdown, .stMarkdown p, .stMarkdown li {
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            line-height: 1.6 !important;
        }
        
        /* Headers and text */
        h1, h2, h3, .subheader {
            color: rgb(255, 255, 255) !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-weight: 700 !important;
        }
        
        /* Content sections */
        .content-section {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 25px;
            border-radius: 10px;
            margin: 15px 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Metrics styling */
        div.stMetric {
            background-color: rgba(0, 0, 0, 0.7) !important;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        div.stMetric label,
        div.stMetric [data-testid="stMetricValue"],
        div.stMetric [data-testid="stMetricDelta"],
        div.stMetric [data-testid="stMetricLabel"] {
            color: rgb(255, 255, 255) !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
            font-weight: 600 !important;
        }
        
        /* Interactive elements */
        .streamlit-expanderHeader, div.stAlert {
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: rgb(255, 255, 255) !important;
        }
        
        /* Form elements */
        div.stSlider label, 
        div.stCheckbox label,
        div.stTextInput label {
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }
        
        /* Charts and dataframes */
        .js-plotly-plot {
            background-color: rgba(255, 255, 255, 0.98) !important;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .dataframe {
            background-color: rgba(255, 255, 255, 0.98) !important;
            border-radius: 10px;
        }
        
        /* Info boxes */
        div.stAlert {
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: rgb(255, 255, 255) !important;
            border: 2px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px;
            padding: 1.2rem;
            margin: 1.2rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        
        div.stAlert p {
            color: rgb(255, 255, 255) !important;
            font-weight: 500 !important;
        }
        
        /* Bullet points and lists */
        .stMarkdown ul li::marker {
            color: rgb(255, 255, 255) !important;
        }
        
        .stMarkdown ul, .stMarkdown ol {
            padding-left: 20px;
        }
        </style>
        """

if __name__ == "__main__":
    main()