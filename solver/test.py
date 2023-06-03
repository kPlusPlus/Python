import itertools
import numpy as np

counter = 0

broj = 2
rez = np.power(130,(1/broj))
print(rez)

for x in np.arange(broj, broj + 0.2, 0.00001):
    rez = np.power(130,(1/x))
    counter += 1  
    
    print("counter",counter, f"{x:.64f}",rez)
    print(" ")
    if rez < 10:
        print("********************************")
        np.set_printoptions(precision=30)        
        print("counter",counter, f"{x:.64f}",rez)
        print(type(x))
        del counter
        del rez
        del x
        break