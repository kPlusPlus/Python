f = open("demofile2.txt", "a")
f.write("Now the file has more content! mimi 123457890")
f.write("Now the file has more content! mimi 1234578901")
f.write("Now the file has more content! mimi 12345789012")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
