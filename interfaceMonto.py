from tkinter import *
from tkinter import ttk

def calcular(monto, intereses):
    resultado = monto * intereses / 100
    accion.configure(text='hola ' + resultado.get())
    return resultado
root = Tk()
root.title("Intreses de prestamo")
monto = DoubleVar()
et = ttk.Label(root, text = "Monto")
et.grid (column =0, row =0)
montoCap = ttk.Entry(root, width = 20, textvariable = monto)
montoCap.grid(column = 0, row=1)

et2 = ttk.Label(root, text = "intereses")
et2.grid (column =2, row =0)
intereses = DoubleVar()
interes = ttk.Entry(root, width = 20, textvariable = intereses)
interes.grid(column = 2, row=1)

accion = ttk.Button(root, text= "calcular monto total", command= calcular(monto,intereses))
accion.grid(column = 1, row = 4)


root.mainloop()
