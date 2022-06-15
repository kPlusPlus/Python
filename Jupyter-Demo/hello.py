import timeit
import time

start = timeit.default_timer()

print("Hello World!")
ime = "mali ivica"
print("Hello " + ime)
ime = "mali perica"
print("Hello " + ime)

stop = timeit.default_timer()
print('Time: ', stop - start)