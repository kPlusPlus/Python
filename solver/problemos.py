# https://www.youtube.com/watch?v=5wJwlVoQ_sg&list=WL&index=838&t=257s&pp=gAQBiAQB
#import itertools
import numpy as np
#from datetime import date


counter=0
start = np.float64(2.321927999999987)
enddd = np.float64(2.3219280949999948)
step  = 0.000000001
howmany = np.ceil((enddd - start)/step)
print("how many items",howmany)

#for x in range(1,3,0.00001):
for x in np.arange(start, enddd,step):
    rez = np.float_power(8,x) + np.float_power(2,x)
    counter += 1
        
    print(f"{x:.64f}" , rez)
    print(" ")
    if rez > 130:
        print("********************************")
        #print("counter",counter,x,rez)
        print("counter",counter, f"{x:.64f}",rez)
        del counter
        del rez
        del x
        break

# 2.3219280948874