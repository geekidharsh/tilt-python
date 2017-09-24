def fib(n):
	results = []
	a,b = 0, 1
	for num in range(a,n):
		b,a = a+b, b
		results.append(b)
	return results