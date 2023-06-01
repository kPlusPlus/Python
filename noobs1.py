# only noobs do this in P
# https://www.youtube.com/shorts/oLYgLa0oQNw
import io


#f = open("nekiTekst.txt")
#text = f.read().encode('utf8')
#f.close()

#print(text)


# https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python
f = io.open("nekiTekst.txt", mode="r", encoding="utf-8")
text = f.read()
print(text)