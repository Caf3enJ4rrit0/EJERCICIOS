# Creacion de Root

import tkinter as tk

# creo una raiz instanciando la clase Tk()
root = tk.Tk()

# Configuro la raiz
root.title("Mi primera GUI")
root.config(bg="#000000")

# Llamo al metodo mainloop para darle forma de GUI a mi raiz
root.mainloop()