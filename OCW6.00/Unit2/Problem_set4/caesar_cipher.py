#!/usr/bin/python
import string

def main():
#All = ' '
	All = ' ' + string.ascii_letters[:]
	Dict = {}
	lth = len(All)
	for i in range(lth):
		Dict[All[i]]=All[(i+3)%lth]
	print Dict




if __name__ == '__main__':
	main()


