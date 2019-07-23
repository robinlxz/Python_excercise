#!/Users/linxz/miniconda2/bin/python
# This is OCW 6.00 test draft

import random
import pylab

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRoll(n = 10):
    result = ''
    res_lis = []
    for i in range(n):
        result = result + str(rollDie())
        res_lis.append(rollDie())
    print result
    return res_lis

#testRoll()

#pylab.figure()
# a = testRoll()
# b = testRoll()
# pylab.plot(range(len(a)),a)
# pylab.plot(range(len(b)),b)
# pylab.plot([1,2,3,4,5,6,8,10,12,14])
# pylab.show()

def plotSavingIncrease(principle, year, interestRate):
    values = []
    for i in range(year+1):
        values.append(principle*((1+interestRate)**i))
    return values


pylab.plot(plotSavingIncrease(20000, 30, 0.02))
pylab.title('Value growth with compound interesets')
pylab.xlabel('years')
pylab.ylabel('value')
pylab.show()