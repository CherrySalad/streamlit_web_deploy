import streamlit as st

# 페이지 기본 설정하기
st.set_page_config(
    page_icon = '😎',
    page_title = '스트림릿 웹 배포 연습',
    layout = 'wide',
)


st.subheader('Documents')

if st.button('app.py 코드 보기'):
    code = '''
    import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from time import sleep

# 페이지 기본 설정하기
st.set_page_config(
    page_icon = '😎',
    page_title = '스트림릿 웹 배포 연습',
    layout = 'wide',
)

# 로딩바 구현하기
with st.spinner(text='잠시만 기다려주세요...'):
    sleep(2)


# 페이지 헤더, 서브헤더 제목 설정하기
st.header('방문을 환영합니다.😊')
st.subheader('스트림릿 기능 맛보기')

# 페이지를 컬럼 단위로 분할하기
cols = st.columns((1,1,2))
    # (1칸, 1칸, 2칸) 비율
cols[0].metric('10/11', '15 C', '2')
cols[0].metric('10/12', '17 C', '2')
cols[0].metric('10/13', '20 C', '3')
cols[1].metric('10/14', '17 C', '-3')
cols[1].metric('10/15', '19 C', '2')
cols[1].metric('10/16', '14 C', '-5')

# 라인 그래프 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)

# 컬럼의 나머지 빈 부분에 라인 차트 보여주기
cols[2].line_chart(chart_data)
    '''
    st.code(code, language = 'python')