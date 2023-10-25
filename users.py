from tkinter import *
from tkinter import messagebox

def accept():
    messagebox.showinfo("Data", "Usuario: " + str(user.get()) + "\nPassword: "+ str(password.get()))
    user.delete(0, END)
    password.delete(0, END)
    user.focus()

def cancel():
    user.delete(0, END)
    password.delete(0, END)

root = Tk()
root.title("Login")

uetq = Label(text="User: ")
petq = Label(text="Password: ")

user = Entry(root, bd=5, highlightcolor="blue", highlightthickness=2)
password = Entry(root, bd=5, highlightcolor="blue", highlightthickness=2)

bAccept = Button(root, text="Accept", command=accept)
bCancel = Button(root, text="Cancel", command=cancel)
bExit = Button(root, text="Exit", command=root.destroy)

uetq.grid(row=0, column=0, sticky="w", padx=10, pady=10)
user.grid(row=0, column=1, sticky="E", padx=10, pady=10)
petq.grid(row=1, column=0, sticky="w", padx=10, pady=10)
password.grid(row=1, column=1, sticky="E", padx=10, pady=10)
bAccept.grid(row=2, column=0, sticky="w", padx=10, pady=10)
bCancel.grid(row=2, column=1, sticky="w", padx=10, pady=10)
bExit.grid(row=2, column=2, sticky="E", padx=10, pady=10)

root.configure(cursor="spider")
root.mainloop()

"""
activebackground = color
activeforeground = color
disablebackground = color
disabledforeground = color
highlightbackground = color
"""