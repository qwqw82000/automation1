import streamlit as st
def main():
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "뤼튼")

    # 버튼 클릭 이벤트 처리
    if st.button("확인"):
        st.write(f"{name}학생에 대한 평가를 시작합니다!")
    # Radio 버튼 생성
    option = st.radio("선택하세요", ("1점", "2점", "3점", "4점"))
    
    # 선택된 옵션에 따라 동작 수행
    if option == "1점":
        st.write("1점이 선택되었습니다.")
    elif option == "2점":
        st.write("2점가 선택되었습니다.")
    elif option == "3점":
        st.write("3점이 선택되었습니다.")
    elif option == "4점":
        st.write("4점이 선택되었습니다.")
    else:
        st.write("5점이 선택되었습니다.")

if __name__ == "__main__":
    main()
