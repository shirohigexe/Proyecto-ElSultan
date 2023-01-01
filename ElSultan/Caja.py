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

    def Facturacion(self,valor_consumo,pago):#metodo para generar una factura
        self._CajaBase += valor_consumo #se suma la ganancia
        devolucion = pago - valor_consumo #se calcula cuanto se debe devolver al cliente
        return 'Devuelve {}'.format(devolucion)