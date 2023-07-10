from gestorAplicaciones.Trabajador import *
from gestorAplicaciones.Negocio import *
from datetime import datetime

######creacion de la clase########
class Administrador(Trabajador):

#####metodo inicializador#######
    def __init__(self, Nombre, Id, Salario, Clave):
        super().__init__(Nombre, Id, Salario, Clave)

######metodos especiales########
    def AgregarEmpleado(self,nombre=None,id=None,salario=None,clave=None, empleado=None):#metodo para agregar un empleado al atributo de clase de la clase negocio
        empleado = empleado
        if empleado == None:
            nuevo = Trabajador(nombre,id,salario,clave)
            nuevo.fechaEntrada = datetime.now()
            Negocio.Empleados.append(nuevo)
        else:
            Negocio.Empleados.append(empleado)

    def DespedirEmpleado(self,id):#metodo para eliminar un empleado del negocio
        for i in Negocio.Empleados: #buscamos al empleado deacuerdo al id
            if i.getId() == id:
                i.fechaSalida = datetime.now()
                Negocio.Despedidos.append(i)
                Negocio.Empleados.remove(i) #lo removemos

    def CambiarSalario(self,id,nuevo):#Metodo para cambiar el salario del empleado
        for i in Negocio.Empleados:
            if i.getId() == id:
                i.Salario = nuevo

