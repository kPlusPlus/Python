from random import seed
from random import random
from random import randint


for n in range(1,10000000,1):
    a = randint(0, 100)
    b = randint(0, 100)
    c = randint(0, 100)    
    print(n," ",a,b,c,(a*b+c) == 85)
    if (a*b+c) == 85:
        print("TO JE TO");
        if (a+b*c) == 86:
            print("TOOOOOOOOOOOOO")
            break