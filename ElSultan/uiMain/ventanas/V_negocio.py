from tkinter import Tk,Label, Button, Entry
import tkinter as tk

#ventana de info del negocio
vent_neg = Tk()
vent_neg.geometry("600x300")
vent_neg.title("informacion del negocio")
icono = tk.PhotoImage(file="uiMain/imagenes/DALLE.png")
vent_neg.iconphoto(True,icono)

vent_neg.mainloop()