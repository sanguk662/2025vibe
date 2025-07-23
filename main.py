import streamlit as st
import random
import streamlit.components.v1 as components

# ------------------------
# 🍱 음식 데이터
# ------------------------
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

# ------------------------
# 🧾 기본 설정
# ------------------------
st.set_page_config(page_title="점심 대포 추천기", layout="centered")
st.title("🎯 점심 대포 추천기")
st.caption("먹고 싶은 음식 종류를 골라주세요!")

# ------------------------
# ✅ 음식 종류 선택
# ------------------------
selected_categories = st.multiselect(
    "음식 종류 선택",
    options=list(menu_data.keys()),
    default=list(menu_data.keys())
)

# ------------------------
# 🎯 메뉴 필터링
# ------------------------
filtered_menu = [
    (category, food)
    for category in selected_categories
    for food in menu_data[category]
]

# ------------------------
# 💥 대포 발사 버튼
# ------------------------
if st.button("발사! 대포에서 점심 메뉴 쏘기 💥"):

    if not filtered_menu:
        st.error("⚠️ 음식 종류를 하나 이상 선택해주세요.")
        st.stop()

    chosen_category, chosen_food = random.choice(filtered_menu)

    # 대포 애니메이션 HTML + CSS
    cannon_html = f"""
    <style>
    .cannon-wrapper {{
        position: relative;
        text-align: center;
        margin-top: 50px;
        height: 220px;
    }}
    .cannon {{
        width: 120px;
        margin-top: 80px;
    }}
    .food-shot {{
        font-size: 30px;
        font-weight: bold;
        color: #FF5722;
        position: absolute;
        left: 50%;
        top: 70px;
        transform: translateX(-50%);
        opacity: 0;
        animation: shoot 1s ease-out forwards;
    }}
    @keyframes shoot {{
        0% {{
            opacity: 0;
            transform: translateX(-50%) translateY(0px) scale(0.3);
        }}
        50% {{
            opacity: 1;
            transform: translateX(-50%) translateY(-60px) scale(1.3);
        }}
        100% {{
            opacity: 1;
            transform: translateX(-50%) translateY(-150px) scale(1);
        }}
    }}
    </style>

    <div class="cannon-wrapper">
        <div class="food-shot">{chosen_food} <span style='font-size:16px;'>({chosen_category})</span></div>
        <img class="cannon" src="https://cdn-icons-png.flaticon.com/512/727/727399.png" />
    </div>
    """

    components.html(cannon_html, height=300)
    st.success(f"🍽️ 오늘의 점심은 **{chosen_category} - {chosen_food}** 입니다!")
