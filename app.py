import streamlit as st
from bbquote.api import quote

st.title("Welcome to our website")

result = quote()

st.write(result)
