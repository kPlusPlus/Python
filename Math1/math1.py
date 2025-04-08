import math 
import numpy as np

for nus in np.arange(6.445,7,0.0001):
    result = math.sqrt(nus) - (nus * nus)
    print(nus,result)