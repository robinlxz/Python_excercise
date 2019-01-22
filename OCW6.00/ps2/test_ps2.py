def evaluate_poly(poly, x): 
	"""
	Computes the polynomial function for a given value x. Returns that value.
	Example:
	>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) # f(x) = 7.0x4
	 + 9.3x3
	 + 5.0x2
	>>> x = -13
	>>> print evaluate_poly(poly, x) # f(-13) = 7.0(-13)4
	 + 9.3(-13)3
	 + 5.0(-13)2
	180339.9
	poly: tuple of numbers, length > 0
	x: number
	returns: float
	"""
	# TO DO ... 
	fx = 0
	for i in range(len(poly)):
		fx += poly[i]*(x**i)
	return fx

print evaluate_poly((1,1,1,1),5)

#For other test
'''
Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
'''
def test_yeild(List):
	for i in List:
		yield i+1

#for p in test_yeild([1,2,3]):
#	print p
