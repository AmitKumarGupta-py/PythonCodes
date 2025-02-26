def fib(n):
	a, b = 1,1
	a, b = b, a+b
	print(a)
	fib(n-1)
fib(5)