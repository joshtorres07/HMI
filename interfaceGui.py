from tkinter import *
class ExamGui():
    def __init__(self):
        root = Tk()
        root.title("Class Example")
        root.geometry("400x300")
        root.configure(bg='blue')
        root.resizable(0,0)
        root.eval('tk::PlaceWindow . center')
        et =  Label(root, text="Good morning", bg='blue', fg='white')
        bt =  Button(root, text="Exit", command=quit)
        et.pack()
        bt.pack()
        root.mainloop()

def main():
    ap =  ExamGui()

if __name__ == '__main__':
    main()