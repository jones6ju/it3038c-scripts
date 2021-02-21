## The sources used for help with this project were
## Geeksforgeeks.com(), John Phillip Jones(youtube:"A digital clock built with Python tkinter"), 
# ## and Medium.com(How to make a clock in python)


# Imported all of tkinter and strftime from time. 
from tkinter import * 
from tkinter.ttk import *
from time import strftime
  
#Adding a window to start with
window = Tk() 
window.title('Current Time') 
  
#Creating the actual clock and then formatting the text.
def time(): 
    string = strftime('%I:%M:%S %p') 
    time_text.config(text = string) 
    time_text.after(1000, time) 
time_text = Label(window, font = ('times new roman', 64, 'bold'), 
            background = 'black', 
            foreground = 'green') 

#fitting the clock into the window
time_text.grid(row=0, column=0)
time() 
mainloop() 


