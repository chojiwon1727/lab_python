"""
클래스 작성, 객체 생성, 메소드 사용 연습
"""

class Employee:
    """
    사원정보와 급여 인상 메소드를 가지고 있는 클래스
    field : empno, ename, sal, deptno
    method : raise_sal(self, pct)
    """
    def __init__(self, empno, ename, sal, deptno):
        self.empno = empno
        self.ename = ename
        self.sal = sal
        self.deptno = deptno

    def raise_sal(self, pct):
        """
        인상된 급여를 리턴
        :param pct: 급여 인상율(0.1 = 10%, 0.5 = 50%,...)
        :return: 인상된 급여
        """
        self.sal = self.sal + self.sal*pct
        return self.sal

    def __repr__(self):
        return f'(사번: {self.empno}, 이름: {self.ename}, 급여: {self.sal}, 부서번호: {self.deptno})'




emp1 = Employee(1010, 'scott', 1000, 10)
print(emp1.__repr__())
print(f'sal: {emp1.raise_sal(0.5)}')
print(emp1.__repr__())
print()

emp2 = Employee(1011, 'king', 10000, 20)
print(emp2.__repr__())
print(f'sal: {emp2.raise_sal(-0.1)}')
print(emp2.__repr__())

emp3 = Employee(1012, 'ohssam', 500, 30)

employees = [emp3, emp1, emp2]

print(employees)

print(sorted(employees, key= lambda x: x.empno))
print(sorted(employees, key= lambda x: x.sal))
print(sorted(employees, key= lambda x: x.ename))

