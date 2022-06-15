# importing  all the
# functions defined in test.py
from test import *
from geteuro import *
 
 
# calling functions
#displayText()
start = timeit.default_timer()
watch_start()

surl = "https://www.coingecko.com/en/coins/avalanche"
page = file_get_contents(surl)

print( page )
watch_stop()

watch_display()

stop = timeit.default_timer()
print('ORIG Time: ', stop - start)
