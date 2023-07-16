from tkinter import Tk,Label, Button, Entry
import tkinter as tk

#comandos para botones
def va_caja():
    print("va al espacio de caja")

def ve_espacioADMIN():
    print("va al espacio del administrador")

def mostrarINFO():
    print("informacion del negocio")

def buscarEmpleado():
    print(buscar.get())


#breacion de ventana
ventana = Tk()
ventana.geometry("600x300")
ventana.title("Proyecto el Sultan")
icono = tk.PhotoImage(file="/home/shirohige/Desktop/Proyecto-ElSultan/ElSultan/uiMain/imagenes/DALLE.png")
ventana.iconphoto(True,icono)

#Label
lbl_esquina = Label(ventana,padx=75,pady=25)
lbl_esquina.grid(row=0,column=0)

#Botones 
espacio_caja = Button(ventana,command=va_caja,bg="gray",text="CAJA ",padx=73,pady=25)
espacio_caja.grid(row=1,column=0)

espacio_admin = Button(ventana,command=ve_espacioADMIN,bg="gray",text="ADMINISTRADOR",padx=45,pady=25)
espacio_admin.grid(row=2,column=0)

info_negocio = Button(ventana,command=mostrarINFO,bg="gray",text=" info ",padx=70,pady=25)
info_negocio.grid(row=3,column=0)

boton_bustar = Button(ventana,command=buscarEmpleado,bg="gray",text="buscar",padx=10,pady=10)
boton_bustar.grid(row=0,column=2)

#Entry
buscar = Entry(ventana,bg="white",width=25)
buscar.grid(row=0,column=1)

ventana.mainloop()

