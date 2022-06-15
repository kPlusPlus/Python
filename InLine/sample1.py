import time

s1 = "This is a test"
s2 = "This is another test"
combined = " ".join([s1, s2])
print(combined)


for item in range(0,10):
    print(item, end='', flush=True)
    time.sleep(2.4)
    