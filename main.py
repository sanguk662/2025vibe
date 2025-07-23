import streamlit as st
import random
import time

st.set_page_config(page_title="🧠 마음의 미니게임", layout="centered")
st.title("🎮 마음의 미니게임")
st.write("당신의 직관과 반응으로 알아보는 심리 테스트 🔍")

# ------------------------
# 🎨 미니게임 1: 색 선택 테스트
# ------------------------

st.header("🎨 미니게임 1: 끌리는 색을 선택하세요")

colors = {
    "🔴 빨강": "에너지가 넘치고 도전적인 상태예요.",
    "🔵 파랑": "차분하고 이성적인 상태입니다.",
    "🟢 초록": "안정과 회복이 필요한 시점이에요.",
    "🟡 노랑": "창의적이고 활기찬 기분이네요!",
    "⚫ 검정": "조용히 혼자 있고 싶은 마음일 수 있어요.",
    "⚪ 흰색": "새로운 시작을 원하거나 마음이 정리된 상태입니다."
}

selected_color = st.radio("지금 가장 끌리는 색은?", list(colors.keys()))

if selected_color:
    st.success(f"당신의 심리 상태 💡: {colors[selected_color]}")

st.markdown("---")

# ------------------------
# ⏱️ 미니게임 2: 반응 속도 테스트
# ------------------------

st.header("⏱️ 미니게임 2: 반응 속도 테스트")
st.write("버튼이 초록색으로 바뀌면 최대한 빨리 눌러보세요!")

if "game_started" not in st.session_state:
    st.session_state["game_started"] = False
    st.session_state["start_time"] = 0.0
    st.session_state["reaction_time"] = None

if not st.session_state["game_started"]:
    if st.button("게임 시작"):
        wait_time = random.randint(2, 5)
        st.session_state["game_started"] = True
        st.write("...")
        time.sleep(wait_time)
        st.session_state["start_time"] = time.time()
        st.session_state["ready"] = True
        st.experimental_rerun()

else:
    if "ready" in st.session_state and st.session_state["ready"]:
        if st.button("🟢 지금 클릭!"):
            reaction = time.time() - st.session_state["start_time"]
            st.session_state["reaction_time"] = reaction
            st.session_state["game_started"] = False
            st.session_state["ready"] = False
            st.success(f"⏱️ 당신의 반응 속도: {reaction:.3f}초")

            # 반응 속도 피드백
            if reaction < 0.3:
                st.write("⚡ 엄청난 집중력! 천재 반사신경!")
            elif reaction < 0.6:
                st.write("👍 좋은 반응 속도예요!")
            else:
                st.write("😴 조금 느렸어요... 쉬는 게 필요할 수도 있어요.")
