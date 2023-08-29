import streamlit as st
def radioButton(word):
    # Radio 버튼 생성
    option = st.radio(word, ("1", "2", "3", "4", "5"))
    
    # 선택된 옵션에 따라 동작 수행
    if option == "1":
        st.write("1점이 선택되었습니다.")
    elif option == "2":
        st.write("2점이 선택되었습니다.")
    elif option == "3":
        st.write("3점이 선택되었습니다.")
    elif option == "4":
        st.write("4점이 선택되었습니다.")
    else:
        st.write("5점이 선택되었습니다.")
    return int(option)
def main():
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "학생 이름")

    # 버튼 클릭 이벤트 처리
    if st.button("확인"):
        st.write(f"{name}학생에 대한 평가를 시작합니다!")
    # 학생의 파이썬 수준 측정
    st.markdown("<h1 style='text-align: center; color: red;'>학생의 파이썬 이해수준을 평가합니다. 1(부족), 2(정진), 3(보통), 4(실력자), 5(마스터)</h1>", unsafe_allow_html=True)
    pythonScore = []
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(입력)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(출력)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(숫자형)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(문자열)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(리스트)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(조건문)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(반복문)"))
    pythonScore.append(radioButton("학생의 파이썬 학습 현황(함수)"))
    
    

if __name__ == "__main__":
    main()
