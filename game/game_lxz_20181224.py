#!/usr/bin/python

#lxz game 2nd try~
#To record in kanban: /Users/linxz/Dropbox/Python/game_try, input 2 hours
from random import randint
from time import sleep

def key_break():
	raw_input("(Press any key to continue ...)")

def game_intro(current_number):
	"""This function get player name, and give breif introduction
	Input: How many chips (number) in hand, for intro
	Output: Player's name as 'player_name' """
	player_name = get_name()
	print '''
Hi %s~~
Welcome to my game!
You start with %d chips!
This game is about to trying to get you chis in hand to become more, round by round
For every round, you will bet with your opponent chips, who bet with more chips, will take all
But, if your bet is too much higher than the your opponents, you will only get half of his chips on table
Let's start!'''%(player_name, current_number)
	return player_name

def get_name():
	player_name = raw_input("May I have your name?")
#	print "ok, so your name is %s" %player_name
	return player_name


def game_over():
	print "Game Over"
	key_break()
	exit()	

def skip_round(x):
	x += 1
	print "You have skipped %d times" %x
	if x > 5:
		print "You have skipped more than 5 times!"
		game_over()
	return x
#def compare_ab(current_number,bet,enemy):


def proceed_round(current_number,rand_range):
	print "Now you have", current_number
#	sleep (1)
	low_range = int(rand_range/randint(2,8))
	print "the number you are going to fight with, will between %s and %s" %(low_range,rand_range)
	decision = raw_input("Do you want to try to win it (yes/no)?")
	if (decision == 'no'):
		print "OK! Let's skip this round!"
		#print "##For debug only: Skip_count still having problem at the moment"
		pass
	elif (decision == 'yes'):
		print "Good luck! Let it begin"
#		sleep (1)
		bet = int(raw_input("How many do you want to bet in this fight? (current value is %s)" %current_number))
		print "So your bet is %s" %bet
		print "##For debug, current_number is", current_number
		if bet > current_number:
			print "You don't have that much, it's cheat!"
			game_over()
		else:			
			print "Ready?"
			sleep (1)
			print "The opponent number is ..."
			sleep (1)
			enemy = randint(low_range,rand_range)
			print "%s !!!"% enemy
#			compare_ab (current_number,bet,enemy)
			if bet > enemy*2:
				current_number += int(enemy/2)
				result = 'Win with too High bet'
			elif bet > enemy:
				current_number += enemy
				result = 'Win!'
			elif bet < enemy:
				current_number -= bet
				result = 'Lose!'
			else:
				result = 'Draw!'
			print '''So for this round, you end up with the result, 
			<<<%s>>>''' %result
			print "Now you have: %s" %current_number
			return current_number

	else:
		print "This is a wrong input, will be considered as skip"
		pass
		
	new_number = current_number
	return new_number



def main():
	skip_count = 0
	init_number = 20
	game_current = init_number
	game_intro(init_number)
	key_break()
	for i in range(15):
		print '''
	========================Start round %d===================='''%(i+1)
		#print "Now is round %d" 
		before = game_current
		game_current = proceed_round(game_current,game_current+randint(1,10))
		if before == game_current:
			skip_count = skip_round(skip_count)
		print "##For debug: before = %s, game_current = %s, skip_count = %s" %(before, game_current,skip_count)
		#print "##For debug: Out of the function, the game_current value is %d" %game_current
		print "========================End round %d===================="%(i+1)
		key_break()
		if game_current < 2:
			print "========================Ending===================="
			sleep(1)
			print '''There is no more chance to win, 
	You have played %d rounds, start with %d and end with %d
	thanks for playing!''' %((i+1),init_number,game_current)
			game_over()

if __name__ == '__main__':
	main()
#print "##For debug: In the end, after %s round, you have %s" %i,game_current