import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='대륙별 공학자들!',
                   page_icon='https://cdn.pixabay.com/photo/2016/06/22/08/40/atom-1472657_960_720.png')

st.title('대륙별 과학자들')

data = [
    {
        'category': '북아메리카',
        'url': 'https://mblogthumb-phinf.pstatic.net/20160527_14/sciencenter_1464333428896KvDVA_JPEG/google_co_kr_20160527_161513.jpg?type=w2',
        'name': '니콜라 테슬라',
        'contry': '미국의 물리학자',
        'content': '교류전기 발명<br>'
                   '테슬라 코일 발명'
    },
    {
        'category': '유럽',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Coulomb.jpg/220px-Coulomb.jpg',
        'name': '샤를 드 쿨롱',
        'contry': '프랑스의 물리학자',
        'content': "전하를 띤 물체 사이에 작용하는 힘과 자석과 자석 사이에서 작용하는 인력과 척력을 측정해 '쿨롱의 법칙'을 발견"
    },
    {
        'category': '유럽',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Arrhenius2.jpg/200px-Arrhenius2.jpg',
        'name': '아레니우스',
        'contry': '스웨덴의 화학자',
        'content': '1903년, 전기해리 이론을 통해 노벨화학상을 받으면서 스웨덴 최초로 노벨상을 수상<br>'
                   '아레니우스 산염기, 아레니우스 식 등을 만듦'
    },
    {
        'category': '북아메리카',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/220px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg',
        'name': '아인슈타인',
        'contry': '미국의 물리학자',
        'content': '상대성 이론 발표<br>'
                   '광전 효과 법칙의 발견'
    },
    {
        'category': '유럽',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Gregor_Mendel_2.jpg/240px-Gregor_Mendel_2.jpg',
        'name': '그레고어 멘델',
        'contry': '오스트리아의 식물학자',
        'content': "유전의 기본 원리 발견 '멘델의 유전법칙'"
    },
    {
        'category': '아프리카',
        'url': 'https://w.namu.la/s/253d5043daa2fc1ffa00288b6cee40f0fcee1986e39bf6c468b756bc8287487266cf7b05dd5dd97b48d0688e6686eebd4ecd2bf2a21f8ebdc4b32cbd908f8474140826e891d72e6dffab33174010f25c441dd1efe2e7269cf8669c2409259636',
        'name': '케빈 리차드슨',
        'contry': '남아프리카공화국의 자연생태학자',
        'content': '동물 다큐멘터리 제작<br>'
                   '사자와의 교감이 뛰어남<br>'
                   "'The Lion Whisperer'이라는 유튜브 채널 운영"
    },
    {
        'category': '오세아니아',
        'url': 'https://w.namu.la/s/41973ba7a3d3342a83a67021bfaf5a5dfc9e307b186a2b8b6bf3fdc3c639dadc36e1f3114febcb7cd15dfd7d73f321d59a5c2d76d753434dd3220e01ab970a3bad4acbb5ed64c730b37dd0fb4d39fdb6f73c5bc858b883b925869b8d21a29a47',
        'name': '러더퍼드',
        'contry': '뉴질랜드의 물리학자,화학자',
        'content': '알파입자 산란실험으로 원자 내부에 원자핵을 발견<br>'
                   '1908 노벨화학상을 수상'
    },
    {
        'category': '아시아',
        'url': 'https://w.namu.la/s/5d8809523836f2b25ff9f28d9626d8c318a60081605b30052c932bfe221801290d0c9fb65d7750552f0626f995e1ab6a9b34625fd634691c128aea171444e68f0966810365aa5cf54ce1242543db7453b4b875ab900749608935dfc4f0259f1d',
        'name': '혼다 소이치로',
        'contry': '일본의 공학자',
        'content': "기업'HONDA'의 창업자<br>"
                   "세계 최초로 '보행자 더미(Dummy)'를 만들어 충돌 테스트를 진행, 보행자 부상과 직결되는 차체 부분을 파악하고 분석, 사고대비 차체를 설계해 모든 차종에 적용"
    },
    {
        'category': '아시아',
        'url': 'http://img.seoul.co.kr//img/upload/2016/01/27/SSI_20160127173928.jpg',
        'name': '조광래',
        'contry': '대한민국의 항공우주연구원',
        'content': "한국의 첫 고체연료 로켓인 'KSR-1'을 개발<br>"
                   "나로호 개발, 발사의 모든 현장에 기여"
    },
    {
        'category': '남아메리카',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/LowResMarcelo-Gleiser.jpg/250px-LowResMarcelo-Gleiser.jpg',
        'name': '마르셀루 글레이제르',
        'contry': '브라질의 물리학자',
        'content': '우주의 기원에서부터 과학과 영성의 상호 관여에 이르기까지 많은 저서를 출판한 다트머스 대학교 물리학, 천문학 교수'
    }
]


def card_list(menu):
    result = ''
    for value in data:
        if value['category'] == menu:
            result = result + f"""
    <div class="col">
    <div class="card" style="width: 18rem;">
  <img src="{value['url']}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{value['name']}</h5>
    <p class="card-text">{value['contry']}</p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">{value['content']}</li>
  </ul>
</div>
</div>
"""
    return result


menu = st.sidebar.selectbox('선택', ('아시아', '북아메리카', '남아메리카', '유럽', '아프리카', '오세아니아'))

components.html(
    f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    <div class="container">
  <div class="row">    
      {card_list(menu)}

  </div>
</div>
    """, height=1000
)