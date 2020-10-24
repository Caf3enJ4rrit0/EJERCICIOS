# Creacion de Root

import tkinter as tk

# creo una raiz instanciando la clase Tk()
root = tk.Tk()

# Configuro la raiz
root.title("Mi primera GUI")
root.config(bg="#000000")

# creo el frame
frame = tk.Frame()
"""frame.pack(side="left", anchor="n")"""                          #donde ubica el frame
frame.pack(expand=True)                                            #para que se centre en la ventana
"""frame.pack(expand=True, fill="both", padx=20, pady=20)"""       #otra forma de modificar y ubicar el frame
frame.config(bg="#a120c1", width="350", height="350", relief="groove", bd=10, cursor="pirate")

# Llamo al metodo mainloop para darle forma de GUI a mi raiz
root.mainloop()