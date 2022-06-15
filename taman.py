from datetime import datetime

tstart = datetime.now()
print(tstart)

a = 201
b = 200

if b > a:
	print("b is greater than a")
if a > b:
	print("a is greater than b")
if a == b:
	print("a is equal to b")
	
tend = datetime.now()
print(tend)

ttime = tend - tstart
print(ttime)
