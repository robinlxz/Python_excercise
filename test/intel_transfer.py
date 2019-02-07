'''
This is about a function to extract some bits from hex input
As Shengjian mentioned, it is used for process info on CAN BUS
'''

from math import floor

def hex_to_bin(hex_str):
	'''
	This function read in a 2 bit length hex, return it's binary in str
	'''
	try:
		if len(hex_str) == 1:
			hex_str = '0' + hex_str
		else:
			len(hex_str) == 2
	except:
		print 'Wrong input for hex_to_bin'
	m1 = hex_str
	#print 'm1 is', m1
	b1 = bin(int(m1,16))[2:]
	#print 'b1 is', b1
	return b1

def extract(message, bitStart, length, byteOrder, singnedOrUnsigned):
	try:
		str(message)
		int(bitStart)
		int(length)
		int(byteOrder)
		int(singnedOrUnsigned)
	except:
		print 'function input type error'

	'''
	>>> bin(0xff)
	'0b11111111'
	'''
	'''
	hex_str = "0xAD4"
	hex_int = int(hex_str, 16)
	new_int = hex_int + 0x200
	print hex(new_int)
	'''
	#Test with message with 2 bit long first
	message = 'a7'
	m1 = message[0:2]
	b1 = hex_to_bin(m1)
	print 'b1 is', b1


#extract('ff',1,1,1,1)

'''
Fake code
'''
#fix Motorol and byteOrder=0


'''
test code
assume b1 is not binary anymore
'''
b = []
for i in range(0,8):
	l = range(i*8,i*8+8)
	l.reverse()
	b.append(l)

#print b
bitStart = 1

start1 = int(floor(bitStart / 8))
start2 = bitStart%8
print 'start from', b[start1][start2]

b_all = []
for lis in b:
	b_all += lis
#print b_all

length = 12
realStart = b_all.index(bitStart)
result = b_all[realStart:(realStart+length)]
print result