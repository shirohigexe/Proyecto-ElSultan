class User:
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

    # metedos set de los atributos

    def setNombre(self,nNombre):
        self.Nombre = nNombre

    def setId(self,nId):
        self.Id = nId

    def setNombre(self,nSalario):
        self.Salario = nSalario

    def setNombre(self,nClave):
        self.Clave = nClave

    #metodos asoaciados a la clase

    def Entrada(self, datatime):
        return None

    def Salida(self, datatime):
        return None

    def CambiarClave(self, String):
        return None

    def IngresarClave(self, String):
        return None