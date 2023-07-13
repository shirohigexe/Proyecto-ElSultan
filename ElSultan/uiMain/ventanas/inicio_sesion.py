#importacion de librerias y metodos
from tkinter import Tk,Label, Button, Entry
import tkinter as tk

#creacion de eventos 
def iniciar():
    if (usuario.get() == "David") and (contrasena.get() == "1234"):
        print("accedio correctamente")
    else:
        print("denegado")


#creacion de ventana de inicio de secion
ventana_inicio = Tk()
ventana_inicio.geometry("400x400")
ventana_inicio.title("Inicio de sesion")
icono = tk.PhotoImage(file="/home/shirohige/Desktop/Proyecto-ElSultan/ElSultan/uiMain/imagenes/DALLE.png")
ventana_inicio.iconphoto(True,icono)


#creacion del labels u sus respectivas entradas
lbl_wellcome = Label(ventana_inicio, text="Bienvenido a tu negocio",width=30,height=5)
lbl_wellcome.pack()

#apartado del usuario (id)
lbl_Usuario = Label(ventana_inicio, text="Usuario",width=30,height=5)
lbl_Usuario.pack()
usuario = Entry(ventana_inicio,width=30)
usuario.pack()

#apartado del usuario (contraseña)
lbl_contrasena = Label(ventana_inicio, text="Contraseña",width=30,height=5)
lbl_contrasena.pack()
contrasena = Entry(ventana_inicio,width=30)
contrasena.pack()

#creacion de botones
iniciar = Button(ventana_inicio,text="iniciar secion",command=iniciar,bg="gray",padx=15,pady=10).pack()

ventana_inicio.mainloop()