import streamlit as st

st.markdown("# 앱ui만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
user_id = st.text_input("반", placeholder="반")
ai_speed = st.select_slider("난이도",options=["쉬움", "보통", "어려움"],value="보통")
creativity = st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감")
