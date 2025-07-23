import streamlit as st
import random
import streamlit.components.v1 as components
import json

# 음식 데이터
menu_data = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기", "냉면"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "샐러드"],
    "기타": ["쌀국수", "타코", "케밥", "샌드위치", "분짜"]
}

st.set_page_config(page_title="점심 룰렛 추천기", layout="centered")
st.title("🎡 점심 룰렛 추천기")
st.caption("먹고 싶은 음식 종류를 선택하세요.")

# 사용자 선택
selected_categories = st.multiselect("음식 종류 선택", menu_data.keys(), default=list(menu_data.keys()))

# 메뉴 구성
filtered_menu = []
for cat in selected_categories:
    for item in menu_data[cat]:
        filtered_menu.append(f"{item} ({cat})")

if not filtered_menu:
    st.warning("음식 종류를 선택해주세요.")
    st.stop()

# 룰렛 HTML + JS
if st.button("🎯 룰렛 돌리기"):
    items_json = json.dumps(filtered_menu, ensure_ascii=False)
    html_code = f"""
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/wheel-spin@1.0.3/wheel.min.js"></script>
        <style>
            #wheel {{
                width: 400px;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <div id="wheel"></div>
        <script>
            const items = {items_json};
            const wheel = new Wheel({
                items: items,
                width: 400,
                radius: 150,
                centerWidth: 80,
                fontSize: 16,
                onSpinEnd: function(winner) {{
                    alert("오늘의 점심은: " + winner);
                }}
            });
            wheel.render(document.getElementById("wheel"));
            wheel.spin();
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=500)

# 현재 선택 메뉴 확인
with st.expander("📋 현재 선택된 메뉴 목록"):
    st.write(filtered_menu)
