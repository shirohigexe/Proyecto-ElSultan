#################Creacion de clase #################
class Caja:

    Clave = "asdfghjklñ456"

#############Creacion del Metodo init##############
    def __init__(self,Cajero):
        self._CajaBase = 100000
        self._Usuario = Cajero
        

########metodos especiales#############
    def PagarEmpleados(self,Trabajador):
        pass ##pago al trabajador pendiente

    @classmethod
    def IngresaClave(cls,IntentoClave):#verificacion de clave de acceso
        if IntentoClave == cls.Clave:
            return True
        return False

    @classmethod
    def CambiarClave(cls,NuevaClave):#metodo para cambiar la clave de acceso
        cls._Clave = NuevaClave
