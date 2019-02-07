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
	assert type(poly) == tuple
	try:
		x = float(x)
	except:
		print 'Error: the input x (%s) cannot be convert to float' %x
	for i in range(len(poly)):
		fx += poly[i]*(x**i)
	return fx



#For other test
'''
Return sends a specified value back to its caller 
whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, 
but don't want to store the entire sequence in memory.
'''
def test_yeild(List):
	for i in List:
		yield i+1
		#return i+1

#for p in test_yeild([1,2,3]):
#	print p

#print evaluate_poly((1,1,1,1),1)

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ... 
    result = []
    for i in range(1,len(poly)): #To start from 1 is because the 0th element is gone
    	result.append(poly[i]*i)
    	#result_t += (poly[i]*i,)
    result_t = tuple(result)
    return result_t

#print compute_deriv((-13.39, 0.0, 17.5, 3.0, 1.0))

