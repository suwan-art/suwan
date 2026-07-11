import streamlit as st

with st.sidebar:
  st.header("대학")
  weather = st.selectbox(["수한", "수완"])
