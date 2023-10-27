import tkinter as tk
import json

# Función para guardar datos en el archivo JSON
def guardar_datos():
    datos = {
        "ID": id_entry.get(),
        "Apellido Paterno": apellido_p_entry.get(),
        "Apellido Materno": apellido_m_entry.get(),
        "Nombre": nombre_entry.get(),
        "Calle": calle_entry.get(),
        "Número Exterior": num_ext_entry.get(),
        "Código Postal": cp_entry.get(),
        "Ciudad": ciudad_entry.get(),
        "Estado": estado_entry.get(),
        "Email": email_entry.get()
    }
    with open('agenda.json', 'a') as archivo:
        json.dump(datos, archivo)
        archivo.write('\n')
    limpiar_campos()

# Función para buscar datos por ID
def buscar_por_id():
    id_buscar = id_buscar_entry.get()
    with open('agenda.json', 'r') as archivo:
        for linea in archivo:
            datos = json.loads(linea)
            if datos['ID'] == id_buscar:
                id_entry.delete(0, tk.END)
                id_entry.insert(0, datos['ID'])
                id_entry.config(state=tk.DISABLED)

                apellido_p_entry.delete(0, tk.END)
                apellido_p_entry.insert(0, datos['Apellido Paterno'])
                apellido_p_entry.config(state=tk.DISABLED)

                apellido_m_entry.delete(0, tk.END)
                apellido_m_entry.insert(0, datos['Apellido Materno'])
                apellido_m_entry.config(state=tk.DISABLED)

                nombre_entry.delete(0, tk.END)
                nombre_entry.insert(0, datos['Nombre'])
                nombre_entry.config(state=tk.DISABLED)

                calle_entry.delete(0, tk.END)
                calle_entry.insert(0, datos['Calle'])
                calle_entry.config(state=tk.DISABLED)

                num_ext_entry.delete(0, tk.END)
                num_ext_entry.insert(0, datos['Número Exterior'])
                num_ext_entry.config(state=tk.DISABLED)

                cp_entry.delete(0, tk.END)
                cp_entry.insert(0, datos['Código Postal'])
                cp_entry.config(state=tk.DISABLED)

                ciudad_entry.delete(0, tk.END)
                ciudad_entry.insert(0, datos['Ciudad'])
                ciudad_entry.config(state=tk.DISABLED)

                estado_entry.delete(0, tk.END)
                estado_entry.insert(0, datos['Estado'])
                estado_entry.config(state=tk.DISABLED)

                email_entry.delete(0, tk.END)
                email_entry.insert(0, datos['Email'])
                email_entry.config(state=tk.DISABLED)

                return
        resultado_label.config(text="ID no encontrado.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    id_entry.config(state=tk.NORMAL)
    id_entry.delete(0, tk.END)

    apellido_p_entry.config(state=tk.NORMAL)
    apellido_p_entry.delete(0, tk.END)

    apellido_m_entry.config(state=tk.NORMAL)
    apellido_m_entry.delete(0, tk.END)

    nombre_entry.config(state=tk.NORMAL)
    nombre_entry.delete(0, tk.END)

    calle_entry.config(state=tk.NORMAL)
    calle_entry.delete(0, tk.END)

    num_ext_entry.config(state=tk.NORMAL)
    num_ext_entry.delete(0, tk.END)

    cp_entry.config(state=tk.NORMAL)
    cp_entry.delete(0, tk.END)

    ciudad_entry.config(state=tk.NORMAL)
    ciudad_entry.delete(0, tk.END)

    estado_entry.config(state=tk.NORMAL)
    estado_entry.delete(0, tk.END)

    email_entry.config(state=tk.NORMAL)
    email_entry.delete(0, tk.END)


    resultado_label.config(text="")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda")
ventana.geometry("250x310")
ventana.configure(bg="white")

# Crear y posicionar etiquetas y campos de entrada
id_label = tk.Label(ventana, text="ID:", bg="white")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(ventana)
id_entry.grid(row=0, column=1)

apellido_p_label = tk.Label(ventana, text="Apellido Paterno:", bg="white")
apellido_p_label.grid(row=1, column=0)
apellido_p_entry = tk.Entry(ventana)
apellido_p_entry.grid(row=1, column=1)

apellido_m_label = tk.Label(ventana, text="Apellido Materno:", bg="white")
apellido_m_label.grid(row=2, column=0)
apellido_m_entry = tk.Entry(ventana)
apellido_m_entry.grid(row=2, column=1)

nombre_label = tk.Label(ventana, text="Nombre:", bg="white")
nombre_label.grid(row=3, column=0)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=3, column=1)

calle_label = tk.Label(ventana, text="Calle:", bg="white")
calle_label.grid(row=4, column=0)
calle_entry = tk.Entry(ventana)
calle_entry.grid(row=4, column=1)

num_ext_label = tk.Label(ventana, text="Número Exterior:", bg="white")
num_ext_label.grid(row=5, column=0)
num_ext_entry = tk.Entry(ventana)
num_ext_entry.grid(row=5, column=1)

cp_label = tk.Label(ventana, text="Código Postal:", bg="white")
cp_label.grid(row=6, column=0)
cp_entry = tk.Entry(ventana)
cp_entry.grid(row=6, column=1)

ciudad_label = tk.Label(ventana, text="Ciudad:", bg="white")
ciudad_label.grid(row=7, column=0)
ciudad_entry = tk.Entry(ventana)
ciudad_entry.grid(row=7, column=1)

estado_label = tk.Label(ventana, text="Estado:", bg="white")
estado_label.grid(row=8, column=0)
estado_entry = tk.Entry(ventana)
estado_entry.grid(row=8, column=1)

email_label = tk.Label(ventana, text="Email:", bg="white")
email_label.grid(row=9, column=0)
email_entry = tk.Entry(ventana)
email_entry.grid(row=9, column=1)

# Crear botones
guardar_button = tk.Button(ventana, text="Guardar", command=guardar_datos, bg="green", fg="white")
guardar_button.grid(row=10, column=0)

id_buscar_label = tk.Label(ventana, text="Buscar por ID:", bg="white")
id_buscar_label.grid(row=11, column=0)
id_buscar_entry = tk.Entry(ventana)
id_buscar_entry.grid(row=11, column=1)
buscar_button = tk.Button(ventana, text="Buscar", command=buscar_por_id , bg="purple", fg="white")
buscar_button.grid(row=13, column=0)
resultado_label = tk.Label(ventana, text="", bg="white")
resultado_label.grid(row=12, column=1)

limpiar_button = tk.Button(ventana, text="Limpiar", command=limpiar_campos, bg="blue", fg="white")
limpiar_button.grid(row=13, column=1)

ventana.mainloop()
