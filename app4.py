import streamlit as st

with st.sidebar:
  st.header("대학")
  weather = st.selectbox("오늘 날씨", ["수한", "수완"])
