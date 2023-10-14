from tkinter import *
import random as rnd
from ChangeOne import *

class ChangeTwo(Change):
    txt = {'azul': 'blue', 'rojo':'red', 'amarillo':'yellow', 'cyan': 'cyan'}

    def change_text(self):
        color = rnd.choice(list(self.txt.keys()))
        self.et.config(text= color.title(), fg= self.txt[color])

if __name__ == '__main__':
    root =  Tk()
    root.title("Change color")
    root.geometry("400x300")
    root.eval('tk::PlaceWindow . center')
    app = Change(master =  root)
    app2 =  ChangeTwo(master=root)
    root.mainloop()