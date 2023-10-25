from tkinter import *
import time

def updateHour():
    hour =  time.strftime("%H:%M:%S")
    vctrl.set(hour)
    root.after(1000, updateHour)

root =  Tk()

vctrl = StringVar()
watch = Label(root, textvariable=vctrl, fg='red', font=("Arial", 18, "bold italic"), padx=20, pady=20, bitmap="hourglass", compound='left')
watch.pack()
updateHour()
root.mainloop()

"""
archivos xbm
error, gray75, 50, 25, 12
hour glass
info
questhead
question
warning
"""

"""root.configure(cursor="arrow"
trek
watch
target
tcross
star
shuttle
sizing
spider
spraycam
heart
man
mouse
pirate
plus
arrow
circle
clock
cross
dotbox
exchange
fleur

"""