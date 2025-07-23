import streamlit as st
import cv2
import numpy as np
from PIL import Image
import random
import io

# 닮은 동물 리스트
animals = [
    {"name": "강아지 🐶", "desc": "활발하고 귀여운 에너지 뿜뿜!", "match_score": lambda f: f[0] < 100},
    {"name": "고양이 🐱", "desc": "도도하면서도 은근한 매력!", "match_score": lambda f: f[1] > 80},
    {"name": "부엉이 🦉", "desc": "지적인 눈빛! 밤에 더 강해요.", "match_score": lambda f: f[2] > 50},
    {"name": "펭귄 🐧", "desc": "귀엽고 꾸준한 성실함!", "match_score": lambda f: f[3] % 2 == 0},
    {"name": "고릴라 🦍", "desc": "강한 카리스마와 리더십!", "match_score": lambda f: f[0] > 130},
    {"name": "판다 🐼", "desc": "느긋하고 사랑스러운 매력!", "match_score": lambda f: f[1] < 50},
]

# Streamlit UI
st.set_page_config(page_title="🐾 나랑 닮은 동물은?", layout="centered")
st.title("🐾 나랑 닮은 동물은?")
st.write("사진을 올리면 당신과 닮은 동물을 알려드립니다! (재미용 😆)")

# 파일 업로드
uploaded_file = st.file_uploader("얼굴이 나오는 사진을 업로드 해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    # 이미지 OpenCV 변환
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # 얼굴 검출
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        st.warning("😢 얼굴이 감지되지 않았어요. 다시 찍어주세요.")
    else:
        st.success(f"얼굴 {len(faces)}개 감지됨! 분석 중...")

        # 얼굴 위치 기반 특징 생성 (가짜 특징값으로 처리)
        x, y, w, h = faces[0]
        fake_features = [w, h, x, y]  # 실제로는 랜덤 기준으로 흉내

        # 동물 매칭
        match = None
        for animal in animals:
            if animal["match_score"](fake_features):
                match = animal
                break

        if match is None:
            match = random.choice(animals)

        st.markdown("---")
        st.header(f"🐾 당신은... **{match['name']}** 닮았어요!")
        st.write(f"💬 {match['desc']}")
        st.markdown("---")
        st.balloons()
