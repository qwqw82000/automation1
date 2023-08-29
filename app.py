import streamlit as st
def python_graph(data,whatGraph):
    import plotly.graph_objects as go
    # 데이터 추출
    topics = list(data[whatGraph].keys())
    scores = list(data[whatGraph].values())
    # 색상 설정 함수
    def get_color(score):
        if score > 3:
            return 'blue'
        elif score < 3:
            return 'red'
        else:
            return 'white'
    # 바 그래프 생성
    fig = go.Figure(data=go.Bar(
        x=topics,
        y=scores,
        marker=dict(color=[get_color(score) for score in scores])
    ))
    # 레이아웃 설정
    fig.update_layout(
        title=whatGraph,
        xaxis_title="주제",
        yaxis_title="점수",
        font=dict(size=30),
    )
    # 그래프 출력
    fig.show()
def python_evaluation():
    data = {"파이썬":{"입력" : 5 , "출력" : 5, "숫자형" : 5, "문자열" : 5, "리스트": 4, "조건문" : 3, "반복문" : 3, "함수" : 1}}
    st.markdown("<h1 style='text-align: center; color: red;'>학생의 파이썬 이해수준을 평가합니다. 1(부족), 2(정진), 3(보통), 4(실력자), 5(마스터)</h1>", unsafe_allow_html=True)
    data["파이썬"]["입력"] = (radioButton("학생의 파이썬 학습 현황(입력)"))
    data["파이썬"]["출력"] = (radioButton("학생의 파이썬 학습 현황(출력)"))
    data["파이썬"]["숫자형"] = (radioButton("학생의 파이썬 학습 현황(숫자형)"))
    data["파이썬"]["문자열"] = (radioButton("학생의 파이썬 학습 현황(문자열)"))
    data["파이썬"]["리스트"] = (radioButton("학생의 파이썬 학습 현황(리스트)"))
    data["파이썬"]["조건문"] = (radioButton("학생의 파이썬 학습 현황(조건문)"))
    data["파이썬"]["반복문"] = (radioButton("학생의 파이썬 학습 현황(반복문)"))
    data["파이썬"]["함수"] = (radioButton("학생의 파이썬 학습 현황(함수)"))
    return python_graph(data,"파이썬")
    
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
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "학생 이름 ")

    # 버튼 클릭 이벤트 처리
    if st.button("확인"):
        st.write(f"{name}학생에 대한 평가를 시작합니다!")
    # 학생의 파이썬 수준 측정
    python_evaluation()

    
    

if __name__ == "__main__":
    main()
