import requests
from bs4 import BeautifulSoup


def han_search(keyword):
    url = 'http://search.hani.co.kr/Search?command=query&media=news&sort=d&period=all'

    for page in range(5):
        print(f'\n ====== page : {page+1} =====')
        params = {'keyword': keyword,
                  'pageseq': page}
        response = requests.get(url, params=params)     # 서버로 요청(request)을 보낸 후, 응답(response)를 받음
        html = response.text.strip()                    # 응답에서 html 문서 추출

        soup = BeautifulSoup(html, 'html5lib')          # HTML문서를 분석하기 위한 BeautifulSoup 객체 생성

        news_link = soup.select('.search-result-list li dl dt a')      # news_link는 list
        for link in news_link:
            link_url = link.get('href')
            link_title = link.text
            print(link_url, link_title)

            content_url = link_url                               # 여기서 부터 내용은 han_search()밖에서 다른 함수로 만들어서 넣어도 됨
            html = requests.get(content_url).text.strip()
            soup = BeautifulSoup(html, 'html5lib')
            news_contents = soup.select('.a-left #a-left-scroll-in .article-text .text')
            # print(news_contents)
            for contents in news_contents:
                news = contents.text
                print(news)


if __name__ == '__main__':
    han_search('머신러닝')
    # with open('result.txt', mode='w', encoding='UTF-8', newline='') as f:
    #     f.write(result)
