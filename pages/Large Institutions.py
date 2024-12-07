import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Museum Collections Analysis",
    page_icon="🎨",
    layout="wide"
)

# Title and introduction
st.title("Museum Collections Analysis Dashboard")
st.markdown("""
This dashboard analyzes artist diversity across the Museum of Modern Art (MoMA) and smaller museums,
combining data from MoMA's public dataset and hand-collected data from smaller institutions.
""")

# Methodology Section - Placed at the top for context
with st.expander("📚 Methodology", expanded=False):
    st.markdown("""
    ### Project Overview
    This analysis combines the MoMA Artists dataset with data from smaller museums, focusing on artist 
    diversity and institutional representation. The data comes from two main sources:
    
    1. **MoMA Collection Data**
       - Sourced from [MoMA's GitHub Repository](https://github.com/MuseumofModernArt/collection)
       - Includes comprehensive artist and artwork information
    
    2. **Smaller Museums Dataset**
       - Hand-collected by Abigail Gedney at Western Washington University
       - Features currently displayed artists
       - Includes self-distinguished ethnicities from artists' personal websites/portfolios
    
    ### Data Processing Steps
    1. Downloaded and preprocessed MoMA data
    2. Cleaned and standardized artist names and dates
    3. Integrated hand-collected smaller museum data
    4. Merged datasets while maintaining institutional attribution
    
    ### Analysis Goals
    - Examine artist diversity across institutions
    - Compare representation in major vs. smaller museums
    - Track changes in artist diversity over time
    """)

# Load data
@st.cache_data
def load_data():
    try:
        # Use Path to create cross-platform compatible path
        data_path = Path('data') / 'combinedSmallandLargeFinal.csv'
        df = pd.read_csv(data_path)
        return df
    except FileNotFoundError:
        st.error("Error: Could not find the dataset file. Please check if 'combinedSmallandLargeFinal.csv' exists in the data directory.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

df = load_data()

if df is not None:
    # Create tabs for different analyses
    tab1, tab2, tab3 = st.tabs([
        "Nationality Distribution", 
        "African Representation",
        "Historical Trends"
    ])
    
    with tab1:
        # Nationality Analysis
        nationality_counts = df['Nationality'].value_counts().head(20)
        nationality_df = nationality_counts.reset_index()
        nationality_df.columns = ['Nationality', 'Count']
        
        fig_nationality = px.bar(nationality_df, 
                     x='Count', 
                     y='Nationality',
                     orientation='h',
                     title='Top 20 Nationality Counts in the Museum of Modern Art',
                     color='Count',
                     color_continuous_scale='viridis')
        
        fig_nationality.update_layout(
            showlegend=False,
            xaxis_title="Count",
            yaxis_title="Nationality",
            yaxis={'categoryorder':'total ascending'},
            margin=dict(l=20, r=20, t=40, b=20),
        )
        
        st.plotly_chart(fig_nationality, use_container_width=True)
    
    with tab2:
        # African Representation Analysis
        african_df = df[
            df['Ethnicity'].str.contains('African', na=False) |
            df['Nationality'].str.contains('African', na=False)
        ]

        # Calculate total number of artists
        total_artists = len(df)
        african_count = len(african_df)
        non_african_count = total_artists - african_count

        # Create pie chart with absolute values
        fig_african = go.Figure(data=[go.Pie(
            labels=['African', 'Non-African'],
            values=[african_count, non_african_count],
            hole=0.3,
            marker_colors=['lightcoral', 'skyblue'],
            texttemplate="%{label}<br>%{value:,} (%{percent})",
            hovertemplate="<b>%{label}</b><br>" +
                         "Count: %{value:,}<br>" +
                         "Percentage: %{percent}<extra></extra>"
        )])

        fig_african.update_layout(
            title={
                'text': 'African Representation in Museum Collections',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            )
        )

        st.plotly_chart(fig_african, use_container_width=True)

        # Display actual numbers
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Representation Statistics")
            st.markdown(f"""
            - Total Artists: {total_artists:,}
            - African Artists: {african_count:,} ({african_count/total_artists:.2%})
            - Non-African Artists: {non_african_count:,} ({non_african_count/total_artists:.2%})
            """)
        with col2:
            st.markdown("### Top 10 Nationalities")
            st.write(df['Nationality'].value_counts().head(10).to_frame('Count'))

    with tab3:
        st.markdown("### Historical Trends in African Representation")
        
        # Convert BeginDate to numeric and create decade grouping
        df['BeginDate'] = pd.to_numeric(df['BeginDate'], errors='coerce')
        df['Decade'] = (df['BeginDate'] // 10) * 10
        
        # Filter data
        filtered_df = df[df['Decade'] >= 1000].copy()
        
        african_data = filtered_df[
            filtered_df['Ethnicity'].str.contains('African', na=False) |
            filtered_df['Nationality'].str.contains('African', na=False)
        ]
        
        # Calculate proportions
        total_per_decade = filtered_df.groupby('Decade').size()
        african_per_decade = african_data.groupby('Decade').size()
        proportion = (african_per_decade / total_per_decade).fillna(0)
        
        # Create dataframe for plotting
        trend_df = pd.DataFrame({
            'Decade': proportion.index,
            'Proportion': proportion.values
        })
        
        # Create Plotly line chart
        fig_trends = go.Figure()
        fig_trends.add_trace(
            go.Scatter(
                x=trend_df['Decade'],
                y=trend_df['Proportion'],
                mode='lines+markers',
                name='Proportion',
                line=dict(color='lightcoral'),
                marker=dict(size=8)
            )
        )
        
        fig_trends.update_layout(
            title={
                'text': 'Proportion of African Representation Over Time at Museum of Modern Art',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title="Decade",
            yaxis_title="Proportion",
            yaxis_tickformat = ',.1%',
            hovermode='x unified',
            showlegend=False
        )
        
        st.plotly_chart(fig_trends, use_container_width=True)
        
        # Add contextual information
        st.markdown("""
        ### Analysis Insights
        This visualization shows the historical progression of African representation in the museum's 
        collection over time. Key observations:
        - The trend line indicates changes in the proportion of African artists relative to the total collection
        - Each point represents a decade's proportion of African representation
        - Hover over points to see exact proportions for each decade
        """)
    
    # Download section at the bottom
    st.header("Download Data")
    st.markdown("""
    The processed dataset is available for download. This includes:
    - Combined artist information from MoMA and smaller museums
    - Standardized ethnicity classifications
    - Institutional attribution
    """)
    
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Dataset as CSV",
        data=csv,
        file_name="museum_artists_analysis.csv",
        mime="text/csv"
    )
else:
    st.error("Unable to load the dataset. Please check the file path and try again.")