import streamlit as st
from utils import check_login_status

st.set_page_config(page_title="Home")

# Navigation buttons
st.sidebar.button("Home", on_click=lambda: st.switch_page("home.py"))
st.sidebar.button("Login", on_click=lambda: st.switch_page("login.py"))
st.sidebar.button("Register", on_click=lambda: st.switch_page("register.py"))

st.title("Welcome to Home Page")

if check_login_status():
    st.write("Hello, World!")
    st.write("Hi, how are you?")
else:
    st.write("Hello, World!")
    st.info("Please log in to see more content.")
