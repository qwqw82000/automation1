import pandas as pd
import streamlit as st
import openpyxl
def main():
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "뤼튼")

    # 버튼 클릭 이벤트 처리
    if st.button("인사"):
        st.write(f"안녕하세요, {name}님!")
    #  csv 파일 업로드
    uploaded_file = st.file_uploader("파일 선택", type=["xlsx"])
    if uploaded_file is not None:
     df = pd.read_excel(uploaded_file)
     st.dataframe(df)  # DataFrame 출력 예시
     # 여기서부터는 데이터에 대한 추가적인 작업 수행 가능
    else:
     st.write("파일이 업로드되지 않았습니다.")


if __name__ == "__main__":
    main()
