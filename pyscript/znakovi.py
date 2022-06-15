def HTML(text):
     return text.replace("{{", "<").replace("}}", ">")

print( HTML("{{b}}Hello Mihael{{/b}}") )
print( HTML("{{h1}}Hello Mihael{{/h1}}") )