import streamlit as st
from PIL import Image
import random

# -------------------------------
# 동물 캐릭터 정보 정의
# -------------------------------
animals = [
    {
        "name": "강아지 🐶",
        "desc": "활발하고 긍정적인 에너지를 가진 당신!",
        "personality": "사람을 좋아하고 쉽게 친해지는 타입이에요.",
        "quote": "세상을 꼬리를 흔들며 맞이하세요!"
    },
    {
        "name": "고양이 🐱",
        "desc": "자유롭고 도도한 매력의 소유자!",
        "personality": "혼자 있는 걸 좋아하지만, 진짜로 마음 열면 깊은 애정을 보여요.",
        "quote": "혼자 있어도 나는 나답게 빛나죠."
    },
    {
        "name": "부엉이 🦉",
        "desc": "차분하고 지적인 관찰자!",
        "personality": "분석적이고 깊은 생각을 많이 하는 스타일이에요.",
        "quote": "지혜로운 눈은 어둠 속에서도 빛나죠."
    },
    {
        "name": "판다 🐼",
        "desc": "편안하고 사랑스러운 분위기!",
        "personality": "느긋한 성격이지만 은근히 고집이 있어요.",
        "quote": "세상에 나만의 템포가 있어요."
    },
    {
        "name": "펭귄 🐧",
        "desc": "꾸준함과 귀여움이 공존하는 당신!",
        "personality": "협동심이 좋고 팀워크를 중시해요.",
        "quote": "한 걸음씩 함께 걷는 게 나의 방식!"
    },
    {
        "name": "고릴라 🦍",
        "desc": "강력한 리더십과 신뢰의 상징!",
        "personality": "책임감 있고 어려운 상황에서도 흔들리지 않아요.",
        "quote": "강함은 배려에서 온다."
    }
]

# -------------------------------
# UI 설정
# -------------------------------
st.set_page_config(page_title="🐾 닮은 동물 매칭기", layout="centered")
st.title("🐾 당신과 닮은 동물은?")
st.markdown("당신의 사진과 이름을 입력하면, AI 동물 분석가가 닮은 동물을 매칭해드릴게요! 🧠")

# -------------------------------
# 사용자 입력
# -------------------------------
name = st.text_input("당신의 이름을 입력해주세요 ✍️", "")

uploaded_file = st.file_uploader("📸 얼굴이 나온 사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

# -------------------------------
# 매칭 로직 실행
# -------------------------------
if name and uploaded_file:
    st.image(Image.open(uploaded_file), caption="✨ 분석할 사진", use_column_width=True)

    if st.button("🔍 나와 닮은 동물 보기"):
        result = random.choice(animals)

        st.markdown("---")
        st.subheader(f"🎉 {name} 님은... **{result['name']}** 닮았어요!")
        st.markdown(f"**성격 특징**: {result['desc']}")
        st.markdown(f"**당신의 성향**: {result['personality']}")
        st.info(f"💬 오늘의 메시지: *{result['quote']}*")
        st.balloons()

elif not name:
    st.info("이름을 입력해주세요 😊")
elif not uploaded_file:
    st.info("사진을 업로드하면 분석이 시작됩니다!")
