a = 0
b = 1
fibo=[a,b]
while b < 100000:
	a, b = b, a+b
	fibo.append(b)
	print(fibo)