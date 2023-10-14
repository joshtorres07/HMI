from tkinter import *
import random as rnd
class Change(Frame):
    text =  ['Monday', 'Tuesday',' Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack(padx=20, pady=20)
        self.create_components()

    def create_components(self):
        self.et = Label(self,text="Day of weekend")
        self.et.pack()
        self.b =  Button(self, command=self.change_text)
        self.b.config(text="change day")
        self.b.pack()

    def change_text(self):
        text =  rnd.choice(self.text)
        self.et.config(text= text)


if __name__ == '__main__':
    root =  Tk()
    root.title("Another way to change day")
    root.geometry("400x300")
    root.eval('tk::PlaceWindow . center')
    app = Change(root)
    root.mainloop()
