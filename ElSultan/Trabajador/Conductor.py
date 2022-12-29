from Trabajador.Trabajador import *

class Conductor(Trabajador):
    Enruta = False

    def __init__(self,Auto,Enruta):
        self.Auto = Auto
        self.Enruta = Enruta


        