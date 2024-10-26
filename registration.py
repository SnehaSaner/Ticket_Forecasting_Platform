import streamlit as st

# Set page configuration
st.set_page_config(page_title="Registration Page", layout="centered")

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

    /* Centered container for the registration box */
    .register-box {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        max-width: 400px;
        margin: 100px auto;
        text-align: center;
    }

    .register-title {
        font-size: 30px;
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

    /* Register button */
    .register-button {
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

    .register-button:hover {
        background-color: #ff4500;
    }

    /* Login link */
    .login-link {
        margin-top: 20px;
        display: block;
        font-size: 16px;
        color: #00235b;
        text-decoration: none;
    }

    .login-link:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Centered registration container
st.markdown("""
    <div class="register-box">
        <h2 class="register-title">Access the Secret Door!</h2>
        <form>
            <input type="text" placeholder="Username" required>
            <input type="email" placeholder="Email" required>
            <input type="password" placeholder="Password" required>
            <button class="register-button" type="submit">Register</button>
        </form>
        <a href="#" class="login-link">Already have an account? Log In</a>
    </div>
""", unsafe_allow_html=True)