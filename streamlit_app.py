import streamlit as st
from utils import check_login_status

st.set_page_config(page_title="Home")

# Navigation bar using a horizontal layout
st.markdown(
    """
    <style>
        .nav-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .nav-container a {
            text-decoration: none;
            color: black;
            font-weight: bold;
        }
    </style>
    <div class='nav-container'>
        <a href='home.py'>🏠 Home</a>
        <a href='login.py'>🔑 Login</a>
        <a href='register.py'>📝 Register</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Home Page")

if check_login_status():
    st.write("Hello, World!")
    st.write("Hi, how are you?")
else:
    st.write("Hello, World!")
    st.info("Please log in to see more content.")
