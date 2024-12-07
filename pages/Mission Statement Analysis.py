import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
        
        /* Enhanced text visibility */
        .stMarkdown, .stMarkdown p, .stMarkdown li {{
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            line-height: 1.6 !important;
        }}
        
        /* Headers and text */
        h1, h2, h3, .subheader {{
            color: rgb(255, 255, 255) !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-weight: 700 !important;
        }}
        
        /* Content sections */
        .content-section {{
            background-color: rgba(0, 0, 0, 0.7);
            padding: 25px;
            border-radius: 10px;
            margin: 15px 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        /* Metrics styling */
        div.stMetric {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        div.stMetric label,
        div.stMetric [data-testid="stMetricValue"],
        div.stMetric [data-testid="stMetricDelta"],
        div.stMetric [data-testid="stMetricLabel"] {{
            color: rgb(255, 255, 255) !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
            font-weight: 600 !important;
        }}
        
        /* Interactive elements */
        .streamlit-expanderHeader, div.stAlert {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: rgb(255, 255, 255) !important;
        }}
        
        /* Form elements */
        div.stSlider label, 
        div.stCheckbox label,
        div.stTextInput label {{
            color: rgb(255, 255, 255) !important;
            font-weight: 600 !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }}
        
        /* Charts and dataframes */
        .js-plotly-plot {{
            background-color: rgba(255, 255, 255, 0.98) !important;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        .dataframe {{
            background-color: rgba(255, 255, 255, 0.98) !important;
            border-radius: 10px;
        }}
        
        /* Info boxes */
        div.stAlert {{
            background-color: rgba(0, 0, 0, 0.7) !important;
            color: rgb(255, 255, 255) !important;
            border: 2px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px;
            padding: 1.2rem;
            margin: 1.2rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }}
        
        div.stAlert p {{
            color: rgb(255, 255, 255) !important;
            font-weight: 500 !important;
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

# Page Configuration
st.set_page_config(
    page_icon=":mortar_board:",
    page_title="Mission Statement Analysis",
    layout="wide"
)

# Add background image
image_path = r"images\aaron douglas - song of the tower.jfif"
st.markdown(add_bg_from_local(image_path), unsafe_allow_html=True)

# Define words to highlight (you can modify this list)
HIGHLIGHT_WORDS = ['global','diverse','diversity','african','equity',
                   'black','women','inclusion','community','culture',
                   'cultural','identity','outreach','equitable','discrimination',
                   'integrity'
]

# Title
st.title("Mission Statement Analysis")

try:
    # Read data
    data_path = Path('data/Mission_Statement_Word_Freq.csv')
    df = pd.read_csv(data_path)
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Mission Statement Word Frequencies")
        
        # Add highlight controls
        show_highlights = st.checkbox("ADEI Buzzwords", value=True)
        if show_highlights:
            st.info(f"Highlighted words: {', '.join(HIGHLIGHT_WORDS)}")
        
        # Slider for selecting number of words to display
        num_words = st.slider("Number of words to display", 5, 50, 25)
        top_n = df.head(num_words)
        
        # Create enhanced bar graph with highlighting
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create bars with different colors based on highlighting
        bars = []
        for i, (word, freq) in enumerate(zip(top_n['Words'], top_n['Frequency'])):
            if show_highlights and word.lower() in [w.lower() for w in HIGHLIGHT_WORDS]:
                # Highlighted bars
                bar = ax.bar(i, freq, color='#FF6B6B')  # Coral red for highlighted words
            else:
                # Regular bars
                bar = ax.bar(i, freq, color='#4A90E2')  # Blue for regular words
            bars.append(bar[0])
        
        # Customize the graph
        ax.set_xlabel('Words', fontsize=10)
        ax.set_ylabel('Frequency', fontsize=10)
        ax.set_title('Distribution of Most Common Words in Mission Statements', fontsize=12)
        
        # Set x-axis labels
        plt.xticks(range(len(top_n)), top_n['Words'], rotation=45, ha='right')
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            word_idx = bars.index(bar)
            word = top_n['Words'].iloc[word_idx]
            
            # Different text color and weight for highlighted words
            if show_highlights and word.lower() in [w.lower() for w in HIGHLIGHT_WORDS]:
                color = '#FF6B6B'
                weight = 'bold'
            else:
                color = '#4A90E2'
                weight = 'normal'
                
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom',
                   color=color,
                   weight=weight)
        
        plt.tight_layout()
        st.pyplot(fig)
        
    with col2:
        # Display interactive dataframe with highlighting
        st.subheader("Word Frequency Data")
        
        # Add search functionality
        search_word = st.text_input("Search for a specific word:")
        
        # Style the dataframe to highlight specific words
        def highlight_words(row):
            if show_highlights and row['Words'].lower() in [w.lower() for w in HIGHLIGHT_WORDS]:
                return ['background-color: #FFE0E0'] * len(row)
            return [''] * len(row)
        
        if search_word:
            filtered_df = df[df['Words'].str.contains(search_word, case=False)]
            st.dataframe(filtered_df.style.apply(highlight_words, axis=1))
        else:
            st.dataframe(df.style.apply(highlight_words, axis=1))
    
      # Add summary statistics
    st.subheader("Quick Statistics")
    col3, col4, col5 = st.columns(3)
    
    # Calculate highlighted words statistics
    highlighted_words_present = df[df['Words'].str.lower().isin([w.lower() for w in HIGHLIGHT_WORDS])]
    
    with col3:
        st.metric("Words That Occur Three or More Times", len(df))
    with col4:
        st.metric("Highlighted Words Found", 
                 len(highlighted_words_present),
                 f"out of {len(HIGHLIGHT_WORDS)} tracked")
    with col5:
        if not highlighted_words_present.empty:
            top_highlighted = highlighted_words_present.iloc[0]
            st.metric("Top Highlighted Word", 
                     top_highlighted['Words'],
                     f"Frequency: {top_highlighted['Frequency']}")
        else:
            st.metric("Top Highlighted Word", "None found", "No highlighted words in data")

    # Add Key Findings section
    st.markdown("---")
    st.subheader("Research Findings")
    
    # Study Overview
    st.markdown("""
    ### Study Overview
    This research analyzed 81 museum mission statements to examine the alignment between institutional language and actual diversity practices. 
    Our methodology included examining common word frequencies, conducting sentiment analysis, and analyzing word co-occurrences to understand 
    the tones and language patterns used in these statements.
    """)
    
    # Create columns for detailed findings
    find_col1, find_col2 = st.columns([1, 1])
    
    with find_col1:
        st.markdown("""
        ### Common Words Analysis
        The analysis of word frequencies revealed important patterns:
        
        - **Top-Tier Words** (Most Frequent):
          - "american"
          - "cultural"
          - "world"
          - "community"
          - "global"
        
        - **Second-Tier Words** (9-12 occurrences):
          - "diverse"
          - "diversity"
          - "african"
          - "equity" (fewer than 10 mentions across 80+ statements)
        
        **Key Finding:** Only approximately 10% of mission statements employ language explicitly supporting diversity claims, 
        which correlates with the limited diversity representation observed in other platforms like social media.
        """)
    
    with find_col2:
        st.markdown("""
        ### Sentiment Analysis
        Using TextBlob analysis tools, we evaluated the emotional tone of statements:
        
        - **Scale:** -1 (negative) to +1 (positive)
        - **Average Score:** 0.1778
        - **Range:**
          - Minimum: -0.2
          - Maximum: 0.8
        
        **Key Finding:** Mission statements generally maintain a neutral tone with a slight positive 
        lean, suggesting careful and measured institutional messaging rather than strongly 
        emotional or aspirational language.
        """)
    
    # Add overall implications
    st.markdown("""
    ### Research Implications
    This analysis reveals a significant gap between institutional rhetoric and diversity initiatives. While museums often 
    present themselves as globally-oriented cultural institutions, the limited use of diversity-related language in mission 
    statements (only ~10%) suggests a disconnect between public messaging and diversity commitments. The neutral tone of 
    most statements, combined with sparse use of DEI terminology, indicates that many institutions may not be explicitly 
    positioning themselves as champions of diversity and inclusion in their core messaging.
    """)

 # Add overall summary
    st.markdown("""
    ### Summary of Analysis
    This word frequency analysis demonstrates how institutions are articulating their commitments through mission statements. 
    The data suggests a balance between traditional academic missions and evolving societal responsibilities, particularly 
    in areas of diversity, equity, and inclusion. The varying frequency of ADEI-related terms may indicate different levels 
    of emphasis across institutions, while also highlighting opportunities for more explicit integration of these concepts 
    into institutional messaging.
    """)
    
    # Add descriptive section at the bottom
    st.markdown("---")  # Add a horizontal line for visual separation
    
    with st.expander("About This Analysis", expanded=False):
        st.markdown("""
        ### Understanding the Mission Statement Analysis
        
        This dashboard provides a comprehensive analysis of word frequencies in institutional mission statements, with a particular focus on Access, Diversity, Equity, and Inclusion (ADEI) related terms. Here's what you're seeing:
        
        #### 🎯 Purpose
        - Identify and track the most commonly used words across mission statements
        - Highlight ADEI-related terms to understand their prevalence
        - Provide interactive tools for deeper analysis of word usage patterns
        
        #### 📊 Features Explained
        - **Bar Graph**: Shows the distribution of the most frequent words, with ADEI terms highlighted in coral red
        - **Word Frequency Data**: Searchable table of all words that appear three or more times
        - **Quick Statistics**: Overview of total word count, ADEI terms found, and top highlighted words
        
        #### 🔍 How to Use
        1. Use the slider to adjust how many words you want to see in the graph
        2. Toggle the "ADEI Buzzwords" checkbox to highlight relevant terms
        3. Search for specific words using the search box in the Word Frequency Data section
        4. Click on column headers in the data table to sort by frequency or alphabetically
        
        #### 📈 Data Notes
        - Only words appearing three or more times are included in the analysis
        - ADEI terms are pre-defined and can be modified as needed
        - Frequencies represent the total count across all analyzed mission statements
        """)

except FileNotFoundError:
    st.error("Could not find the CSV file in the data directory.")
    st.info(f"Current working directory: {Path.cwd()}")
except Exception as e:
    st.error(f"An unexpected error occurred: {str(e)}")