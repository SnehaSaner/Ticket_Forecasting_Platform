import streamlit as st

# Set page configuration
st.set_page_config(page_title="Login Page", layout="centered")

# Custom CSS to maintain the design style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    /* Page background */
    .stApp {
        background: linear-gradient(to right, #00235b, #ff6868 50%, #00235b);
        color: white;
        font-family: 'Pacifico', cursive;
    }

    /* Centered container for the login box */
    .login-box {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        max-width: 400px;
        margin: 100px auto;
        text-align: center;
    }

    .login-title {
        font-size: 43px;
        font-family: 'Bubblegum Sans', cursive; /* Changed to Bubblegum Sans */ 
        margin-bottom: 30px;
        color: #ff6868;
    }

    /* Input fields styling */
    input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #ddd;
        font-size: 16px;
    }

    /* Login button */
    .login-button {
        background-color: #ff6347;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 18px;
        margin-top: 20px;
        transition: background-color 0.3s;
    }

    .login-button:hover {
        background-color: #ff4500;
    }

    /* Sign-up link */
    .signup-link {
        margin-top: 20px;
        display: block;
        font-size: 16px;
        color: #00235b;
        text-decoration: none;
    }

    .signup-link:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Centered login container
st.markdown("""
    <div class="login-box">
        <h2 class="login-title">Magic Door</h2>
        <form>
            <input type="text" placeholder="Username" required>
            <input type="password" placeholder="Password" required>
            <button class="login-button" type="submit">Login</button>
        </form>
        <a href="#" class="signup-link">New here? Sign Up</a>
    </div>
""", unsafe_allow_html=True)

# Set page configuration
st.set_page_config(page_title="Registration Page", layout="centered")

# Navigation logic
if 'page' not in st.session_state:
    st.session_state['page'] = 'registration'

def navigate_to_main():
    st.session_state['page'] = 'main'
    st.experimental_rerun()

def navigate_to_login():
    st.session_state['page'] = 'login'
    st.experimental_rerun()

# Registration Form
st.title("Registration Page")
username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Button actions for registration and login
if st.button('Register'):
    # Add registration logic here if needed
    navigate_to_main()  # Navigate to the main page

if st.button('Already have an account? Log In'):
    navigate_to_login()  # Navigate to the login page
    
