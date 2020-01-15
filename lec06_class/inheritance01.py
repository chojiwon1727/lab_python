import math
"""
상속(inheritance)
"""


class Shape:
    def __init__(self, x=0, y=0):
        print('Shape.__init__ 호출')
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Shape(x={self.x}, y={self.y})'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        """
        shape 객체는 넓이를 계산할 수 없음
        shape의 sub class들이 각자의 방식으로 넓이 계산해야 함
        :return: 도형의 넓이
        """
        raise NotImplemented('area 메소드는 반드시 override')

    def draw(self):
        """
        넓이를 계산하는 area 메소드를 사용해서 도형 내부를 그려주는 메소드
        :return: None
        """
        print(f'Drawing area {self.area()}')

class Rectangle(Shape):
    def __init__(self, w=0, h=0, x=0, y=0):     # 직사각형을 만들려면 시작점(x,y)와 직사각형의 가로, 세로 길이가 필요
        print('Rectangle.__init__호출')
        super().__init__(x,y)     # 부모클래스의 __init__ 호출--> super()대신 Shape.__init__(self,x,y) 가능
        self.w = w
        self.h = h

    def __repr__(self):            # 부모로부터 상속받은 메소드를 자식클래스에서 재정의(override)
        return f'사각형(가로={self.w}, 세로={self.h}, x={self.x}, y= self.y) '

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r=0, x=0, y=0):
        print('Circle.__init__호출')
        super().__init__(x,y)    # super클래스의 __init__메소드를 반드시 호출해야 함
        self.r = r               # sub클래스만 갖는 field를 초기화

    def __repr__(self):
        return f'동그라미(반지름={self.r}, x={self.x}, y={self.y})'

    def area(self):
        return math.trunc(math.sqrt(self.r**2 * math.pi))


if __name__ == '__main__':
    shape1 = Shape()
    print(shape1)
    shape1.move(1,2)
    print(shape1)

    rect1 = Rectangle(w=3, h=4, x=1, y=1)
    print('rect1 타입:', type(rect1))
    print(rect1)        # override한 __repr__메소드가 호출됨
    rect1.move(-1, -2)  # 부모에게서 상속받은 move 메소드가 호출됨
    print(rect1)

    rect2 = Circle(r=10, x=0, y=0)
    print(type(rect2))
    print(rect2)
    rect2.move(5,6)
    print(rect2)

    rect1.draw()
    rect2.draw()