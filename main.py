from situation import *
from student import *
from apisode import *
from situList import *


stu = Student("min",10,10)

situ = Situation(scdSitu,scdSituEx)

situ.printSitu()
situ.choSitu()

stu.exp = situ.returnExp(stu.exp)
stu.sts = situ.returnSts(stu.sts)

print("exp : ",stu.exp)
print("sts : ",stu.sts)