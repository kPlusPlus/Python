import random
import timeit

start = timeit.default_timer()
my_list = []
countelement = 10000


def generate_lottery_numbers(num_numbers=6, range_start=1, range_end=49):
    return random.sample(range(range_start, range_end + 1), num_numbers)


for i in range(countelement):
    lottery_numbers = generate_lottery_numbers()
    my_list.append(lottery_numbers)
    ###print(i , " Your lottery numbers are:", lottery_numbers)


stop = timeit.default_timer()
print(my_list)
print('Time: ', stop - start)

# Time:  1.0370708000045852 kaVioLina   100000
# Time:  0.7106481000009808 kaVioLina iz prompta

# Time:  0.07693620002828538 kyViolina  100000  --- without print
# Time:  0.04006659996230155 kaVioLina iz prompta