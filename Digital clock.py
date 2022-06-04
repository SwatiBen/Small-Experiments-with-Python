from tkinter import * 
import pyglet 
from datetime import datetime

pyglet.font.add_file('digital-7.ttf')
bc = "#f5e942"
fc = "#3d0720"

window = Tk()
window.title("Digital Clock")
window.geometry('530x150')
window.resizable(width=False, height=False )
window.configure(bg=bc)

def clock():
    time = datetime.now()
    hour= time.strftime(" %H : %M : %S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%B")
    year = time.strftime("%Y")
    l1.configure(text=hour)
    l1.after(200,clock)
    l2.configure(text=weekday+ "  " + str(day) + "/" + str(month) + "/" + str(year))

l1 = Label(window, text = '12:00:50', font = ('digital-7 80'), bg = bc, fg= fc) 
l1.grid(row = 0, column = 0, padx = 5, sticky=NW)

l2 = Label(window, text = 'Wednesday 01/06/2022', font = ('digital-7 20'), bg = bc, fg=fc) #label 1 for time
l2.grid(row = 1, column = 0,padx= 30, sticky=NW)

clock()

window.mainloop()
