import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    nombre= nombre.get()
    messagebox.showinfo("Mensaje", f"Hola {nomb} bienvenido al programa")

ventana = tk.Tk()
ventana.title("Ejemplo de GUI ")

etiqueta = tk. Label (ventana, text="Ingresa tu nombre:")
etiqueta.grid(row=0, column=0, padx=5, pady=10)

nombre tk.Entry(ventana, width=40)
nombre.grid(row=0, column=1, padx=5, pady=10)

boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)

ventana.mainloop()