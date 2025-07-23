import streamlit as st
import datetime
import hashlib

st.set_page_config(page_title="🗓️ 할 일 관리 앱", layout="centered")
st.title("✅ 나의 할 일 관리 앱")

# 세션 초기화
if "todos" not in st.session_state:
    st.session_state.todos = []

# 고유 key 생성 함수
def generate_key(task):
    return hashlib.md5(f"{task['text']}_{task['date']}".encode()).hexdigest()

# 할 일 추가
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

# 필터링된 목록 보여주기
def show_tasks(filter_fn):
    found = False
    for item in st.session_state.todos:
        if filter_fn(item):
            found = True
            task_key = generate_key(item)
            cols = st.columns([0.1, 0.7, 0.1])
            done = cols[0].checkbox("", value=item["done"], key=f"done_{task_key}")
            if done:
                cols[1].markdown(f"~~{item['text']}~~ (🗓️ {item['date']})")
            else:
                cols[1].markdown(f"{item['text']}  (🗓️ {item['date']})")
            if cols[2].button("🗑️", key=f"del_{task_key}"):
                st.session_state.todos.remove(item)
                st.experimental_rerun()
            item["done"] = done
    if not found:
        st.info("할 일이 없습니다!")

# 탭 구성
tabs = st.tabs(["📅 오늘 할 일", "📆 예정된 할 일", "✅ 완료된 할 일"])
today = datetime.date.today()

with tabs[0]:
    st.subheader("📅 오늘 해야 할 일")
    show_tasks(lambda x: not x["done"] and x["date"] == today)

with tabs[1]:
    st.subheader("📆 앞으로의 할 일")
    show_tasks(lambda x: not x["done"] and x["date"] > today)

with tabs[2]:
    st.subheader("✅ 완료된 일")
    show_tasks(lambda x: x["done"])

# 통계
total = len(st.session_state.todos)
done = len([x for x in st.session_state.todos if x["done"]])
if total:
    st.progress(done / total)
    st.write(f"총 {total}개 중 {done}개 완료 (✅ {int(done/total*100)}%)")
else:
    st.write("할 일이 아직 없어요 😊")
