import student
from student import *

from random import choice

hiPoint = [20,15,10]
loPoint = [20,5,0]

class Situation:

    question = ""
    exList = {}
    expPnt = 0
    stsPnt = 0
    ans = 0

    def __init__(self,question,exList):
        self.question =question
        self.exList = dict(exList)



    def printSitu(self):

        print(f"{self.question}\n")
        for i in range(4):
            print(f"{i + 1}. {self.exList[i + 1]}")
        print()

    def choSitu(self):
        self.ans = int(input("선택한 번호를 입력하세요: "))
        situT = lambda a: 1 if a == 1 or a == 2 else 0
        self.siType = situT(self.ans)


    def returnExp(self,exp ):
        if self.ans == 1:
            expPnt = choice(hiPoint)
            print("high point :",expPnt)
            exp= exp + expPnt
            return exp

        elif self.ans == 2:
            expPnt = choice(loPoint)
            print("low point :", expPnt)
            exp = exp + expPnt
            return exp

        elif self.ans == 3:
            expPnt = choice(loPoint)
            print("low point :", expPnt)
            exp = exp + expPnt
            return exp

        else:
            expPnt = choice(hiPoint)
            print("hipoint :", expPnt)
            exp = exp + expPnt
            return exp

    def returnSts(self,sts):
        if self.ans == 1:
            stsPnt = choice(hiPoint)
            sts = sts + stsPnt
            return sts
        elif self.ans == 2:
            stsPnt = choice(loPoint)
            sts = sts + stsPnt
            return sts
        elif self.ans == 3:
            stsPnt = choice(loPoint)
            sts = sts + stsPnt
            return sts
        else:
            stsPnt = choice(hiPoint)
            sts = sts + stsPnt
            return sts










