from tkinter import *
from tkinter import  messagebox
import  random as rnd

def __init__(self):
    root.title("Adivinando un numero")
    root.geometry("160x250")
    root.resizable(0, 0)
    root.eval('tk::PlaceWindow . center')
    eAdNu =  Label(root, text="Adivinando un numero", highlightcolor="pink")
    bPlay = Label(root, text="Jugar", bg='green', fg='white', padx=10, pady=10, width=17)

    bExit = Button(root, text="Exit", command=quit, width=17, highlightcolor="red")
    bVer = Button(root, text="Verify", command=verify, width=17, highlightcolor="red", state=DISABLED)
    number = Entry(root, bd=5, highlightcolor="blue", highlightthickness=2, state=DISABLED)
   # numberResult =  verify(self)
    #textResult =  Text(root, text= numberResult)
    eAdNu.grid(row=0, column=0, sticky="E", padx=10, pady=10)
    bPlay.grid(row=1, column=0, sticky="E", padx=10, pady=10)
    number.grid(row=2, column=0, sticky="E", padx=10, pady=10)
    bVer.grid(row=3, column=0, sticky="E", padx=10, pady=10)
    bExit.grid(row=4, column=0, sticky="W", pady=10, padx=10)


    root.mainloop()

def verify(self):
    if generate_number() == self.number:
        return  "Felicidades has acertado el numero"
    else:
        for i in range(2):
             return f"Lo siento, no has adivinado, te quedan {i+1} intentos"
def generate_number():
    number = rnd.randint(1,100)
    return  number

def play(self):
    self.bVer['STATE'] = NORMAL
if __name__ == '__main__':
    root = Tk()
    __init__(root)