class Trabajador:
    #podemos poner un atributo de clase que sea un salariop base (minimo) con metodo de clase aceedemos a el.

    def __init__(self,Nombre,Id,Salario,Clave):
            self.Nombre = Nombre
            self.Id = Id
            self.Salario = Salario
            self.Clave = Clave

    #metedos get de los atributos

    def getNombre(self):
        return self.Nombre

    def getId(self):
        return self.Id

    def getSalario(self):
        return self.Salario

    def getClave(self):
        return self.Clave

    #metodos asoaciados a la clase

    def Entrada(self, datatime):
        return None

    def Salida(self, datatime):
        return None

    def CambiarClave(self, String):
        self.Clave == String

    def ComprobarClave(self,intento):
        if intento == self.Clave:
            return True
        return False