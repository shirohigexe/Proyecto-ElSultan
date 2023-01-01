import Trabajador
import Orden

######creacion de la clase#######
class Mesero(Trabajador):

######metodo Inicializador######
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)

#######metodos especiales######
    def TomarOrden(self,p,c,e,s,b):
        orden = Orden(p,c,e,s,b) #de la clase orden
        return orden

    def PasarOrden(self):
        pass #Nota, no la veo necesario

    def DarMenu(self):
        pass#no esta listo
