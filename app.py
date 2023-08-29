import streamlit as st
def main():
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "뤼튼")

    # 버튼 클릭 이벤트 처리
    if st.button("인사"):
        st.write(f"안녕하세요, {name}님!")
    # Radio 버튼 생성
    option = st.radio("선택하세요", ("옵션 1", "옵션 2", "옵션 3"))
    
    # 선택된 옵션에 따라 동작 수행
    if option == "옵션 1":
        st.write("옵션 1이 선택되었습니다.")
    elif option == "옵션 2":
        st.write("옵션 2가 선택되었습니다.")
    else:
        st.write("옵션 3이 선택되었습니다.")

if __name__ == "__main__":
    main()
