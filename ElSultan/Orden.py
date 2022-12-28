############creacion de la clase#############
class Orden:

############creacion del metodo init########
    def __init__(self,P,C,E,S,B):
        self._Proteina = P
        self._Carbohidrato = C
        self._Ensalada = E
        self._Sopa = S
        self._Bebida = B

############metodos gett y sett############
    def getProteina(self):
        return self._Proteina

    def getCarbohidrato(self):
        return self._Carbohidrato

    def getEnsalada(self):
        return self._Ensalada

    def getSopa(self):
        return self._Sopa

    def getBebida(self):
        return self._Bebida

##############################
    def setProteina(self,newP):
        self._Proteina = newP

    def setCarbohidrato(self,newC):
        self._Carbohidrato = newC

    def setEnsalada(self,newE):
        self._Ensalada = newE

    def setSopa(self,newS):
        self._Sopa = newS

    def setBebida(self, newB):
        self._Bebida = newB
