import streamlit as st
import random
import streamlit.components.v1 as components

# 🍱 음식 데이터
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

# 🔧 페이지 설정
st.set_page_config(page_title="점심 대포 추천기", layout="centered")
st.title("🎯 점심 대포 추천기")
st.caption("먹고 싶은 음식 종류를 골라보세요!")

# ✅ 사용자 선택
selected_categories = st.multiselect(
    "음식 종류 선택",
    options=list(menu_data.keys()),
    default=list(menu_data.keys())
)

# 🎯 메뉴 필터링
filtered_menu = [
    (category, food)
    for category in selected_categories
    for food in menu_data[category]
]

# 💥 발사 버튼
if st.button("발사! 대포에서 점심 메뉴 쏘기 💥"):

    # 🚨 빈 리스트면 중단
    if not filtered_menu:
        st.error("⚠️ 추천할 음식이 없습니다. 음식 종류를 선택해주세요.")
        st.stop()

    # ✅ 안전하게 추천
    chosen_category, chosen_food = random.choice(filtered_menu)

    # HTML + CSS 대포 애니메이션
    cannon_html = f"""
    <style>
    .cannon-wrapper {{
        position: relative;
        text-align: center;
