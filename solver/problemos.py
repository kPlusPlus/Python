# https://www.youtube.com/watch?v=5wJwlVoQ_sg&list=WL&index=838&t=257s&pp=gAQBiAQB
import itertools
import numpy 
counter=0

#for x in range(1,3,0.00001):
for x in numpy.arange(2.321927999999987, 2.3219280949999948, 0.000000001):
    rez = pow(8,x) + pow(2,x)
    counter += 1
    with np.printoptions(precision=30, suppress=True):
        print(x , rez)
    print(" ")
    if rez > 130:
        print("********************************")
        print("counter",counter,x,rez)
        del counter
        del rez
        del x
        break