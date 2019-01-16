#!/usr/bin/python

# This is OCW 6.00 test draft
# And my first time answer for Unit 1 Quiz


def findAll(wordList, lStr):
	"""assumes: wordList is a list of words in lowercase.
	lStr is a str of lowercase letters.
	No letter occurs in lStr more than once
	returns: a list of all the words in wordList that contain
	each of the letters in lStr exactly once and no
	letters not in lStr. [added again for test]"""
	result = []
	for word in wordList:
		if len(word) == len(lStr):
#			print 'in camparing', word, 'and', lStr
			Lstr=[]
			Lword=[]
			for letter in lStr:
#				print 'now letter is', letter
				Lstr.append(letter)
#			print 'now Lstr is', Lstr
			Lstr.sort() 
#			print 'and Lstr.sort() is', Lstr
			for letter in word:
				Lword.append(letter)
			Lword.sort()
			if Lstr == Lword:
				print 'We think this two are equal', Lstr, Lword
				result.append(word)
				print 'After append, result is', result
	return result

#a = findAll(['abc','defg','def'],'cba')
#print 'the output of function is', a


def addVectors(v1, v2):
	"""assumes v1 and v2 are lists of ints.
	Returns a list containing the pointwise sum of
	the elements in v1 and v2. For example,
	addVectors([4,5], [1,2,3]) returns [5,7,3],and
	addVectors([], []) returns []. Does not modify inputs."""
	if len(v1) > len(v2):
		result = v1[:]
		other = v2[:]
	else:
		result = v2[:]
		other = v1[:]
	for i in range(len(other)):
		result[i] += other[i]
	print 'v1 = ', v1, 'v2 = ', v2
	return result 
#print addVectors([1,2,3],[1,2])

'''
1. True
Wrong. 
2. False
Wrong.
3. False
4. False
5. True
Wrong
2)
Wrong


3)
Anser: 'atm' and 'tmah'
atm correct
f('math') Wrong (got it)

6)
1
2 (Wrong, got it.)
{}
error

7)
None
'n = 1'
'n = 1' (Wrong, got it)
'''