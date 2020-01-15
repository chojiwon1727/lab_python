import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('반지름은 0 또는 양수')

    def area(self):
        return self.radius**2

    def perimeter(self):
        return 2*self.radius*math.pi

    def __str__(self):
        return f'Circle(r={self.radius})'

    def __repr__(self):
        return f'circle({self.radius})'

    def __eq__(self, other):
        print('__eq__호출')
        return self.radius == other.radius

    def __ne__(self, other):
        print('__ne__호출')
        return self.radius != other.radius

    def __gt__(self, other):
        # greater than : > 연산자를 사용하면 자동 호출
        print('__gt__ 호출')
        return self.radius > other.radius

    def __ge__(self, other):
        # greater than or equal to : >= 연산자를 사용하면 자동동으로 출되는 메소드
        # return self.__gt__(other) or self.__eq__(other)
        return self.radius >= other.radius


if __name__ == '__main__':
    circle1 = Circle(15)
    circle2 = Circle(13)

    # print(circle1)
    # print(circle1.area())
    # print(circle1.perimeter())
    # print(id(circle1))
    # print()
    # print(circle2)
    # print(circle2.area())
    # print(circle2.perimeter())
    # print(id(circle2))
    # print()
    # print(circle1 == circle2)
    # print(circle1 != circle2)
    #
    # print(circle1 > circle2)
    # print(circle1 >= circle2)
    # print(circle1 < circle2)
    # print(circle1 <= circle2)


    circles = [
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(50),
        Circle(0)
    ]

    print(circles)
    print(sorted(circles))
    print(sorted(circles, reverse=True))
