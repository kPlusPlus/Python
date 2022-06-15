#import tkinter as tk
#import PyPDF2
from tkinter import *

#creating the application main window.
top = Tk()
redbutton = Button(top, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)
greenbutton = Button(top, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
bluebutton = Button(top, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
blackbutton = Button(top, text = "Green", fg = "red" )  
blackbutton.pack( side = BOTTOM)  

#Entering the event main loop  
top.mainloop()
