# okretalica
from sys import stdout
from time import sleep

simbols = "-\|/"
no = 0
count = len(simbols)

for i in range(1,20):
    #stdout.write("\r%d" % i)
    stdout.write("\r "+ simbols[no] + "\t" + str(i))
    stdout.flush()
    sleep(0.4)
    no = no + 1
    if (no > (count-1)):
        no = 0
                 
stdout.write("\n") # move the cursor to the next line

