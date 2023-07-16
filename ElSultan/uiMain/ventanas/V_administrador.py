from tkinter import Tk,Label, Button, Entry
import tkinter as tk

#ventana de administrador
espacio_admin = Tk()
espacio_admin.geometry("600x300")
espacio_admin.title("Espacio de Admin")
icono = tk.PhotoImage(file="uiMain/imagenes/DALLE.png")
espacio_admin.iconphoto(True,icono)

espacio_admin.mainloop()