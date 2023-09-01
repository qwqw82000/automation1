import streamlit as st
from studentEvaluation import studentEvaluation, readTxt, urlButton

def main():
    # url 버튼 4개 만들기
    urlButton()
    # 웹 화면 시작
    st.title("학생 평가 앱")
    st.write("안녕하세요! 다빈치 코딩 학생 평가용 웹입니다!")

    # 텍스트 입력 받기
    studentName = st.text_input("학생 이름 입력", "김종하")
    string = st.text_input("평가 언어 및 스택", "파이썬")

    button_clicked = st.button("모든 평가 마치기")
    # 학생 평가 함수(인자 : 학생이름, 평가 언어및 스택)
    if button_clicked:
        # 1. 들어가는 인사
        greeting_txt = readTxt(codingAcademy = "다빈치 코딩학원",studentName = studentName)
        st.markdown(greeting_txt)
        studentEvaluation(studentName,string)
    

if __name__ == "__main__":
    main()
