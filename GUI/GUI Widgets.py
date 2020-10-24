# Creacion de Root

import tkinter as tk

# creo una raiz instanciando la clase Tk()
root = tk.Tk()

# Configuro la raiz
root.title("Mi primera GUI")
root.config(bg="#000000")

# creo el frame
frame = tk.Frame()
frame.pack(expand=True)
frame.config(bg="#a120c1", width="350", height="350", relief="groove", bd=10, cursor="pirate")

#Creo una etiqueta
tk.Label(frame, text="Mi primera etiqueta", fg="black", font=("Verdana", 16)).place(x=50, y=100)

#creo un cuadro de entrada
tk.Entry(frame).place(y=50, x=200)

#Creo un boton check
tk.Checkbutton(frame, text="Probando").place(x=50, y=50)

# Llamo al metodo mainloop para darle forma de GUI a mi raiz
root.mainloop()