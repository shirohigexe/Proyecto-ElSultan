from gestorAplicaciones.Trabajador import *
from gestorAplicaciones.Orden import *

class Conductor(Trabajador):

##########se crea el metodo inicializador#########
    def __init__(self,Auto):
        self._Auto = Auto
        self._Enruta = False#indicara si esta ocupado o no
        self._Ordenes = {}#un diccionario para que la clave sea la direccion del pedido y el valor sea la Orden en si

############metodos de clase#########
    def InicioRuta(self):
        self._Enruta = True#ocupa al conductor

    def FinalizarRuta(self):
        self._Enruta = False#desocupa al conductor

    def PedidoEntregado(self,dirc):
        self._Ordenes.pop(dirc) #con esto eliminamos el par clave:valor del pedido a entregar

    def RecibirPedido(self,Orden, dirc):
        self._Ordenes[dirc] = Orden #agregamos la orden al conductor con su respectiva direccion