class Rectangle:
    """ 직사각형 클래스 """

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def info(self):
        print(f'Rectangle : (w={self.w}, h={self.h})')

    def area(self):
        return self.w * self.h

    # == 연산자를 사용했을 때 자동으로 호출되는 메소드
    def __eq__(self, other):
        return self.w == other.w and self.h == other.h

    # 객체의 내용을 print할 때 자동으로 호출되는 메소드
    def __str__(self):
        return f'<직사각형 가로 ={self.w}, 세로 = {self.h}'



if __name__ == '__main__':
    rect1 = Rectangle(3, 2)
    print(type(rect1))
    print(id(rect1))
    rect1.info()

    rect4 = Rectangle(2,3)
    print(rect4.area())

    rect5 = Rectangle(2,3)
    print(rect5.area())

    print(rect5)


# obj1 == obj2 비교하는 방법(== 연산자의 동작방식):
# obj1 == obj2 는 obj1.__eq__(obj2)와 동일   --> obj1이 self, obj2가 other
# ==연산자는 클래스의 __eq__ 함수를 호출
# 개발자가 클래스를 정의할 때 __eq__ 메소드를 정의하지 않아도
# 모든 클래스는 __eq__메소드를 가지고 있음
# 기본 __eq__메소드는 객체들의 주소값(id)를 비교함
# 개발자가 __eq__메소드를 다른 방식으로 작성하면 ==연산자는 개발자의 의도대로 True, False를 리턴하게 됨

