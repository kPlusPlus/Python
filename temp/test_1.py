# https://towardsdatascience.com/10-ways-to-speed-up-your-python-code-e3d57630b710
from datetime import datetime
tstart = datetime.now()

numbers = []

for x in range(100000):
    if x % 2 == 0:
        numbers.append(x**2)
        
        
tend = datetime.now()
ttime = tend - tstart
print(ttime)