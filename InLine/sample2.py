from sys import stdout
from time import sleep
for i in range(1,20):
    #stdout.write("\r%d" % i)
    stdout.write("\rabs "+ str(i))
    stdout.flush()
    sleep(1)
stdout.write("\n") # move the cursor to the next line
