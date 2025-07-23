import streamlit as st
import random
import streamlit.components.v1 as components

# -----------------------------
# 🍱 음식 데이터 (카테고리별)
# -----------------------------
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

# -----------------------------
# 🌟 Streamlit 설정
# -----------------------------
st.set_page_config(page_title="점심 대포 추천", layout="centered")
st.title("🎯 점심 대포 추천기")

# -----------------------------
# ✅ 사용자 입력 - 음식 종류 선택
# -----------------------------
selected_categories = st.multiselect(
    "먹고 싶은 음식 종류를 골라보세요:",
    menu_data.keys(),
    default=list(menu_data.keys())
)

# -----------------------------
# 🎯 추천 대상 메뉴 필터링
# -----------------------------
filtered_menu = [
    (category, item)
    for category in selected_categories
    for item in menu_data[category]
]

if not filtered_menu:
    st.warning("최소 하나의 음식 종류를 선택해주세요.")
    st.stop()

# -----------------------------
# 💥 발사 버튼 클릭 시 동작
# -----------------------------
if st.button("발사! 대포에서 점심 메뉴 쏘기 💥"):
    chosen_category, chosen_food = random.choice(filtered_menu)

    # HTML + CSS 애니메이션 효과
    cannon_html = f"""
    <style>
    .cannon-wrapper {{
        text-align: center;
        margin-top: 50px;
        position: relative;
        height: 200px;
    }}
    .cannon {{
        width: 120px;
        height: auto;
        margin-top: 50px;
    }}
    .food {{
        font-size: 32px;
        font-weight: bold;
        animation: shoot 1s ease-out forwards;
        position: absolute;
        left: 50%;
        top: 50px;
        transform: translateX(-50%);
        color: #FF5722;
        opacity: 0;
    }}
    @keyframes shoot {{
        0% {{ top: 50px; opacity: 0; transform: translateX(-50%) scale(0.2); }}
        50% {{ opacity: 1; transform: translateX(-50%) scale(1.4); }}
        100% {{ top: -60px; opacity: 1; transform: translateX(-50%) scale(1); }}
    }}
    </style>

    <div class="cannon-wrapper">
        <div class="food">{chosen_food} <span style='font-size:18px;'>({chosen_category})</span></div>
        <img src="https://cdn-icons-png.flaticon.com/512/727/72739
