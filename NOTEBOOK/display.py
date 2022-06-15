from IPython.display import display, HTML
display(HTML('<h1>Hello World</h1>'))

#from IPython.display import display
display({'text/html': '<h1>Hello World</h1>', 'text/plain': 'Hello World'}, raw=True)