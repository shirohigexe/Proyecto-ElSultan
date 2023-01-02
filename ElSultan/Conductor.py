from Trabajador import *

class Conductor(Trabajador):

##########se crea el metodo inicializador#########
    def __init__(self,Auto):
        self._Auto = Auto
        self._Enruta = False#indicara si esta ocupado o no

############metodos de clase#########
    def InicioRuta(self):
        self._Enruta = True#ocupa al conductor

    def FinalizarRuta(self):
        self._Enruta = False#desocupa al conductor

    def PedidoEntregado(self):
        pass #No logro visualizar correctamente el metodo

    def RecibirPedido(self,Orden):
        pass#metodo para capturar la orden