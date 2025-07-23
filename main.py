import streamlit as st
import os

# 페이지 제목
st.title("📝 나의 할 일 목록 앱")
st.write("할 일을 입력하고 저장해보세요!")

# 파일 이름
FILENAME = "todo_list.txt"

# 할 일 입력
todo_input = st.text_input("할 일을 입력하세요:")

# 저장 버튼
if st.button("📥 저장하기"):
    if todo_input.strip() == "":
        st.warning("❗ 할 일을 입력해야 저장됩니다.")
    else:
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(todo_input + "\n")
        st.success("✅ 저장되었습니다!")

# 구분선
st.markdown("---")

# 저장된 할 일 목록 출력
st.subheader("📋 저장된 할 일 목록")

if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            for i, line in enumerate(lines, 1):
                st.write(f"{i}. {line.strip()}")
        else:
            st.info("할 일이 아직 없습니다.")
else:
    st.info("할 일이 아직 없습니다.")
