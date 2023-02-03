import pickle

from gestorAplicaciones.Trabajador import Trabajador

import pathlib
import os

class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo(cls):
        Trabajador._Trabajadores = Deserializador.deserializar(Trabajador._Trabajadores, "Trabajadores")
