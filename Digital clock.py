# pip install pyglet
from tkinter import * #from tkinter import everything
# we need a module(pyglet) that handle the clock font file
import pyglet 
from datetime import datetime

pyglet.font.add_file('digital-7.ttf')
bc = "#f5e942"
fc = "#3d0720"

window = Tk()
window.title("Digital Clock")
window.geometry('530x150')
window.resizable(width=False, height=False )
window.configure(bg=bc) # for background color of the window

# Creating a function which make clock alive
def clock():
    time = datetime.now()# gives the current date and time
    hour= time.strftime(" %H : %M : %S") # strf is converting time to string
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%B")
    year = time.strftime("%Y")
    l1.configure(text=hour)
    l1.after(200,clock)
    l2.configure(text=weekday+ "  " + str(day) + "/" + str(month) + "/" + str(year))


l1 = Label(window, text = '12:00:50', font = ('digital-7 80'), bg = bc, fg= fc) #label 1 for time
l1.grid(row = 0, column = 0, padx = 5, sticky=NW)#NW is North West
# sticky makes data in window stick to north west can be seen when width, height = True om window resizable

l2 = Label(window, text = 'Wednesday 01/06/2022', font = ('digital-7 20'), bg = bc, fg=fc) #label 1 for time
l2.grid(row = 1, column = 0,padx= 30, sticky=NW)


clock()

window.mainloop()


