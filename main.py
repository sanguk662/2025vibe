import streamlit as st

# 페이지 제목
st.title("📝 나의 할 일 목록 앱")

# 설명 텍스트
st.markdown("할 일을 입력하고 목록으로 저장해보세요. 프로그램은 종료 버튼 없이 웹 환경에서 동작합니다.")

# 입력 받기
todo = st.text_input("할 일을 입력하세요", "")

# 저장할 파일 경로
filename = "할일목록.txt"

# 저장 버튼을 누르면 할 일 저장
if st.button("할 일 저장하기"):
    if todo.strip() == "":
        st.warning("할 일을 입력하세요!")
    else:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(todo + "\n")
        st.success("✅ 저장되었습니다!")

# 현재 저장된 할 일 목록 보여주기
st.markdown("## 📋 현재 할 일 목록")

try:
    with open(filename, "r", encoding="utf-8") as f:
        todos = f.readlines()
        if todos:
            for i, line in enumerate(todos, 1):
                st.write(f"{i}. {line.strip()}")
        else:
            st.info("할 일이 아직 없습니다.")
except FileNotFoundError:
    st.info("아직 저장된 할 일이 없습니다.")
💡 실행 방법
