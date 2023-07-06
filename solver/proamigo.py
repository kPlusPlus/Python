# https://www.youtube.com/watch?v=3dwDOqe3Q6Y
#import itertools
import numpy as np
from datetime import datetime

tstart = datetime.now()
counter=0
start = np.float64(3.69)
enddd = np.float64(4)
# step  = 0.000000001
step  = 0.00000001
howmany = np.ceil((enddd - start)/step)
print("how many items",howmany)

#for x in range(1,3,0.00001):
for x in np.arange(start, enddd,step):
    rez = np.float_power(x,4) - np.float64(x)
    counter += 1
        
    print(f"{x:.64f}" , rez)
    print(" ")
    if rez > 182:
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

# 3.6914584199911364414958825364010408520698547363281250000000000000 181.99999857199228
# step  = 0.000001
# 0:00:43.132770
