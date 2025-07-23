import streamlit as st
import datetime

st.set_page_config(page_title="🗓️ 할 일 관리 앱", layout="centered")

st.title("✅ 나의 할 일 관리 앱")
st.caption("오늘 할 일, 계획된 일, 완료된 일까지 체계적으로 관리하세요!")

# -----------------------
# 초기화
# -----------------------
if "todos" not in st.session_state:
    st.session_state.todos = []

# -----------------------
# 할 일 추가 폼
# -----------------------
with st.form("add_task"):
    col1, col2 = st.columns([3, 1])
    with col1:
        task_text = st.text_input("할 일을 입력하세요 ✍️")
    with col2:
        due_date = st.date_input("기한", datetime.date.today())
    submitted = st.form_submit_button("➕ 추가하기")

    if submitted and task_text.strip():
        st.session_state.todos.append({
            "text": task_text,
            "done": False,
            "date": due_date
        })
        st.success(f"'{task_text}' 추가됨!")

st.markdown("---")

# -----------------------
# 탭으로 구분
# -----------------------
tabs = st.tabs(["📅 오늘 할 일", "📆 예정된 할 일", "✅ 완료된 할 일"])

today = datetime.date.today()

# -----------------------
# 필터링 함수
# -----------------------
def show_tasks(condition_fn):
    found = False
    for idx, item in enumerate(st.session_state.todos):
        if condition_fn(item):
            found = True
            cols = st.columns([0.1, 0.7, 0.1, 0.1])
            done = cols[0].checkbox("", value=item["done"], key=f"task_{idx}")
            if done:
                cols[1].markdown(f"~~{item['text']}~~ (🗓️ {item['date']})")
            else:
                cols[1].markdown(f"{item['text']}  (🗓️ {item['date']})")
            delete = cols[2].button("🗑️", key=f"del_{idx}")
            if delete:
                st.session_state.todos.pop(idx)
                st.experimental_rerun()
            st.session_state.todos[idx]["done"] = done
    if not found:
        st.info("할 일이 없습니다!")

# -----------------------
# 오늘 탭
# -----------------------
with tabs[0]:
    st.subheader("📅 오늘 해야 할 일")
    show_tasks(lambda x: not x["done"] and x["date"] == today)

# -----------------------
# 예정 탭
# -----------------------
with tabs[1]:
    st.subheader("📆 앞으로의 할 일")
    show_tasks(lambda x: not x["done"] and x["date"] > today)

# -----------------------
# 완료 탭
# -----------------------
with tabs[2]:
    st.subheader("✅ 완료된 일")
    show_tasks(lambda x: x["done"])

st.markdown("---")

# -----------------------
# 통계
# -----------------------
total = len(st.session_state.todos)
done = len([x for x in st.session_state.todos if x["done"]])
if total:
    percent = int((done / total) * 100)
    st.progress(percent / 100)
    st.write(f"총 {total}개 중 {done}개 완료 (✅ {percent}%)")
else:
    st.write("할 일이 아직 없어요 😎")


