import streamlit as st

st.markdown("# 앱ui만들기")
user_id = st.text_input("이름", placeholder="홍길동")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
