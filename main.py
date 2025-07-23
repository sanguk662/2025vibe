import streamlit as st
import random
import time
import streamlit.components.v1 as components

# 음식 데이터
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

st.set_page_config(page_title="점심 대포 추천", layout="centered")
st.title("🎯 점심 대포 추천기")

# 사용자 카테고리 선택
selected_categories = st.multiselect("먹고 싶은 음식 종류를 골라보세요:", menu_data.keys(), default=list(menu_data.keys()))

# 선택된 메뉴 리스트 만들기
filtered_menu = []
for cat in selected_categories:
    for item in menu_data[cat]:
        filtered_menu.append((cat, item))  # (카테고리, 음식)

if not filtered_menu:
    st.warning("최소 하나의 음식 종류를 선택해주세요.")
    st.stop()

# 대포 추천 버튼
if st.button("발사! 대포에서 점심 메뉴 쏘기 💥"):
    # 음식 선택
    chosen_category, chosen_food = random.choice(filtered_menu)

    # 애니메이션 효과 (HTML + CSS)
    cannon_html = f"""
    <style>
    .cannon-wrapper {{
        text-align: center;
        margin-top: 50px;
        position: relative;
    }}
    .cannon {{
        width: 150px;
        height: auto;
    }}
    .food {{
        font-size: 32px;
        font-weight: bold;
        animation: shoot 1s ease-out forwards;
        position: absolute;
        left: 50%;
        top: 0;
        transform: translateX(-50%);
        color: #FF5722;
    }}

    for cat in selected_categories:
        st.write(f"**{cat}**: {', '.join(menu_data[cat])}")
