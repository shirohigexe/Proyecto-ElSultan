from Trabajador import *

########creacion de la clase########
class Cajero(Trabajador):

########metodo inizializador##########
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)

########metodos especiales por completar#######
    def GenerarFactura(self):
        pass


###Nota, tal vez se deba tener en cuenta otros cambios#########