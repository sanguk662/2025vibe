def show_tasks(title, filter_fn):
    st.subheader(title)
    found = False

    for item in st.session_state.todos:
        if "id" in item and filter_fn(item):
            found = True
            task_id = item["id"]
            unique_key = f"{task_id}_{title.replace(' ', '_')}"  # 고유 키 보장

            cols = st.columns([0.08, 0.75, 0.1])

            # ✅ 체크박스
            done = cols[0].checkbox("✅", value=item["done"], key=f"done_{unique_key}")
            if done:
                cols[1].markdown(f"~~{item['text']}~~ (📅 {item['date']})")
            else:
                cols[1].markdown(f"{item['text']} (📅 {item['date']})")

            # 🗑 삭제 버튼
            if cols[2].button("🗑️", key=f"del_{unique_key}"):
                st.session_state.todos = [
                    t for t in st.session_state.todos if t.get("id") != task_id
                ]
                st.experimental_rerun()

            # 상태 저장
            item["done"] = done

    if not found:
        st.info("할 일이 없습니다!")
