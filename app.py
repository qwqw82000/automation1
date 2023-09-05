import streamlit as st
from studentEvaluation import studentEvaluation, readTxt, urlButton, redirect_button

def main():
    
    # url 버튼 4개 만들기
    # urlButton()
    redirect_button("https://github.com/qwqw82000/automation1","깃허브 연결")
    redirect_button("https://docs.google.com/spreadsheets/d/1-mDi2Tt_arrQmdtTHR-wlmSo0I-dx5CV0cny9btCD3k/edit#gid=543926080","엑셀 공유 시트")
    redirect_button("https://forms.gle/rBwPcdsPYpNXURjj9","설문 폼")
    redirect_button("https://streamlit.io/cloud","streamlit cloud")

    # 웹 화면 시작
    st.title("학생 평가 앱")
    st.write("안녕하세요! 다빈치 코딩 학생 평가용 웹입니다!")

    # 텍스트 입력 받기
    studentName = st.text_input("학생 이름 입력", "김종하")
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
        for string in stringList:
            studentEvaluation(studentName,string)
        # 담당 선생님 의견
        st.markdown(
        f"""
            <h2 id="-studentname-">다빈치 코딩 {studentName}학생의 담당 선생님 의견</h2>
            또래에 비해서 확실하게 뛰어난 집중력과 의지력 그리고 융퉁성 또한 갖춰져 있음, 본인이 더 성장하기 위해선 어려운 일도 도전하려하고 이를 즐기는 편임, 이런 성향에 협업능력(친화력)또한 좋아 미래의 발전가능성이 큰 편임, 현재 파이썬(기초는 거의 완벽, 모르더라도 바로바로 스스로 찾아서 해결 가능한 수준), 데이터분석, 인공지능, 가벼운 개발(앱 인벤터, 아두이노)등을 공부한 상태이며 코드페어 공모전 역시 2회참가, 빅콘테스트 데이터 분석 대회(장려상 수상)등의 이력이 있으며 향후 미래가 기대되는 친구임. 하지만 바쁜 일정때문에 꾸준히 출석하지는 못하고 있음(보충은 하는 상태). 현재는 c언어를 공부하며 컴퓨터의 내부 메모리에대한 공부를 하고 있으며 이후 개발에 대한 지식을 계속해서 공부할 계획(HTML, JAVASCRIPT, JAVA등 이미 객체 지향적인 개념이 어느정도 잡혀있기 때문에 어렵지 않게 적응할 수 있을 것이라고 생각함)프론트 엔드와 벡엔드에 대한 실습을 진행하고 풀스택을 모두 경험시켜서 개발 전반에 대한 흐름을 익힐 수 있도록 지도할 계획임
        """,
        unsafe_allow_html=True
        )
    
if __name__ == "__main__":
    main()
