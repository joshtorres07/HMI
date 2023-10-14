from tkinter import *
import random as rnd

def change_day(et, text):
    text = rnd.choice(text)
    et.config(text = text)

if __name__ == '__main__':
    text =  ['Monday', 'Tuesday',' Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
    root = Tk()
    root.geometry("300x300")
    root.title("Change day")
    root.eval('tk::PlaceWindow . center')
    app =  Frame(root)
    app.pack(padx=20, pady=20)
    et = Label(app,text="Day of weekend")
    bt =  Button(app,text = "change", command=lambda: change_day(et,text))
    et.pack()
    bt.pack()
    root.mainloop()