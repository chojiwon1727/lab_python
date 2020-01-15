class Account:
    """ 은행 계좌 클래스
    field(데이터) : 계좌번호(accountno - 하나의 객체로 만들기), 잔액(balance)
    method(기능) : 입금(deposit) - 금액, 출금(withdraw) - 금액, 이체(transfer) - 계좌, 금액
    """

    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance
        # try:
        #     temp = balance + 1
        # except Exception:
        #     raise TypeError('')
        #  혹은
        # if not isinstance(balance, int) and \
        #     not isinstance(balance, float):
        #     raise TypeError('')

    def __repr__(self):
        return f'Account(account no.: {self.accountno}, balance: {self.balance})'

    def deposit(self, money):
        if money < 0:
            raise ValueError('입금 금액은 0보다 크거나 같아야 합니다')
        self.balance = self.balance + money
        print(f'balance : {self.balance}')

    def withdraw(self, money):
        if money < 0:
            raise ValueError('출금 금액은 0보다 크거나 같아야 합니다')
        elif self.balance < money:
            raise ValueError('출금 금액은 잔액보다 작거나 같아야 합니다')
        print(f'withdraw_price : {money}')
        self.balance = self.balance - money
        print(f'balance : {self.balance}')

    def transfer(self, other_account_no, money):
        """
        계좌이체기능
        :param other_account_no: 이체할 상대방 계좌
        :param money: 이체할 금액
        :return: None
        """
        print(f'transfer_price: {money}')
        print(f'balance : {self.balance - money}')




if __name__ == '__main__':
    account1 = Account(123456, 1000)
    print(account1)
    account1.deposit(500)
    account1.withdraw(600)

    account2 = Account(789000, 100)
    print(account2)
    account1.transfer(account2, 500)




































