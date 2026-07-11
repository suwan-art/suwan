import streamlit as st

st.markdown("# 앱ui만들기")
user_id = st.text_input("아이디(ID)를 입력하세요", placeholder="example_user")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
