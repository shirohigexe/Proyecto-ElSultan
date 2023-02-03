from datetime import datetime

class Trabajador:
    #podemos poner un atributo de clase que sea un salariop base (minimo) con metodo de clase aceedemos a el.
    _Trabajadores = []

    def __init__(self,Nombre,Id,Salario,Clave):
        self.Nombre = Nombre
        self.Id = Id
        self.Salario = Salario
        self.Clave = Clave
        self.fechaEntrada = None
        self.fechaSalida = None
        self._Trabajadores.append(self)

    #metedos get de los atributos
    def getFechaEntrada(self):
        return "{}/{}/{}".format(self.fechaEntrada.day,self.fechaEntrada.month,self.fechaEntrada.year)

    def getFechaSalida(self):
        return "{}/{}/{}".format(self.fechaSalida.day,self.fechaSalida.month,self.fechaSalida.year)

    def getNombre(self):
        return self.Nombre

    def getId(self):
        return self.Id

    def getSalario(self):
        return self.Salario

    def getClave(self):
        return self.Clave

    #metodos asoaciados a la clase

    def Entrada(self, datetime):
        return None

    def Salida(self, datetime):
        return None

    def CambiarClave(self, String):
        self.Clave == String

    def ComprobarClave(self,intento):
        if intento == self.Clave:
            return True
        return False

    #metodos de clase
    @classmethod
    def getTrabajadores(cls):
        return cls._Trabajadores

