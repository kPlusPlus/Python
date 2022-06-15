#snimi u csv i kasnije prikaži u dijagramu
import csv
import numpy as np

# open the file in the write mode
f = open('sumaa.csv', 'w',newline='')
# create the csv writer
writer = csv.writer(f,delimiter=';')

header = ["No","Result"]
writer.writerow(header)

maxrow = 5000 #10000000
printat = 1000

sumaa=float(0)
for i in range(1,maxrow,1):
    sumaa = sumaa + float(1/float(i))
    if (i % printat == 0):
        print ("count",i,"suma",sumaa)
    row = [i,sumaa]
    writer.writerow(row)
    
f.close()
