##To use the clock simply run the file and the current time will be displayed in the window.
#The time will be displayed showing hours, minutes, and seconds on a 12 hour scale. In the future
#I could add an alarm or stopwatch to original clock.

##REFERENCES
#Geeksforgeeks.org (https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/)
#Medium.com (https://medium.com/dev-genius/how-to-make-a-clock-with-python-7587e107bb5e)
#Youtube, John Phillip Jones (https://www.youtube.com/watch?reload=9&v=0I97O2p-4Tc)


# Imported all of tkinter, and strftime from time. 
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


