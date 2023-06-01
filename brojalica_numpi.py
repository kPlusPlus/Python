# brojalica
from datetime import datetime
import sys
import csv
import os
import fastmath as fm
#import numpy as np
import numba

sys.set_int_max_str_digits(10000000)
@numba.jit()
def kpdiv(a,b):
    return a / b


filename = 'brojalica.csv'
if os.path.exists(filename):
    os.remove(filename)


f = open(filename,'w')

#vrh=10000000
vrh=10000
ispisna = vrh / 10
tstart = datetime.now()

x = range(1, vrh + 1, 1)
for n in x:
    #result = (vrh/n)
    result = kpdiv(vrh,n)
    izr = str(n) , str(result)    
    if n % ispisna == 0:
        print(izr)
    f.write(str(n)+";"+str(result)+"\n")

tend = datetime.now()
ttime = tend - tstart
print(ttime)

f.close()

#   kaviolina   	0:00:13.870911
#	kaviolina Thonny	0:00:03.092891		0:00:05.676272			Python 3.10.9