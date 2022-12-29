from Trabajador.Trabajador import *

######creacion de la clase########
class Administrador(Trabajador):

#####metodo inicializador#######
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)

######metodos especiales########
    def AgregarEmpleado(self,Trabajador):#metodo para agregar un empleado al atributo de clase de la clase negocio
        pass#No esta listo

    def DespedirEmpleado(self,Trabajador):#metodo para eliminar un empleado del negocio
        pass#no esta listo

    def CambiarSalario(self,Trabajador):#Metodo para cambiar el salario del empleado
        pass#no esta listo