from gestorAplicaciones.Trabajador import *

########creacion de la clase########
class Cajero(Trabajador):

########metodo inizializador##########
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)


###Nota, tal vez se deba tener en cuenta otros cambios#########