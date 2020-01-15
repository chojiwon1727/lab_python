"""
다음에서 '머신러닝'으로 검색한 기사 100개의 URL주소와 기사 제목 출력
웹 주소(URI/URL) : http://www.youtube.com/watch?v=k7...&a=...
 - https : 프로토콜 이름
 - www.youtube.com : 서버 주소[:포트번호] -> 포트번호 대부분 생략(보통 포트번호 80)
 - watch : 경로(path)  -> 단계는 여러개가 될 수도 있음
 - ? 뒷부분 : querystring -> user가 서버로 보내는 정보(어떤 내용을 보겠다고 서버에 보내는 내용)
     -> param이름=param값 형식으로 작성
     -> 여러개일수도 있음(여러개인 경우 &로 구분됨)
     -> 동일한 서버(네이버, 다음, 유튜브...)에서 다른 내용을 본다면 앞은 동일하고 querystring만 변함
"""

import requests
from bs4 import BeautifulSoup


def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1'
    for page in range(1,11):
        print(f'\n=== page : {page} ===')
        req_params = {'q': keyword,         # 검색어(키워드)를 쿼리 스트링에 파라미터로 전달
                      'p': page}            # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가
        response = requests.get(url, params=req_params)
        html = response.text.strip()
        soup = BeautifulSoup(html, 'html5lib')
        news_link = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_link:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)


if __name__ == '__main__':
    daum_search('산업심리학')

if False:
    # page = 0
    # for page in range(1,11):
    #     print(f'\n=== page : {page} ===')
    #     url_path = f'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&p={page}'
    #     page += 1
    #     # print(url_path)
    #
    #     html = requests.get(url_path).text.strip()
    #
    #     soup = BeautifulSoup(html, 'html5lib')
    #
    #     news_link = soup.select('.coll_cont ul li a.f_link_b')
    #     for link in news_link:
    #         print(link.get('href'), link.text)



    # url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&p='
    # for page in range(1,11):
    #     page_url = url + str(page)
    #     print(page_url)
    #     html = requests.get(page_url).text.strip()
    #
    #     soup = BeautifulSoup(html, 'html5lib')
    #
    #
    #     news_link = soup.select('.coll_cont ul li a.f_link_b')
    #     for link in news_link:
    #         print(link.get('href'), link.text)

    url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D'
    for page in range(1, 11):
        print(f'\n=== page : {page} ===')
        response = requests.get(url, params={'p': page})
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')

        news_link = soup.select('.coll_cont ul li a.f_link_b')
        for link in news_link:
            print(link.get('href'), link.text)






