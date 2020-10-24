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

imagen = tk.PhotoImage(file="fry.png")
tk.Label(frame, image=imagen).place(x=15, y=15)



# Llamo al metodo mainloop para darle forma de GUI a mi raiz
root.mainloop()