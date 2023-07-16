from tkinter import Tk,Label, Button, Entry
import tkinter as tk

#Ventana de caja
venta_caja = Tk()
venta_caja.geometry("600x300")
venta_caja.title("Caja ElSultan")
icono = tk.PhotoImage(file="uiMain/imagenes/DALLE.png")
venta_caja.iconphoto(True,icono)



venta_caja.mainloop()