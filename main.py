import streamlit as st
from PIL import Image
import random

# 동물 목록
animals = [
    {"name": "강아지 🐶", "desc": "활발하고 에너지 넘치는 당신!"},
    {"name": "고양이 🐱", "desc": "도도하고 묘한 매력을 지닌 스타일!"},
    {"name": "부엉이 🦉", "desc": "지적인 눈빛과 깊은 통찰력!"},
    {"name": "펭귄 🐧", "desc": "귀엽고 꾸준한 성실함이 매력!"},
    {"name": "판다 🐼", "desc": "느긋하고 사랑스러운 존재!"},
    {"name": "고릴라 🦍", "desc": "강한 리더십과 믿음직한 성격!"}
]

# Streamlit 설정
st.set_page_config(page_title="🐾 닮은 동물 매칭기", layout="centered")
st.title("🐾 당신과 닮은 동물은?")
st.write("사진을 업로드하면 랜덤으로 닮은 동물을 알려드립니다! (재미용 😊)")

# 파일 업로드
uploaded_file = st.file_uploader("📸 얼굴이 나오는 사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    if st.button("🔍 닮은 동물 분석하기"):
        result = random.choice(animals)
        st.markdown("---")
        st.header(f"✨ 당신은... **{result['name']}** 닮았어요!")
        st.write(f"💬 {result['desc']}")
        st.balloons()
else:
    st.info(
