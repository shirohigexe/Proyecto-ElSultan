from datetime import datetime


############# Creacion de la clase negocio###############
class Negocio:

    def __init__(self,Nombre): #metodo init para iniciar la clase
        self._Nombre = Nombre
        self._Empleados = []
        self._abre = 8
        self._cierra = 16

##########gett, sett y str##############
    def __str__(self):
        return self._Nombre


########metodos especiales ##############

    #metodo que retornara True si el negocio está abierto en el horario estipulado de lo contrario 
    #retorna un False
    def Estado(self):
        fecha = datetime.now()
        if fecha.hour >= self._abre and fecha.hour <= self._cierra:
            return True
        return False

    #metodo para cambiar el horario de trabajo del negocio
    def CambiarHorario(self,Horaabierto,Horacerrado):
        self._abre = Horaabierto
        self._cierra = Horacerrado
