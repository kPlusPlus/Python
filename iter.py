import itertools, string

maxChar = int(input('Character limit for password: '))
output_file = open('text.txt', 'a+')

x = list(map(''.join, itertools.permutations(string.printable, maxChar)))
#x.write(str(x))
#x.close()

# writes the output of the above line to a file 
output_file.write(str(x)) 

# saves the output to the file and closes it to preserve ram
output_file.close() 
