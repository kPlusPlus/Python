# https://www.youtube.com/watch?v=3dwDOqe3Q6Y
#import itertools
import numpy as np
from datetime import datetime

tstart = datetime.now()
counter=0
start = np.float64(3.0)
enddd = np.float64(4)
# step  = 0.000000001
step  = 0.000001
howmany = np.ceil((enddd - start)/step)
print("how many items",howmany)

#for x in range(1,3,0.00001):
for x in np.arange(start, enddd,step):
    rez = np.float_power(x,4) - np.float64(x)
    counter += 1
        
    print(f"{x:.64f}" , rez)
    print(" ")
    if rez > 183:
        print("********************************")
        #print("counter",counter,x,rez)
        print("counter",counter, f"{x:.64f}",rez)
        del counter
        del rez
        del x
        break

tend = datetime.now()
ttime = tend - tstart
print(ttime)

# 0.8613531161119573065221288743487093597650527954101562500000000000 19.999999997982027
# 0:12:56.659181