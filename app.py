import streamlit as st
from studentEvaluation import studentEvaluation, readTxt, urlButton, redirect_button, loadSheet,searchStudent

def main():
    
    # url 버튼 4개 만들기
    # urlButton()
    redirect_button("https://github.com/qwqw82000/automation1","깃허브 연결")
    redirect_button("https://docs.google.com/spreadsheets/d/1dqNCXz-_Ja61498ermgteu01q2adZjElScz4fuCfR9Q","엑셀 공유 시트")
    redirect_button("https://forms.gle/rBwPcdsPYpNXURjj9","설문 폼(미평가 학생의 경우)")
    redirect_button("https://streamlit.io/cloud","streamlit cloud")

    # 웹 화면 시작
    st.title("학생 평가 웹")
    st.write("안녕하세요! 다빈치 코딩 학생 평가용 웹입니다!")

    # 텍스트 입력 받기
    studentName = st.text_input("학생 이름 입력", "유지민")
    # 다중 선택 생성
    stringList = st.multiselect('평가하고자 하는 스택 선택', ['파이썬 기초', 'c언어 기초', '자료구조','태도'])

    button_clicked = st.button("모든 평가 마치기")
    # 학생 평가 함수(인자 : 학생이름, 평가 언어및 스택)
    if button_clicked:
        # 1. 들어가는 인사
        st.markdown(
        f"""
            <h2 id="-studentname-">들어가는 인사</h2>
        """,
        unsafe_allow_html=True
        )
        greeting_txt = readTxt(codingAcademy = "다빈치 코딩학원",studentName = studentName)
        st.markdown(greeting_txt)
        # 2. 종합 평가
        st.markdown(
        f"""
            <h2 id="-studentname-">다빈치 코딩 {studentName}학생의 종합 평가</h2>
        """,
        unsafe_allow_html=True
        )
        # 과목 순회 종합 평가
        for string in stringList:
            studentEvaluation(studentName,string)
        # 담당 선생님 의견
        df = loadSheet()
        df = searchStudent(df,studentName)
        df = df.reset_index()
        st.markdown(
        f"""
            <h2 id="-studentname-">다빈치 코딩 {studentName}학생의 담당 선생님 의견</h2>
        """,
        unsafe_allow_html=True
        )
        if df.loc[0, '담당 선생님 의견'] != '':
            st.write(df.loc[0, '담당 선생님 의견'])
            st.write(df)
        else:
            st.write("담당 선생님 의견 미작성")
    
if __name__ == "__main__":
    main()
