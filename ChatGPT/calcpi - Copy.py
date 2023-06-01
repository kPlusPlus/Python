# napravio ChatGPT
import random
#import datetime
from datetime import datetime
#from datetime import datetime


def calculate_pi(num_samples):
    inside_circle = 0
    for i in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi = 4 * inside_circle / num_samples
    return pi

#num_samples = int(input("Unesite broj uzoraka: "))
num_samples = 1000000000


tstart = datetime.now()
pi = calculate_pi(num_samples)
print("Izračunati broj Pi je:", pi)
tend = datetime.now()
ttime = tend - tstart
print(ttime)



#10000000     kaviolina         0:00:07.755334
#100000000    kaviolina         0:01:30.123397
#1000000000   kaviolina         0:20:21.498795
