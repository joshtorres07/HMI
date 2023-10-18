from tkinter import *
from tkinter import  ttk, messagebox

class Windows():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400+50+50")
        self.option = IntVar()
        self.msg = StringVar(value="")
        Label(self.root,text="Windows example of predefined dialog", font =("Arial", 16)).pack()
        Radiobutton(self.root, text="Window 1", variable=self.option, value=1, command=self.selection).pack()
        Radiobutton(self.root, text="Window 2", variable=self.option, value=2, command=self.selection).pack()
        Radiobutton(self.root, text="Window 3", variable=self.option, value=3, command=self.selection).pack()
        Radiobutton(self.root, text="Window 4", variable=self.option, value=4, command=self.selection).pack()
        Radiobutton(self.root, text="Window 5", variable=self.option, value=5, command=self.selection).pack()
        Radiobutton(self.root, text="Window 6", variable=self.option, value=6, command=self.selection).pack()
        Radiobutton(self.root, text="Window 7", variable=self.option, value=7, command=self.selection).pack()
        Radiobutton(self.root, text="Window 8", variable=self.option, value=8, command=self.selection).pack()
        self.et =  Label(self.root, textvariable=self.msg).pack()
        Button(self.root, text="exit", command=self.root.destroy).pack()
        self.root.mainloop()

    def selection(self):
        op =  self.option.get()
        match op:
            case 1:
                messagebox.showinfo(title="Messages", message= "show messages")
            case 2:
                messagebox.showwarning(title="Warning", message="show warnings")
            case 3:
                messagebox.showerror(title="Error", message="show errors")
            case 4:
                x= messagebox.askquestion(title="Question", message="Will you attend to java tec day?")
                self.msg.set(str(x))
            case 5:
                x =  messagebox.askokcancel(title="Ok / No", message="Are you come to java tec day")
                self.msg.set(str(x))
            case 6:
                x = messagebox.askretrycancel(title="retry", message="retry or cancel")
                self.msg.set(str(x))
            case 7:
                x = messagebox.askyesno(title="yes/no", message="Again, will you attend java tec day")
                self.msg.set(str(x))
            case 8:
                x = messagebox.askyesnocancel(title="yes/no/cancel", message="Will you buy t-shirt")
                self.msg.set(str(x))

def main():
    ap = Windows()

if __name__ == '__main__':
    main()


