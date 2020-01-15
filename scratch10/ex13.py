"""
icrawler 패키지를 사용해서 google 이미지 검색 결과 다운로드
> pip install icrawler
"""
from icrawler.builtin import GoogleImageCrawler
import os

# 이미지 저장 경로(window의 경우에만 +os.sep )
save_dir = os.path.join('C:' + os.sep, 'dev', 'images')

# GoogleImageCrawler 객체 생성
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

# 검색 필터링 조건
filters = {
    'size':'large'}

google_crawler.crawl(keyword='은혁', filters=filters, max_num=50)


