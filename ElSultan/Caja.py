#################Creacion de clase #################
class Caja:

#############Creacion del Metodo init##############
    def __init__(self,Cajero):
        self._CajaBase = 100000
        self._Usuario = Cajero
        self._Clave = "asdfghjklñ456"

########metodos especiales#############
    def PagarEmpleados(self,Trabajador):
        pass ##pago al trabajador pendiente

    def IngresaClave(self,IntentoClave):#verificacion de clave de acceso
        if IntentoClave == self._Clave:
            return True
        return False

    def CambiarClave(self,NuevaClave):#metodo para cambiar la clave de acceso
        self._Clave = NuevaClave
