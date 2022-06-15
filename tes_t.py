import time

ibroj = 1

for i in range(1,200):
	print(i,ibroj);
	ibroj = ibroj * 2;
	if i%10 == 0:
		time.sleep(1);