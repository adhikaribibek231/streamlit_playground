import streamlit as st
import sqlite3
import hashlib
from utils import login_user, set_login_status

st.set_page_config(page_title="Login")

st.sidebar.button("Home", on_click=lambda: st.switch_page("streamlit_app.py"))
st.sidebar.button("Login", on_click=lambda: st.switch_page("login.py"))
st.sidebar.button("Register", on_click=lambda: st.switch_page("register.py"))

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if login_user(username, hashed_password):
        set_login_status(username)
        st.success("Logged in successfully!")
        st.switch_page("home.py")
    else:
        st.error("Invalid credentials")
