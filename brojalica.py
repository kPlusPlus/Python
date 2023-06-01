# brojalica
from datetime import datetime
import sys
import csv
import os
sys.set_int_max_str_digits(1000000)


filename = 'brojalica.csv'
if os.path.exists(filename):
    os.remove(filename)

f = open(filename,'w')

vrh=1000000
tstart = datetime.now()

x = range(1, vrh + 1, 1)
for n in x:
    result = (vrh/n)
    izr = str(n) , str(result)
    if n % 100000 == 0:
        print(izr)
    f.write(str(n)+";"+str(result)+"\n")

tend = datetime.now()
ttime = tend - tstart
print(ttime)

f.close()

#   kaviolina   0:00:13.870911