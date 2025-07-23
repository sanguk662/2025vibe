import streamlit as st
import random

# 기본 점심 메뉴 리스트
default_menu = [
    "김치찌개", "된장찌개", "불고기", "제육볶음", "비빔밥", "김밥", "냉면",
    "칼국수", "돈까스", "햄버거", "파스타", "샐러드", "쌀국수", "초밥", "떡볶이"
]

# 세션 상태에 메뉴 저장
if 'menu' not in st.session_state:
    st.session_state.menu = default_menu.copy()

st.title("🍱 오늘 뭐 먹지?")

# 메뉴 추천 버튼
if st.button("점심 메뉴 추천받기"):
    recommendation = random.choice(st.session_state.menu)
    st.success(f"✨ 오늘의 추천 메뉴: **{recommendation}**")

# 메뉴 추가 기능
with st.expander("➕ 메뉴 직접 추가하기"):
    new_item = st.text_input("추가할 메뉴 입력")
    if st.button("메뉴 추가"):
        if new_item and new_item not in st.session_state.menu:
            st.session_state.menu.append(new_item)
            st.success(f"'{new_item}' 메뉴가 추가되었어요!")
        elif new_item in st.session_state.menu:
            st.warning("이미 있는 메뉴입니다.")
        else:
            st.warning("메뉴를 입력해주세요.")

# 현재 메뉴 리스트 보여주기
with st.expander("📋 현재 메뉴 리스트 보기"):
    st.write(st.session_state.menu)
