import streamlit as st

st.markdown("# 앱ui만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
user_id = st.text_input("반", placeholder="반")
creativity = st.slider("난이도", 0, 100, 50)
