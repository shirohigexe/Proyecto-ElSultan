################creacion de clase###########
class Cliente:

##############creacion del metodo init#############
    def __init__(self,nombre,id):
        self._Nombre = nombre
        self._id = id

###########metodos gett y str#############
    def getNombre(self):
        return self._Nombre
    
    def getID(self):
        return self._id

    def __str__(self):
        return "hola, soy {}".format(self._Nombre)

##########metodos especiales######################
    def RealizarPedidos(self):#metodo para realizar un pedido
        pass
    #Nota: no está listo

    def CancelarPedido(self):#metodo para cancelar un pedido
        pass
    #Nota: no está listo

    def PedirMenu(self):#metodo para visualizar el menu
        pass
    #Nota: no está listo