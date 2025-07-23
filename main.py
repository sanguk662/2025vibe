import streamlit as st
import datetime
import uuid

st.set_page_config(page_title="✅ 나의 할 일 관리 앱", layout="centered")
st.title("✅ 나의 할 일 관리 앱")

# ---------------------------
# 초기 세션 상태 설정
# ---------------------------
if "todos" not in st.session_state:
    st.session_state.todos = []

# ---------------------------
# 할 일 추가 폼
# ---------------------------
with st.form("add_task"):
    col1, col2 = st.columns([3, 1])
    with col1:
        task_text = st.text_input("할 일을 입력하세요 ✍️")
    with col2:
        due_date = st.date_input("기한", datetime.date.today())
    submitted = st.form_submit_button("➕ 추가하기")

    if submitted and task_text.strip():
        st.session_state.todos.append({
            "id": str(uuid.uuid4()),  # ✅ 중복 방지를 위한 고유 ID
            "text": task_text.strip(),
            "done": False,
            "date": due_date
        })
        st.success(f"'{task_text}' 추가되었습니다!")

st.markdown("---")

# ---------------------------
# 할 일 출력 함수
# ---------------------------
def show_tasks(filter_fn):
    found = False
    for item in st.session_state.todos:
        if filter_fn(item):
            found = True
            task_id = item["id"]
            cols = st.columns([0.1, 0.7, 0.1])
            done = cols[0].checkbox(
                "", value=item["done"], key=f"done_{task_id}"
            )
            if done:
                cols[1].markdown(f"~~{item['text']}~~ (🗓 {item['date']})")
            else:
                cols[1].markdown(f"{item['text']} (🗓 {item['date']})")

