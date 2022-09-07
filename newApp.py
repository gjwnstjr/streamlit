import streamlit as st

st.text_input('이름')
st.text_input('학번')

kor1 = st.radio('1. 3학년 1학기 국어 과목 중 1과목 선택', ('화법과 작문', '언어와 매체'))
kor2 = st.radio('2. 3학년 2학기 국어 과목 중 1과목 선택', ('고전 읽기', '현대문학 감상'))
math1 = st.radio('3. 3학년 1학기 수학 과목 중 1과목 선택', ('확률과 통계', '미적분'))
math2 = st.radio('4. 3학년 2학기 수학 과목 중 1과목 선택', ('수학적사고와 적분', '수학적사고와 통계', '수학적사고와 기하'))
art = st.radio('5. 예술과목 중 1과목 선택(학기 구분 없음)', ('음악감상과 비평', '미술창작'))
rsch = st.write('6. 탐구 일반, 진로 과목 중 3과목 선택[택3](학기 구분 없음)')
st.checkbox('생활과 윤리')
st.checkbox('한국 지리')
st.checkbox('동아시아사')
st.checkbox('사회문화')
st.checkbox('물리학II')
st.checkbox('화학II')
st.checkbox('생명과학II')
st.checkbox('지구과학II')
st.write('*과학중점반은 과학 과목 중 3과목을 선택합니다.')

st.radio('7. 탐구 진로, 전문 과목 중 1과목 선택(학기 구분 없음)(일반반)', ('생활과 과학', '한국사회의 이해'))
st.write('*과학중점반은 선택하지 마세요.')

st.write('8. 다음 과목 중 두 과목 선택[택2](학기 구분 없음)(일반반)')
st.checkbox('심화국어')
st.checkbox('심화수학II')
st.checkbox('심화영어I')
st.write('*과학중점반은 선택하지 마세요.')




