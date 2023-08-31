import streamlit as st
def python_graph(data,whatGraph):
    import plotly.graph_objects as go
    # 데이터 추출
    topics = list(data[whatGraph].keys())
    scores = list(data[whatGraph].values())
    # 색상 설정 함수
    def get_color(score):
        if score >= 3:
            return 'blue'
        else:
            return 'red'
    # 바 그래프 생성
    fig = go.Figure(data=go.Bar(
        x=topics,
        y=scores,
        marker=dict(color=[get_color(score) for score in scores])
    ))
    # 레이아웃 설정
    fig.update_layout(
        title=f"학생의 {whatGraph}평가(5점만점)",
        xaxis_title="주제",
        yaxis_title="점수",
        font=dict(size=30),
    )
    # 축 범위 지정
    fig.update_yaxes(range=[1, 5])
    # 그래프 출력
    st.plotly_chart(fig)
def python_evaluation():
    data = {"파이썬":{"입력" : 0 , "출력" : 0, "숫자형" : 0, "문자열" : 0, "리스트": 0, "조건문" : 0, "반복문" : 0, "함수" : 0}}
    st.markdown("<h2 style='text-align: center; color: red;'>학생의 파이썬 이해수준을 평가합니다. 1(부족), 2(정진), 3(보통), 4(실력자), 5(마스터)</h2>", unsafe_allow_html=True)
    data["파이썬"]["입력"] = (radioButton("1. 학생의 파이썬 학습 현황(입력)"))
    data["파이썬"]["출력"] = (radioButton("2. 학생의 파이썬 학습 현황(출력)"))
    data["파이썬"]["숫자형"] = (radioButton("3. 학생의 파이썬 학습 현황(숫자형)"))
    data["파이썬"]["문자열"] = (radioButton("4. 학생의 파이썬 학습 현황(문자열)"))
    data["파이썬"]["리스트"] = (radioButton("5. 학생의 파이썬 학습 현황(리스트)"))
    data["파이썬"]["조건문"] = (radioButton("6. 학생의 파이썬 학습 현황(조건문)"))
    data["파이썬"]["반복문"] = (radioButton("7. 학생의 파이썬 학습 현황(반복문)"))
    data["파이썬"]["함수"] = (radioButton("8. 학생의 파이썬 학습 현황(함수)"))
    if st.button("파이썬 평가 완료"):
        return python_graph(data,"파이썬")
        
def readTxt(codingAcademy,studentName):
    # 텍스트 파일 열기
    with open("greeting.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return content.format(codingAcademy = codingAcademy, studentName =studentName)
def radioButton(word):
    # Radio 버튼 생성
    option = st.radio(word, (1, 2, 3, 4, 5))
    
    # 선택된 옵션에 따라 동작 수행
    if option == 1:
        st.write("1점이 선택되었습니다.")
    elif option == 2:
        st.write("2점이 선택되었습니다.")
    elif option == 3:
        st.write("3점이 선택되었습니다.")
    elif option == 4:
        st.write("4점이 선택되었습니다.")
    else:
        st.write("5점이 선택되었습니다.")
    return option

def main():
    st.title("학생 평가 앱")
    st.write("안녕하세요! 다빈치 코딩 학생 평가용 웹입니다!")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "학생 이름 ")

    # 버튼 클릭 이벤트 처리
    if st.button("확인"):
        st.write(f"{name}학생에 대한 평가를 시작합니다!")
    # 학생의 파이썬 수준 측정

    python_evaluation()





    # 버튼 클릭 여부 확인
    button_clicked = st.button("모든 평가 마치기")

    # 버튼이 클릭되면 새로운 페이지 표시
    if button_clicked:
        # 1. 들어가는 인사
        greeting_txt = readTxt(codingAcademy = "다빈치 코딩학원",studentName = name)
        st.markdown(greeting_txt)
        # 2. 코딩 공부 현황
    

    
    

if __name__ == "__main__":
    main()
