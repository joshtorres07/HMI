import tkinter as tk
import random

def iniciar_juego():
    global numero_secreto, intentos_restantes
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 3
    entry_estado.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_numero.config(state=tk.NORMAL)
    boton_verificar.config(state=tk.NORMAL)
    boton_jugar.config(state=tk.DISABLED)

def verificar_numero():
    global intentos_restantes
    intentos_restantes -= 1
    numero_ingresado = entry_numero.get()

    try:
        numero_ingresado = int(numero_ingresado)
    except ValueError:
        entry_estado.delete(0, tk.END)
        entry_estado.insert(0, "Ingresa un número válido (1-100)")
        entry_estado.config(fg="red")
        return

    if numero_ingresado < numero_secreto:
        entry_estado.delete(0, tk.END)
        entry_estado.insert(0, "Intenta un número más alto. Intentos restantes: " + str(intentos_restantes))
        entry_estado.config(fg="red")
    elif numero_ingresado > numero_secreto:
        entry_estado.delete(0, tk.END)
        entry_estado.insert(0, "Intenta un número más bajo. Intentos restantes: " + str(intentos_restantes))
        entry_estado.config(fg="red")
    else:
        entry_estado.delete(0, tk.END)
        entry_estado.insert(0, "¡Felicidades! Adivinaste el número.")
        entry_estado.config(fg="green")
        boton_verificar.config(state=tk.DISABLED)
    entry_numero.delete(0, tk.END)

    if intentos_restantes == 0:
        entry_estado.delete(0, tk.END)
        entry_estado.insert(0, "¡Perdiste! El número correcto era " + str(numero_secreto))
        entry_estado.config(fg="red")
        boton_verificar.config(state=tk.DISABLED)


ventana = tk.Tk()
ventana.title("Adivina el número")
ventana.configure(bg="white")
ventana.geometry("270x200")

# Inicializar variables
numero_secreto = 0
intentos_restantes = 3

adivinado_label =  tk.Label(ventana, text="Adivinando un número", fg="blue", bg="white", font=("Arial", 13))
boton_jugar = tk.Button(ventana, text="Jugar", command=iniciar_juego, fg="white", bg="green")
entry_numero = tk.Entry(ventana, width=10)
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_numero, state=tk.DISABLED, bg="cyan")
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, fg="white", bg="red")
entry_estado = tk.Entry(ventana, width=40)

adivinado_label.pack(fill="x", expand=True)
boton_jugar.pack(fill="x", expand=True)
entry_numero.pack(fill="x", expand=True)
boton_verificar.pack(fill="x", expand=True)
boton_salir.pack(fill="x", expand=True)
entry_estado.pack(fill="x", expand=True)

ventana.mainloop()
