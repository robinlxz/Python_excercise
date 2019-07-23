# 6.00 Problem Set 2
#
# Successive Approximation
#
#url: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-6-recursion/MIT6_00SCS11_ps2.pdf

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
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
        print 'Error: the input x (%s) cannot be convert to float' % x
    for i in range(len(poly)):
        fx += poly[i]*(x**i)
    return fx

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

def compute_root(poly, x_0, epsilon,i):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ... 
    '''
    lxz question:
    1. cannot init i = 1 every time enter function. Then how to record interative?
    A: Either using while, or add one more parameter in recursive function
    2. What is the mistake when using 'while 1', or 'while a > b'
    A: Using while, then no recursive is needed
    3. Why output is 'None'
    A: Because the return is not open for recursive case (https://www.cnblogs.com/yechenkai/p/7143475.html)
    '''
    if abs(evaluate_poly(poly, x_0)) < epsilon:
        #return (x_0, i)
        #print 'now difference is', evaluate_poly(poly, x_0)
        #print 'x_0 = ', x_0
        print 'interation count i = ', i
        #return x_0
        return (x_0,i)
    else:
        print 'now difference is', evaluate_poly(poly, x_0)
        #raw_input('any key...')
        x_1 = x_0 - evaluate_poly(poly, x_0)/evaluate_poly(compute_deriv(poly), x_0)
        i += 1
        #print 'x_1 =', x_1
        #i += 1
        #print 'i =', i
        #r = compute_root(poly, x_1, epsilon, i)
        r_t = compute_root(poly, x_1, epsilon, i)
        return r_t
        #if i > 200:
        #    exit() 

def compute_root2(poly, x_0, epsilon):
    while abs(x_0) > epsilon:
        x_0 = evaluate_poly(poly, x_0)/evaluate_poly(compute_deriv(poly), x_0)
        #x_0 = compute_root2(poly, x_0, epsilon)
    return x_0

def main():
    poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
    #poly = (0, 0, 1)
    x_0 = 0.1
    epsilon = 0.0001
    result = compute_root(poly, x_0, epsilon, 1)
    assert len(result) == 2

    r2 = compute_root2(poly, x_0, epsilon)
    print r2
    #print 'The filnal output is:', result
    print 'The root we found is %s, the amount of iterations is %s.' %(result[0], result[1])


if __name__ == '__main__':
    main()