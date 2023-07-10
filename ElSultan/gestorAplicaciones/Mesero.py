from gestorAplicaciones.Trabajador import *
from gestorAplicaciones.Orden import *
######creacion de la clase#######
class Mesero(Trabajador):

######metodo Inicializador######
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)
        self._Orden = None

#######metodos especiales######
    def TomarOrden(self,p,c,e,s,b):
        self._Orden = Orden(p,c,e,s,b) #de la clase orden
        return self._Orden

    def DarMenu(self):
        pass#no esta listo, debido a que logro visualizar el menu
