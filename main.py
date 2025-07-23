import streamlit as st
import random
import streamlit.components.v1 as components
import json

# 음식 데이터 (카테고리별)
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

st.set_page_config(page_title="점심 룰렛", layout="centered")
st.title("🎡 오늘의 점심 룰렛")

# 카테고리 선택
selected_categories = st.multiselect("먹고 싶은 음식 종류를 골라보세요:", menu_data.keys(), default=list(menu_data.keys()))

# 선택된 메뉴 구성
filtered_menu = []
for cat in selected_categories:
    filtered_menu.extend(menu_data[cat])

if not filtered_menu:
    st.warning("메뉴가 없습니다. 최소 한 가지 카테고리를 선택해주세요.")
    st.stop()

# 룰렛 실행 버튼
if st.button("룰렛 돌리기 🎯"):
    selected_menu = random.choice(filtered_menu)
    menu_json = json.dumps(filtered_menu, ensure_ascii=False)

    # 룰렛 HTML/JS 삽입 (basic animation)
    html_code = f"""
    <html>
    <head>
    <style>
        .wheel {{
            margin: auto;
            border: 10px solid #555;
            border-radius: 50%;
            width: 300px;
            height: 300px;
            position: relative;
            animation: spin 4s cubic-bezier(0.33, 1, 0.68, 1);
        }}

        .center {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }}

        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate({random.randint(720, 1440)}deg); }}
        }}
    </style>
    </head>
    <body>
        <div class="wheel">
            <div class="center">{selected_menu}</div>
        </div>
    </body>
    </html>
    """

    components.html(html_code, height=350)

    st.success(f"🥳 오늘의 점심은 **{selected_menu}** 입니다!")

# 현재 메뉴 목록 보기
with st.expander("📋 현재 메뉴 목록"):
    for cat in selected_categories:
        st.write(f"**{cat}**: {', '.join(menu_data[cat])}")
