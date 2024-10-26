import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns  # If not installed, run: pip install seaborn
import matplotlib.pyplot as plt 
import io
import os
import plotly.io as pio
from fpdf import FPDF
import tempfile
import random
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MousePosition, Fullscreen, MeasureControl, Draw


# Initialize session state for the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Overview'

# Function to change pages
def set_page(page):
    st.session_state.current_page = page

# CSS for custom sidebar styling
st.markdown(
    """
    <style>
        

        /* Style for buttons inside the container */
        .navigation-container .stButton button {
            background: linear-gradient(to right, #6a0dad, #00bfae);
            color: #fff;
            font-size: 18px;
            padding: 12px 20px;
            width: 100%;
            border: none;
            border-radius: 8px;
            margin: 10px 0;
            cursor: pointer;
            font-family: 'Bubblegum Sans', cursive;
            font-weight: bold;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        /* Hover effect for buttons */
        .navigation-container .stButton button:hover {
            background: linear-gradient(to right, #00bfae, #6a0dad);
            transform: scale(1.05);
        }

         
    </style>
    """,
    unsafe_allow_html=True
)

# Inline CSS styling
st.markdown(
    """
    <style>
    .custom-subheader {
        color: #FF6347; /* Change to the color you want */
        font-size: 24px; /* Adjust font size as needed */
        font-family: 'Bubblegum Sans', cursive; /* Change font family */
        margin: 20px 0; /* Add spacing */
        font-weight: bold; /* Make text bold */
        text-align: center; /* Center the text */
        background: linear-gradient(to right, #ffafbd, #ffc3a0); /* Gradient background */
        padding: 10px;
        border-radius: 8px; /* Rounded corners */
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2); /* Optional: Add a shadow */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True
)





# Sidebar navigation buttons
with st.sidebar:
    st.markdown('<div class="navigation-container">', unsafe_allow_html=True)
    st.markdown(
    f'<div style="color: #00235b; font-size: 40px; font-family: \'Bubblegum Sans\', cursive; font-weight: bold; text-align: center;">Navigation</div>',
    unsafe_allow_html=True
)
 # Add a title for the navigation section

    if st.button('Overview'):
        set_page('Overview')

    if st.button('Demand Forecasting'):
        set_page('Demand Forecasting')

    if st.button('Data Exploration'):
        set_page('Data Exploration')

    if st.button('Insights'):
        set_page('Insights')

    st.markdown('</div>', unsafe_allow_html=True)

    # Other buttons (Feedback, Settings, Help, Logout) outside the navigation container
    st.button('Feedback')
    st.button('Settings')
    st.button('Help')
    st.button('Logout')

# Header with colored star

# Add the animated icons and subheader using st.markdown
st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <div class="icon-container"><i class="fas fa-music"></i></div> <!-- Start icon -->
        <h1 style="display: inline; color: #FF6347; font-family: 'Bubblegum Sans', cursive; margin: 0 20px;">Ticket Availability Dashboard</h1>
        
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("Welcome to the **Ticket Availability Dashboard**. This is your one-stop solution for analyzing and forecasting event ticket availability trends!")

# Function to load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Apply custom CSS from 'styles.css'
local_css("styles.css")


# Cache data loading
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the cleaned and categorized dataset
file_path = 'categorized_events_dataset_updated.csv'  # Update this path if needed
categorized_data = load_data(file_path)

# Filter data for the overview
overview_data = categorized_data[['event_category', 'availability_standard', 'availability_resale']]

# Group data by category for the demand overview
category_summary = overview_data.groupby('event_category').sum().reset_index()


# Sample dataset mapping event categories to latitude and longitude (you can expand this based on your data)
location_data = {
    'Music Concert': {'latitude': 40.7128, 'longitude': -74.0060},  # New York
    'Sports Event': {'latitude': 34.0522, 'longitude': -118.2437},  # Los Angeles
    'Theater': {'latitude': 51.5074, 'longitude': -0.1278},  # London
    'Comedy Show': {'latitude': 48.8566, 'longitude': 2.3522},  # Paris
    'Festival': {'latitude': 35.6895, 'longitude': 139.6917},  # Tokyo
    'Film Premiere': {'latitude': 55.7558, 'longitude': 37.6173},  # Moscow
    'Art Exhibition': {'latitude': 41.9028, 'longitude': 12.4964}  # Rome
}

def add_lat_lon_to_data(data):
    # Add latitude and longitude columns to the DataFrame
    data['latitude'] = data['event_category'].apply(lambda x: location_data.get(x, {}).get('latitude', None))
    data['longitude'] = data['event_category'].apply(lambda x: location_data.get(x, {}).get('longitude', None))
    return data

# Function to display Folium map in the demand overview
def demand_overview():
    st.title('Overview Page')
    st.write("This section provides an overview of ticket availability across different event categories.")

    # Create a horizontal bar chart for ticket availability distribution
    fig = px.bar(
        category_summary,
        y='event_category',
        x='availability_standard',
        orientation='h',
        color='availability_standard',
        labels={'event_category': 'Event Category', 'availability_standard': 'Standard Ticket Availability'},
        title='Ticket Availability Distribution by Event Category',
        color_continuous_scale='Viridis'
    )

    fig.update_layout(
        yaxis=dict(title='Event Category'),
        xaxis=dict(title='Availability Standard'),
        coloraxis_colorbar=dict(title='Tickets Available'),
        height=600
    )

    st.plotly_chart(fig)

# Load the dataset once and cache it
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Convert event_date to datetime during data loading
    data['event_date'] = pd.to_datetime(data['event_date'], errors='coerce')
    return data

# Use the cached data loader
categorized_data = load_data('categorized_events_dataset_updated.csv')

def demand_forecasting(data):
    st.title('Demand Forecasting Page')

    # Step 1: Filter data for years 2024 to 2035 (Optimized to run on already pre-processed data)
    data = data[(data['event_date'].dt.year >= 2024) & (data['event_date'].dt.year <= 2035)]

    # Sample data if it's too large for quicker visualization (adjust sample size as needed)
    if len(data) > 10000:
        data = data.sample(n=10000, random_state=42)

    # User input for threshold
    availability_threshold = st.slider('Select Availability Threshold (%)', 0, 100, 50)
    filtered_data = data[data['availability_standard'] >= availability_threshold]

    # Aggregate data by year and event category
    filtered_data['year'] = filtered_data['event_date'].dt.year
    aggregated_data = filtered_data.groupby(['year', 'event_category']).sum(numeric_only=True).reset_index()

    

    # Step 3: Create the stacked bar chart
    st.markdown('Forecast Availability by Year and Event Category')
    fig_bar = px.bar(
        aggregated_data,
        x='year',
        y='availability_standard',
        color='event_category',
        title='Stacked Bar Chart: Forecast Availability by Event Category',
        labels={'availability_standard': 'Total Ticket Availability'},
        text='availability_standard',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        hover_name='event_category'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Step 4: Create the demand pie chart
    st.markdown('Demand Distribution')
    demand_pie = filtered_data.groupby('event_category')['availability_standard'].sum().reset_index()
    fig_pie = px.pie(
        demand_pie,
        names='event_category',
        values='availability_standard',
        title='Demand Distribution by Event Category',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # Step 5: Pricing Analysis - Simple Bar Chart
    st.markdown('Pricing Analysis')
    price_summary = filtered_data.groupby('year')['capacity'].sum().reset_index()
    fig_price = px.bar(
        price_summary,
        x='year',
        y='capacity',
        title='Pricing Suggestion Over Time',
        labels={'capacity': 'Total Capacity'},
        color_discrete_sequence=['#636EFA']
    )
    st.plotly_chart(fig_price, use_container_width=True)

    # Display the summarized data for reference
    st.write(aggregated_data)

    # Generate and Download PDF Button
    if st.button('Download Forecasting Report as PDF'):
        # Create a temporary directory to store images
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save figures as images
            fig_bar_path = f"{temp_dir}/fig_bar.png"
            fig_pie_path = f"{temp_dir}/fig_pie.png"
            fig_price_path = f"{temp_dir}/fig_price.png"

            fig_bar.write_image(fig_bar_path)
            fig_pie.write_image(fig_pie_path)
            fig_price.write_image(fig_price_path)

            # Generate PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(200, 10, 'Forecasting Report', ln=True, align='C')
            pdf.set_font('Arial', '', 12)
            pdf.cell(200, 10, f'Threshold: {availability_threshold}%', ln=True)
            pdf.ln(10)

            # Add bar chart image to PDF
            pdf.image(fig_bar_path, x=10, y=30, w=180)
            pdf.ln(85)

            # Add pie chart image to PDF
            pdf.image(fig_pie_path, x=10, y=130, w=180)
            pdf.ln(85)

            # Add pricing bar chart image to PDF
            pdf.image(fig_price_path, x=10, y=230, w=180)

            # Save the PDF to a temporary file
            pdf_output_path = f"{temp_dir}/forecasting_report.pdf"
            pdf.output(pdf_output_path)

            # Read the PDF file and provide download button
            with open(pdf_output_path, 'rb') as pdf_file:
                pdf_data = pdf_file.read()
                st.download_button(
                    label="Download Forecasting Report as PDF",
                    data=pdf_data,
                    file_name='forecasting_report.pdf',
                    mime='application/pdf'
                )
# Function for Data Exploration page
# Data Exploration Section
def data_exploration(categorized_data):
    st.title('Data Exploration Page')

    # Dropdown to select a venue with a unique key
    venue_options = categorized_data['venue_id'].unique()
    selected_venue_id = st.selectbox('Select Venue ID:', venue_options, key='unique_venue_selectbox')

    # Filter data based on selected venue_id
    filtered_data = categorized_data[categorized_data['venue_id'] == selected_venue_id]

    # Check if there is data for the selected venue
    if filtered_data.empty:
        st.warning("No data available for venue ID {selected_venue_id}.")
        return

    # Debug: Show first few rows of the filtered data to understand its contents
    st.write("Filtered Data Preview:", filtered_data.head())

    # Scatter plot for ticket availability by event date
    st.markdown('Ticket Availability for Venue ID: {selected_venue_id}')
    fig = px.scatter(
        filtered_data,
        x='event_date',
        y='availability_standard',
        color='event_category',
        size='capacity',
        hover_name='event_category',
        title=f'Ticket Availability at Venue {selected_venue_id}',
        labels={'availability_standard': 'Ticket Availability'},
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        xaxis_title='Event Date',
        yaxis_title='Availability Standard',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#f0f0f0',
        title_x=0.5,
    )
    st.plotly_chart(fig, use_container_width=True)

    # Correlation Scatter Plot
    st.markdown('Correlation Analysis: Select Variables')
    
    # Dropdown to select variables for correlation analysis
    available_columns = ['availability_standard', 'availability_resale', 'capacity']
    x_axis = st.selectbox('Select X-axis Variable:', available_columns, key='unique_x_axis')
    y_axis = st.selectbox('Select Y-axis Variable:', available_columns, key='unique_y_axis')
    
    # Scatter plot for correlation
    st.markdown(f'Correlation Scatter Plot: {x_axis} vs {y_axis}')
    fig_bubble = px.scatter(
        filtered_data,
        x=x_axis,
        y=y_axis,
        size='capacity',
        color='event_category',
        hover_name='event_category',
        title=f'Correlation Scatter Plot: {x_axis} vs {y_axis}',
        labels={x_axis: x_axis.title(), y_axis: y_axis.title()},
        color_continuous_scale='Plasma'
    )
    fig_bubble.update_layout(
        xaxis_title=x_axis.title(),
        yaxis_title=y_axis.title(),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#f0f0f0',
        title_x=0.5,
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

def insights(categorized_data):
    st.title("Insights")

    # Step 1: Convert 'event_date' to datetime and ensure it's in UTC
    categorized_data['event_date'] = pd.to_datetime(categorized_data['event_date'], errors='coerce').dt.tz_convert('UTC')
    
    # Step 2: Date Range Selection
    st.markdown("Select Date Range:")
    min_date = categorized_data['event_date'].min().date()
    max_date = categorized_data['event_date'].max().date()
    start_date, end_date = st.date_input("Date Range:", [min_date, max_date])
    
    # Convert start_date and end_date to timezone-aware timestamps in UTC
    start_date = pd.Timestamp(start_date).tz_localize('UTC')
    end_date = pd.Timestamp(end_date).tz_localize('UTC')
    
    # Filter data based on the selected date range
    filtered_data = categorized_data[(categorized_data['event_date'] >= start_date) & (categorized_data['event_date'] <= end_date)]

    # Ensure that filtered_data is not empty
    if filtered_data.empty:
        st.write("No data available for the selected date range.")
    else:
        # Step 3: Plot Overall Trends Graph (Area Chart)
        st.markdown('Overall Trends')
        fig_trend = px.area(
            filtered_data,
            x='event_date',
            y='availability_standard',
            title='Total Ticket Availability Over Time',
            labels={'event_date': 'Date', 'availability_standard': 'Total Ticket Availability'},
            color_discrete_sequence=['#FFA07A'],  # Light salmon color for better readability
            template='plotly_white'  # A clean template for improved visualization
        )
        fig_trend.update_layout(
            xaxis_title='Date',
            yaxis_title='Total Ticket Availability',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='#f0f0f0',
            title_x=0.5,
        )
        st.plotly_chart(fig_trend, use_container_width=True)
# Step 4: Anomaly Detection Section
        st.markdown('## Anomaly Detection')
        anomaly_percentile = st.slider('Select Anomaly Percentile:', 0, 100, 95)
        fig_anomaly = plot_anomaly_detection(filtered_data, anomaly_percentile)
        if fig_anomaly:
            st.plotly_chart(fig_anomaly, use_container_width=True)
        else:
            st.write("No anomalies detected for the selected threshold.")

def plot_anomaly_detection(filtered_data, anomaly_percentile=95):
       if not filtered_data.empty:
        anomaly_threshold = np.percentile(filtered_data['availability_standard'], anomaly_percentile)

        # Filter data for anomalies
        anomalies = filtered_data[filtered_data['availability_standard'] > anomaly_threshold]

        # Custom color sequence for the event categories
        custom_colors = ['#722F37', '#DC143C', '#228B22', '#FFA500', '#1E90FF', '#FF0000', '#FFFF00']

        # Plot the anomaly graph with gridlines
        fig_anomaly = px.scatter(
            anomalies,
            x=anomalies.index,
            y='availability_standard',
            title='Anomaly Detection: Availability Standard',
            color='event_category',
            color_discrete_sequence=custom_colors
        )

        # Add black border to each dot
        fig_anomaly.update_traces(marker=dict(line=dict(width=0.5, color='black')))

        # Update layout to include gridlines
        fig_anomaly.update_layout(
            xaxis_title='Index',
            yaxis_title='Availability Standard',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='#f0f0f0',
            title_x=0.5,
            xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='LightGrey'),
            yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='LightGrey')
        )

        return fig_anomaly
       else:
           return "No data available for the selected date range."
       

# Main logic to switch between pages
if st.session_state.current_page == 'Overview':
    demand_overview()


elif st.session_state.current_page == 'Demand Forecasting':
    demand_forecasting(categorized_data)

elif st.session_state.current_page == 'Data Exploration':
    data_exploration(categorized_data)
    
# Integrate into Insights Page
elif st.session_state.current_page == 'Insights':
    insights(categorized_data)