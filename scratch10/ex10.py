import requests
from bs4 import BeautifulSoup

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'

# 사이트(웹 서버)로 요청(request)를 보냄
html = requests.get(url).text.strip()  # 요청의 결과(응답, response - HTML)를 저장 -> .strip()은 앞뒤공백 제거
print(html[0:100])  # 전체 문자열에서 100자만 확인

# BeautifulSoup객체 생성
soup = BeautifulSoup(html, 'html5lib')

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
    print(link.get('href'))     # -> 모든 링크가 출력되기 때문에 어떤 href가 관심있는 것인지 분리해야 함


# CSS selector를 선택할 때는 찾고싶은 class의 value나 id의 HTML요소가 하나만 있는지 여러개가 있는지 보고 선택해야 함
div_coll_cont = soup.find_all(class_='coll_cont')     # soup.find_all(attrs={'class':'coll_cont'})와 동일
print(len(div_coll_cont))
print()
# 4출력 : div_coll_cont라는 부분이 4개가 있다는 의미 -> 원하는 class:'coll_cont'가 4개중에 몇번째인지 알아봐야 함
# 웹사이트 개발자 도구에서 Ctrl + F 해서 coll_cont를 검색해서 몇번째인지 알아봐야 함
# - 결과: 첫번째  -> 인덱스 0번만 사용하거나 HTNL 하위 요소(sub / child element)를 찾으면됨

# HTML 하위요소(sub / child element) 찾는 방법
# 1) parent_selector > child_selector(바로 아래쪽의 child element만 찾아갈 수 있음)
#    :    div > ul > li    혹은  .coll_cont > #clusterResultUL > .fst
#     -> 태그앞에는 아무것도 안쓰지만 class와 id는 .class와 #id 로 사용

# 2) ancestor_selector(조상 선택자) descendant_selector(자손 선택자) -> 조상선택자와 자손 선택자 사이에 공백만 주면 됨
#    :    div li    혹은    .coll_cont .fst       -> 몇단계를 생략하고 들어가도 됨

# soup.select(CSS selector) : soup객체에서 CSS선택자로 요소들을 찾는 방법
news_link = soup.select('.coll_cont ul li a.f_link_b')     # a태그를 찾아가서 a태그들 중에서 f_link_b class만 찾겠다는 의미
for link in news_link:
    print(link.get('href'))      # 한페이지의 뉴스 개수만큼 출력되면 제대로 출력한 것

# -> 여러 페이지의 내용을 출력하고 싶으면 1페이지와 2페이지, ...의 url이 어떻게 변화하는지를 보고 for문을 돌리면 됨
