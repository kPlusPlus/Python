#snimi u csv i kasnije prikaži u dijagramu
import csv
import numpy as np
import timeit

start = timeit.default_timer()
# open the file in the write mode
f = open('sumaa.csv', 'w',newline='')
# create the csv writer
writer = csv.writer(f,delimiter=';')

header = ["No","Result"]
writer.writerow(header)

maxrow = 10000000
printat = 1000

sumaa=np.float64(0)
for i in range(1,maxrow,1):
    sumaa = sumaa + np.float64(1/i)
    if (i % printat == 0):
        print ("count",i,"suma",sumaa)
    row = [i,np.float64(sumaa)]
    writer.writerow(row)
    
f.close()

stop = timeit.default_timer()
print('Time: ', stop - start)

# 169.67 kaVIoLIna
# 161.52 rpi4