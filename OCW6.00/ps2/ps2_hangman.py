# 6.00 Problem Set 3
# 
# Hangman
#
#url: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_ps2.pdf

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"
ROUND_LIMIT = 15

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def game_intro(ROUND_LIMIT):
    print '''The game "hangman" start, you will be given: 
    1. a word with only lower case letter
    2. the length of the word
    3. the amount of 'Guesses' you have is %s, and only lost one Guess when it's wrong.
    ''' %ROUND_LIMIT

def show_length(word):
    assert len(word)>0
    print ('Welcome to the game, Hangman!\n'
           'I am thinking of a word that is %s letters long.') % len(word)

def get_guess_input():
    guess = raw_input('Please guess a letter:')
    assert guess in string.ascii_lowercase
    return guess

# def get_output(word, guess):
#     output = ''
#     for l in word:
#         if l == guess:
#             output += l
#         else:
#             output += '_'
#     return output

def get_next_output(word, guess, status):
    output = ''
    assert len(word) == len(status)
    for i in range(len(word)):
        if guess == word[i]:
            output += guess
        elif status[i] != '_':
            output += status[i]
        else:
            output += '_'
    return output

def game_over():
    print 'Game Over.'
    exit()

def game_start():
    word = choose_word(wordlist)
    print word
    game_intro(ROUND_LIMIT)
    show_length(word)
    status = '_'*len(word)
    i = ROUND_LIMIT
    while status != word:
        if i == 0:
            print 'you\'ve reached %s rounds, current status is %s.' %(ROUND_LIMIT, status)
            game_over()
        print '------------'
        print 'You have %s guesses left' %i
        guess = get_guess_input()
        status = get_next_output(word, guess, status)
        print status
        if guess in word:
            i += 1
        i -= 1

    print "You get it! The word is %s, you get it in %s round.\nCongratulations, you won!" %(word, i)

def main():
    game_start()

if __name__ == '__main__':
    main()