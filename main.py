import streamlit as st
import datetime
import uuid

# -----------------------
# 페이지 설정
# -----------------------
st.set_page_config(page_title="📆 할 일 체크리스트 앱", layout="centered")
st.title("✅ 할 일 체크리스트 앱")

# -----------------------
# 세션 상태 초기화 및 정리
# -----------------------
if "todos" not in st.session_state:
    st.session_state.todos = []
else:
    # id가 없는 잘못된 데이터 필터링
    st.session_state.todos = [t for t in st.session_state.todos if "id" in t]

# -----------------------
# 할 일 추가 폼
# -----------------------
with st.form("add_task_form"):
    col1, col2 = st.columns([3, 1])
    with col1:
        task_text = st.text_input("할 일을 입력하세요 ✍️")
    with col2:
        due_date = st.date_input("기한", datetime.date.today())

    submitted = st.form_submit_button("➕ 추가하기")

    if submitted:
        if task_text.strip():
            st.session_state.todos.append({
                "id": str(uuid.uuid4()),
                "text": task_text.strip(),
                "done": False,
                "date": due_date
            })
            st.success(f"'{task_text}' 할 일이 추가되었습니다!")
        else:
            st.warning("할 일 내용을 입력해주세요!")

st.markdown("---")

# -----------------------
# 할 일 출력 함수
# -----------------------
def show_tasks(title, filter_fn):
    st.subheader(title)
    found = False

    for item in st.session_state.todos:
        # 필터 조건
        if "id" in item and filter_fn(item):
            found = True
            task_id = item["id"]
            cols = st.columns([0.08, 0.75, 0.1])

            # 체크박스 (완료 여부)
            done = cols[0].checkbox("", value=item["done"], key=f"done_{task_id}")
            if done:
                cols[1].markdown(f"~~{item['text']}~~ (🗓 {item['date']})")
            else:
                cols[1].markdown(f"{item['text']} (🗓 {item['date']})")

            # 삭제 버튼
            if cols[2].button("🗑️", key=f"del_{task_id}"):
                st.session_state.todos = [t for t in st.session_state.todos if t.get("id") != task_id]
                st.experimental_rerun()

            # 상태 업데이트
            item["done"] = done

    if not found:
        st.info("할 일이 없습니다!")

# -----------------------
# 탭 구성
# -----------------------
today = datetime.date.today()
tab1, tab2, tab3 = st.tabs(["📌 오늘 할 일", "📆 예정된 할 일", "✅ 완료된 할 일"])

with tab1:
    show_tasks("📌 오늘 해야 할 일", lambda x: not x["done"] and x["date"] == today)

with tab2:
    show_tasks("📆 예정된 할 일", lambda x: not x["done"] and x["date"] > today)

with tab3:
    show_tasks("✅ 완료된 할 일", lambda x: x["done"])

# -----------------------
# 통계 출력
# -----------------------
total = len(st.ses

