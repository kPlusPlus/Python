# test.py>
import timeit
wstart = timeit.default_timer()
wstop = timeit.default_timer()

# function
def displayText():
    print( "Geeks 4 Geeks !")

# watch functions
def watch_start():
    print("watch start")
    wstart = timeit.default_timer()

def watch_stop():
    print("watch stop")
    wstop = timeit.default_timer()

def watch_display():
    print("Watch display")
    print('Time: ', wstop - wstart)
    #print('Time: ', wstart)