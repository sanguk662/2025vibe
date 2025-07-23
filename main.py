import streamlit as st
import datetime

st.set_page_config(page_title="📝 할 일 목록", layout="centered")

st.title("✅ 나의 할 일 목록 앱")
st.caption("오늘 할 일을 추가하고, 완료 체크로 정리해보세요!")

# -----------------------
# 세션 상태 초기화
# -----------------------
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# -----------------------
# 할 일 추가
# -----------------------
with st.form("할 일 추가"):
    new_todo = st.text_input("할 일을 입력하세요 ✍️", "")
    submitted = st.form_submit_button("➕ 추가")
    if submitted and new_todo.strip():
        st.session_state.todo_list.append({"task": new_todo, "done": False})
        st.success(f"'{new_todo}' 추가됨!")

st.markdown("---")

# -----------------------
# 할 일 목록 보여주기
# -----------------------
st.subheader("📋 할 일 목록")

if st.session_state.todo_list:
    for idx, item in enumerate(st.session_state.todo_list):
        cols = st.columns([0.1, 0.8, 0.1])
        done = cols[0].checkbox("", value=item["done"], key=f"todo_{idx}")
        if done:
            cols[1].markdown(f"~~{item['task']}~~")
        else:
            cols[1].markdown(item["task"])
        delete = cols[2].button("❌", key=f"del_{idx}")
        # 상태 업데이트
        st.session_state.todo_list[idx]["done"] = done
        if delete:
            st.session_state.todo_list.pop(idx)
            st.experimental_rerun()
else:
    st.info("할 일이 아직 없습니다. 위에 입력해서 추가해보세요!")

