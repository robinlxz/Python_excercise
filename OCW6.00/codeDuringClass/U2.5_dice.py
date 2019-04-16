#!/Users/linxz/miniconda2/bin/python
# This is OCW 6.00 U2.5 test draft
import random

def rollDie():
	return random.randint(1,6)


def testRoll(n = 10):
	result = ''
	for i in range(n):
		result = result + str(rollDie())

def checkPascal(numTrials = 100000):
	yes = 0.0
	for i in range(numTrials):
		for j in range(24):
			if rollDie() == 6 and rollDie() == 6:
				yes += 1.0
				break
	print 'Probability of having double 6 in 24 rolls = ' + str(yes/numTrials)

checkPascal()