from Trabajador.Trabajador import *
from Orden import *

######creacion de la clase#######
class Mesero(Trabajador):

######metodo Inicializador######
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)

#######metodos especiales######
    def TomarOrden(self,Orden):
        orden = Orden #de la clase orden
        pass#no esta listo

    def PasarOrden(self):
        pass #no esta listo

    def DarMenu(self):
        pass#no esta listo
