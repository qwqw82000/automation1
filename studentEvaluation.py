import pandas as pd
import streamlit as st
def loadSheet():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    # 구글 서비스 계정의 JSON 키 파일 경로
    json_keyfile = 'service_account_key.json'

    # 스코프(scope) 설정
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # 인증 정보 생성
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)

    # 인증 정보로 세션 생성
    client = gspread.authorize(credentials)

    # 구글 스프레드시트 문서의 URL
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-mDi2Tt_arrQmdtTHR-wlmSo0I-dx5CV0cny9btCD3k/edit'

    # 시트 이름 (또는 인덱스) 지정 (예: 첫 번째 시트)
    worksheet_name = '설문지 응답 시트1'

    # 시트 열기
    worksheet = client.open_by_url(spreadsheet_url).worksheet(worksheet_name)

    # 데이터 가져오기 (데이터프레임 형태로 반환)
    dataframe = pd.DataFrame(worksheet.get_all_records())

    # 데이터 확인
    dataframe.head()
    return dataframe
def python_graph(studentName, data,whatGraph):
    import plotly.graph_objects as go
    # 데이터 추출
    topics = list(data.columns)
    data = data.replace('', 0)
    scores = list(data.iloc[0])
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
        title=f"{studentName}학생의 {whatGraph}평가(5점만점)",
        xaxis_title="주제",
        yaxis_title="점수",
        font=dict(size=30),
    )
    # 축 범위 지정
    fig.update_yaxes(range=[1, 5])
    # 그래프 출력
    st.plotly_chart(fig)
    # fig.show()
# 원하는 학생 찾기
def searchStudent(df,name):
    result = df.loc[df['담당 학생의 이름은?'] == name]
    return result
def searchSpecificColumn(df,string):
    # 데이터프레임에서 특정 문자열을 포함하는 열들 가져오기 (예: 'target_string')
    result = df.filter(like=string, axis=1)
    return result
def Preprocessing(df):
    df.replace({'부족': 1, '정진': 2, '보통': 3, '실력자': 4, '마스터': 5}, inplace=True)
    return df
def replaceColumnName(df,string):
    old_list = list(df.columns)
    # 리스트 내부에서 특정 문자열 제거 (예: 'target_string')
    new_list = [x.replace(string, "") for x in old_list]
    df.columns = new_list
    return df


def studentEvaluation(studentName,string):
    dataframe = loadSheet()
    # 부족,정진, 보통, 실력자, 마스터 전처리
    Preprocessing(dataframe)
    # 학생 찾기
    studentDataframe = searchStudent(dataframe,studentName)
    # 특정 과목 컬럼 찾기
    targetDf = searchSpecificColumn(studentDataframe,string)
    # 컬럼이름 적게 변경
    replaceColumnName(targetDf,string)
    # 파이썬 그래프 그리기
    python_graph(studentName,targetDf, whatGraph = string)

def readTxt(codingAcademy,studentName):
    # 텍스트 파일 열기
    with open("greeting.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return content.format(codingAcademy = codingAcademy, studentName =studentName)
def urlButton():
    import webbrowser
    # 버튼 생성
    button_labels = ['깃허브 연결', '엑셀 공유 시트', 'streamlit cloud','설문 폼']  # 버튼 라벨 리스트
    buttons = [st.button(label) for label in button_labels]
    # 각 버튼에 대한 동작 정의
    urls = ['https://github.com/qwqw82000/automation1', 'https://docs.google.com/spreadsheets/d/1-mDi2Tt_arrQmdtTHR-wlmSo0I-dx5CV0cny9btCD3k/edit#gid=543926080', 'https://streamlit.io/cloud','https://forms.gle/rBwPcdsPYpNXURjj9']

    for i, button in enumerate(buttons):
        if button:
            url = urls[i]  # 해당 버튼에 대응하는 URL 가져오기
            webbrowser.open_new_tab(url)  # 웹 브라우저를 새 탭으로 열어주는 함수 호출
