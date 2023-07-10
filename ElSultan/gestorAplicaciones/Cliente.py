from gestorAplicaciones.Orden import *

################creacion de clase###########
class Cliente:
#NOTA: seria buena idea aregar un contador para ver que clietne es mas frecuente y asi dar descuento
##############creacion del metodo init#############
    def __init__(self,nombre,id):
        self._Nombre = nombre
        self._id = id
        self._Pedido = None

###########metodos gett y str#############
    def getNombre(self):
        return self._Nombre
    
    def getID(self):
        return self._id

    def __str__(self):
        return "hola, soy {}".format(self._Nombre)

##########metodos especiales######################
    def RealizarPedidos(self,pro,car,ens,sop,beb):#metodo para realizar un pedido
        self._Pedido = Orden(pro,car,ens,sop,beb)

    def CancelarPedido(self):#metodo para cancelar un pedido
        self._Pedido = None

    def PedirMenu(self):#metodo para visualizar el menu
        pass
    #Nota: no está listo
