class Score:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def calc_total(self):
        return self.korean + self.english + self.math


    def calc_avg(self):
        return self.calc_total()/3

score1 = Score(99,88,77)
score1.math = 79
print(score1.calc_total())
print(score1.calc_avg())

score2 = Score(90,85,70)
print(score2.calc_total())
print(score2.calc_avg())
