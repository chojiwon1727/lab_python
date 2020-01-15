"""
lec06_class\class07.py 파일에서 정의한 Acoount 클래스를 사용해서
은행 어플리케이션을 작성
1) 계좌개설
2) 입금
3) 출금
4) 이체
"""
from lec06_class.class07 import Account

print('Banking Application')
# 여러개의 계좌들을 관리하기 위한 dict 선언(dict_key: 계좌번호, dict_value: Account 객체)
accounts = {}

while True:     # 무한루프
    # 메인 메뉴
    print('[0] 종료')
    print('[1] 계좌 개설')
    print('[2] 입금')
    print('[3] 출금')
    print('[4] 이체')
    print('[5] 계좌 정보 출력')
    print('--------------')
    print('선택>>>')
    menu = input()
    if menu == '0':
        break
    elif menu == '1':
        print('--- 신규 계좌 개설 화면 ---')
        account_no = int(input('계좌번호 입력>>'))
        money = int(input('잔액 입력>>'))
        accounts[account_no] = Account(account_no, money)
        # print(accounts)
    elif menu == '5':
        print('---계좌 정보 조회 화면---')
        account_no = int(input('조회할 계좌번호 입력>>'))
        print(accounts[account_no])   # accounts dict에서 조회할 계좌번호인 account_no index 출력
    elif menu == '2':
        print('---입금 화면---')
        account_no = int(input('입금할 계좌번호 입력>>'))
        money = int(input('입금 금액 입력>>'))
        accounts[account_no].deposit(money)    # dict가 객체(account_no)와 Account class로 이뤄져있어서 가능
    elif menu == '3':
        print('---출금 화면---')
        account_no = int(input('출금할 계좌번호 입력>>'))
        money = int(input('출금 금액 입력>>'))
        accounts[account_no].withdraw(money)
    elif menu == '4':
        print('---이체 화면---')
        from_acc = int(input('내 계좌번호 입력>>'))
        to_acc = int(input('상대방 계좌번호 입력>>'))
        money = int(input('이체 금액 입력>>'))
        accounts[from_acc].transfer(accounts[to_acc], money)

print('Banking App 종료')