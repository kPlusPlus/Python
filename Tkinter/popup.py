# https://www.youtube.com/watch?v=Au6FPjkgbUE
#from tkinter import *

from tkinter import Button, Label, Tk, Toplevel


window = Tk()
window.title("Main window")
window.geometry("300x300")

def popup():
    popupwindow = Toplevel(window)
    popupwindow.title("Alert")
    popupwindow.geometry("200x100")
    alert = Label(popupwindow,text="Is it right?")
    button1 = Button(popupwindow, text="Ok", command=popupwindow.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()


button = Button(window,
                text="Open",
                command=popup)
button.pack()

window.mainloop()