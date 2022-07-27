class Trabajador():
    Trabajadores = []

    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario
        self.tiempo = 0
        self.Trabajadores.append(self)

    def __str__(self):
        return self.nombre

    def getSalario(self):
        return "el salario de {} es de {}".format(self.nombre,self.salario)

    def getnombre(self):
        return self.nombre

    def setSalario(self,nuevoSalario):
        self.salario = nuevoSalario

    @classmethod
    def hecharTrabajador(cls,trabajador):
        cls.Trabajadores.remove(trabajador)

    @classmethod
    def agregarTrabajador(cls, trabajador):
        cls.Trabajadores.append(trabajador)

    @classmethod
    def listaT(cls):
        return cls.Trabajadores



elder = Trabajador("elder torres",500000)
yia = Trabajador("yia cardoa", 300000)
for i in Trabajador.listaT():
    print(i.getSalario())