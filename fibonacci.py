#Program to generate nth Fibonacci number

def simple_addition(n):
	a = 0
	b = 1
	if(n==1 or n==2):
		return n-1
	n=n-2
	while(n>0):
		c= a+b
		a=b
		b=c
		n=n-1
	return c 

def fib_recursion(n):
	if(n==1 or n==2):
		return n-1
	else: return fib_recursion(n-1)+ fib_recursion(n-2)

memo = {0:0, 1:1}

def fib_dynamic(n):
	if not n in memo:
		memo[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
	return memo[n]


"""
References:
1. Multiple methods to generate Fibonacci numbers includind the ones above http://en.literateprograms.org/Fibonacci_numbers_(Python)
"""
