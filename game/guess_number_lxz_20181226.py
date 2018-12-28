#!/user/bin/python

from random import randint

def game_intro():
	print '''
	The objective of this game is to guess a number (smaller than 999).
	Every round, you will enter your guess.
	The system will tell you if it is the answer.
	If it is not, the system will help you by telling you the remainder of dividing this number by another number.
	Let's start!
	'''

def generate_number():
	"""This generate a 2 digits number
	(Future) Make it to generate digits based on input?"""
	num4 = randint(1,999)
	return(num4)

def one_guess(guess,answer):
	if guess == answer:
#		print "Yes, the answer is %s!! You win!" %answer
		return True
	else:
		print "No, not this one"
		return False

def divide_test(big,small):
	remain = big%small
	print 'The number, if divided by %s, the remainder is %s' %(small,remain)

def main():
	game_intro()
	answer = generate_number()
	gameEnd = False
	guessTimes = 0
	i = 2
	while (not gameEnd):
		guess = int(raw_input("Tell me your guess:"))
		gameEnd = one_guess(guess, answer)
		if gameEnd:
			print "Yes, the answer is %s!! You win!" %answer
			print "You've guessed %s times to find it" %guessTimes
			exit()
		divide_test(answer,i)
		i += 1
#		print "For debug: answer == %s, i == %s, guess == %s" %(answer, i, guess)
		guessTimes +=1



if __name__ == '__main__':
	main()