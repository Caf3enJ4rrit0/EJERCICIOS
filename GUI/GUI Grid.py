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
frame.config(bg="#a120c1", width="350", height="350", relief="groove", bd=10, cursor="gumby")

#Creo un entradas en posiciones segun grilla
nombre = tk.Label(frame, bg="#a120c1", fg="white", text="Nombre: ").grid(row=0, column=0, sticky="w")
edad = tk.Label(frame, bg="#a120c1", fg="white", text="Edad: ").grid(row=1, column=0, sticky="w")
dni = tk.Label(frame, bg="#a120c1", fg="white", text="DNI: ").grid(row=2, column=0, sticky="w")

cuadro_nombre = tk.Entry(frame).grid(row=0, column=1)
cuadro_edad = tk.Entry(frame).grid(row=1, column=1)
cuadro_dni = tk.Entry(frame).grid(row=2, column=1)


# Llamo al metodo mainloop para darle forma de GUI a mi raiz
root.mainloop()