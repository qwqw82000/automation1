
import streamlit as st

def main():
    st.title("Streamlit 앱")
    st.write("안녕하세요! 이곳에 내용을 작성할 수 있습니다.")

    # 텍스트 입력 받기
    name = st.text_input("이름 입력", "뤼튼")

    # 버튼 클릭 이벤트 처리
    if st.button("인사"):
        st.write(f"안녕하세요, {name}님!")

if __name__ == "__main__":
    main()

# if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    # introduce_prompt = """코딩학원에서 부모님들께 보내는 학생 통지문을 문자로 보낼때 서론 부분을 적어줘"""
    # generated_text_introduce = chat_gpt.generate_text(introduce_prompt, 'gpt-3.5-turbo',openai_api_key, 2000)# generate_text() 함수를 사용하여 기사 생성
    # print(generated_text_introduce)
    
