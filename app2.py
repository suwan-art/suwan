import streamlit as st

st.markdown("# 앱ui만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
user_id = st.text_input("반", placeholder="반")
creativity = st.slider("난이도", 0, 100, 50)
ai_speed = st.select_slider("응답 처리 속도를 선택하세요",options=["매우 느림", "느림", "보통", "빠름", "실시간"],value="보통")
