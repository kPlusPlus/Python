import random
import timeit

start = timeit.default_timer()

def generate_lottery_numbers(num_numbers=6, range_start=1, range_end=49):
    return random.sample(range(range_start, range_end + 1), num_numbers)


for i in range(10000):
    lottery_numbers = generate_lottery_numbers()
    print(i , " Your lottery numbers are:", lottery_numbers)

stop = timeit.default_timer()
print('Time: ', stop - start)

# Time:  1.0370708000045852 kaVioLina   100000
# Time:  0.7106481000009808 kaVioLina iz prompta