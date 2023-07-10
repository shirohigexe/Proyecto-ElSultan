from gestorAplicaciones.Trabajador import *
from gestorAplicaciones.Orden import *
###########se crea la clase#################
class Cocinero(Trabajador):##hereda de la clase Trabajador

#########metodo inicializador de herencia################
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)
        self.PreparandoOrden = False
        self.Orden = None

##########metodo get#################
    def getOcupado(self):
        return self.PreparandoOrden

#############se crean las clases especiales####
    def RecibirOrden(self,orden):
        self.Orden = orden#la orden es de la clase Orden
        self.PreparandoOrden = True#ocupa al cocinero

    def FinalizarOrden(self):#indica que la orden esta lista
        self.PreparandoOrden = False#vuelve a desocupar al cocinero
        return Orden

