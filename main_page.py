import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Ticket Forecasting Dashboard", layout="wide")
# Function to encode image to base64
def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the image
img_base64 = get_base64_image("concert.jpg")  # Replace with your image path
img_base64_1 = get_base64_image("Drama.jpg")  # Replace with the correct path to Drama.jpg
img_base64_2 = get_base64_image("Sports.jpg")  # Replace with the correct path to Sports.jpg
img_base64_3 = get_base64_image("Piano.jpg")  

# Custom CSS to set a background image for the hero section
st.markdown(f"""
    <style>
    /* Page background */
    .stApp {{
        background-color: #00235b;
    }}

    /* Navbar styling */
    .navbar {{
       background: linear-gradient(to right, #ff6868, #00235b 50%, #ff6868);

        padding: 20px;
        border-bottom: 1px solid #e5e5e5;
        text-align: center;
    }}

    .navbar h1 {{
        font-size: 50px;
        font-family: 'Bubblegum Sans', cursive; /* Changed to Bubblegum Sans */ 
        color: #ffff;
        display: inline;
        margin: 0 15px;
    }}

    .navbar a {{
        margin: 0 20px;
        color:#ffff;
        font-family: 'Bubblegum Sans', cursive; /* Changed to Bubblegum Sans */
        text-decoration: none;
        font-size: 25px;
    }}

    .navbar a:hover {{
        color: #ff6347;
        font-weight: bold;
    }}

    /* Hero section with background image */
    .hero-section {{
        background-image: url(data:image/jpeg;base64,{img_base64});
        background-size: cover;
        background-position: center;
        padding: 120px 20px;
        color: white;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }}

    /* Overlay content */
    .hero-content {{
        position: relative;
        z-index: 2;
        padding-top: 100px;
        
    }}

    .hero-title {{
        font-size: 56px;
        color:#ffff;
        font-family: 'Bubblegum Sans', cursive; /* Changed to Bubblegum Sans */
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }}

    .hero-button {{
        background-color: #ff6347;
        color: white;
        font-size: 20px;
        padding: 15px 40px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}

    .hero-button:hover {{
        background-color: #ff4500;
    }}

    /* Three boxes section */
    .boxes-section {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 50px;
    }}

    /* Box styles */
    .box {{
        width: 30%;
        padding: 30px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s;
        background-size: cover;
        background-position: center;
        border: 1px solid white; /* Add a white border to the box */
    }}


    .box:hover {{
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
    }}

    .box h3 {{
        font-size: 30px;
        color: #ffff;
        font-family: 'Bubblegum Sans', cursive; /* Changed to Bubblegum Sans */
        margin-bottom: 15px;
    }}

    .box p {{
        font-size: 16px;
        color: #ffff;
        margin-bottom: 20px;
    }}

    .box-button {{
        background-color: #ff6347;
        color: white;
        padding: 10px 25px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
    }}

    .box-button:hover {{
        background-color: #ff4500;
    }}
    </style>
""", unsafe_allow_html=True)

# Navbar Section
st.markdown("""
    <div class="navbar">
        <h1>Ticket Forecast & Event Analysis</h1>
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">Login</a>
        <a href="#">Register</a>
        <a href="#">Contact</a>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Concert Ticket Demand & Pricing</h1>
            <button class="hero-button">Learn More</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Three Boxes Section with different background images
st.markdown(f"""
    <div class="boxes-section">
        <div class="box" style="background-image: url(data:image/jpeg;base64,{img_base64_1});">
            <h3>Drama</h3>
            <p>Discover breathtaking drama performances around you.</p>
            <button class="box-button">Explore Dramas</button>
        </div>
        <div class="box" style="background-image: url(data:image/jpeg;base64,{img_base64_2});">
            <h3>Sports</h3>
            <p>Stay updated with sports events and book your seats to enjoy the action live.</p>
            <button class="box-button">Book Sports Events</button>
        </div>
        <div class="box" style="background-image: url(data:image/jpeg;base64,{img_base64_3});">
            <h3>Piano</h3>
            <p>Find exclusive piano concerts and grab the best seats for an unforgettable experience.</p>
            <button class="box-button">Browse Piano Concerts</button>
        </div>
    </div>
""", unsafe_allow_html=True)

