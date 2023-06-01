# reakoython.com
import itertools, string, timeit
from pathlib import Path

#--- INIT ---
start = timeit.default_timer()
count = 0
output_file = open('iter_1.txt', 'a+')

#--- functions ---
def toString(List):
    return ''.join(List)

def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0


#for p in itertools.permutations('ABCDEFGHIJKLMNOXPRSTUVWZ'):
for p in itertools.permutations('ABCDEFGHIJKL'):
    strop = toString(p)
    if (count % 100000 == 0):
        print(count," ",strop)    
        if (Path(r'iter_1.txt')):
            file=Path(r'iter_1.txt').stat().st_size
        print("Size of file is :", convert_bytes(file), "bytes")
    count += 1
    stringp = strop + "\n"
    output_file.writelines(stringp)

output_file.close()

stop = timeit.default_timer()
print('Time: ', stop - start)

# kaviolina	33.69 sec
# ubuntu  py2 6.002 sec
# ubuntu  py3 20 sec