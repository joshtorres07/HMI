from tkinter import *

def quitEvent(event):
    root.quit()
root = Tk()
root.title("Menu example")
root.geometry("200x200")
root.config(width=100, height=300)
def one(event):
    pass
def two():
    pass
def three():
    pass
def four():
    pass

#Create menu bar
menubar = Menu(root)
#create options menu
menu1 =  Menu(menubar, tearoff=1)
#add to window
root.config(menu=menubar)
#create options menu
menu1.add_command(label="Option 1", accelerator="Ctrl_U", command=one)
menu1.add_command(label="Option 2", command=two)
menu1.add_command(label="Option 3", command=three)
menu1.add_command(label="Option 4", command=four)
menu1.add_separator()
menu1.add_command(label="Exit", accelerator='Ctrl_Q', command=root.destroy)
menubar.add_cascade(menu=menu1, label="Menu 1")
root.bind_all("<Control-q>", quitEvent)
root.bind_all("<Control-u>", one)
root.mainloop()
