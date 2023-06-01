# Using readlines()
file1 = open('rockyou.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.decode()))
    #print("Line{}: {}".format(count, line.strip()))