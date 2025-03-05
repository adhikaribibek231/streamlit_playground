import streamlit as st
import sqlite3
import hashlib
from utils import register_user

st.set_page_config(page_title="Register")

st.sidebar.button("Home", on_click=lambda: st.switch_page("streamlit_app.py"))
st.sidebar.button("Login", on_click=lambda: st.switch_page("login.py"))
st.sidebar.button("Register", on_click=lambda: st.switch_page("register.py"))

st.title("Register")

new_username = st.text_input("Choose a Username")
new_password = st.text_input("Choose a Password", type="password")

if st.button("Register"):
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    if register_user(new_username, hashed_password):
        st.success("Registered successfully! You can now log in.")
        st.switch_page("login.py")
    else:
        st.error("Username already exists. Try a different one.")
