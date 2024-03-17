# https://www.geeksforgeeks.org/calculate-pi-with-python/?ref=gcse
from datetime import datetime
import csv

tstart = datetime.now()

# Initialize denominator
k = 1

# Initialize sum
s = 0

maxRange = 100000000
printAt = 1000000

#f = open("CalcPi.csv", "a")
f = open('CalcPi.csv', 'w',newline='')
writer = csv.writer(f,delimiter=',')
header = ["No","Result"]
writer.writerow(header)


for i in range(maxRange):

    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:

        # odd index elements are negative
        s -= 4/k

    # denominator is odd
    k += 2
    if (i % printAt == 0):
        print(i,s)
        f.write(str(i)+","+str(s) +"\n")
        row = [i,s]
        writer.writerow(row)


print(s)
f.flush() # TEST TEST TEST
f.close()

tend = datetime.now()
ttime = tend - tstart
print(ttime)

# kaviolina         0:00:26.072287
# bubica            0:01:57.488756
# CoLab             0:00:40.8