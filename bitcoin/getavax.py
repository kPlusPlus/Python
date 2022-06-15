from dateutil import parser
import timeit
import time
import csv
from geteuro import *
start = timeit.default_timer()

ulog = 2.572425
config='getavax.csv'

file = open(config,'r+')
file.seek(0)

#print(file)
csvreader = csv.reader(file, delimiter=';')
rows = []
for row in csvreader:
    rows.append(row)    

print('Rows' , len(rows))
last_line = len(rows) - 1


timeold = rows[last_line][0]
currold = rows[last_line][1]
ihave = 0
dt_timeold = parser.parse(timeold)

print(timeold , " " , currold)
surl = "https://www.coingecko.com/en/coins/avalanche"
page = file_get_contents(surl)
print( page )
# *** TU SAM STAO

file.close()
stop = timeit.default_timer()
print('Time: ', stop - start)