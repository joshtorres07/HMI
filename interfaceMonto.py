from tkinter import *
from tkinter import ttk

def calcular(monto, intereses):
    resultado = monto * intereses / 100
    accion.configure(text='Resultado: ' + str(resultado))
    return resultado

root = Tk()
root.title("Intereses de préstamo")
monto = DoubleVar()
et = ttk.Label(root, text="Monto")
et.grid(column=0, row=0)
montoCap = ttk.Entry(root, width=20, textvariable=monto)
montoCap.grid(column=0, row=1)

et2 = ttk.Label(root, text="Intereses")
et2.grid(column=2, row=0)
intereses = DoubleVar()
interes = ttk.Entry(root, width=20, textvariable=intereses)
interes.grid(column=2, row=1)

accion = ttk.Button(root, text="Calcular", command=lambda: calcular(monto.get(), intereses.get()))
accion.grid(column=1, row=4)

root.mainloop()
