import pickle 

from gestorAplicaciones.Trabajador import Trabajador

import pathlib
import os

class Serializador():
    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muñeco")

    def serializarTodo(cls):

        Serializador.serializar(Trabajador.getTrabajadores(), "Trabajadores")