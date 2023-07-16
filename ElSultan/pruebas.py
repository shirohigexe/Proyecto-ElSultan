
from gestorAplicaciones.Trabajador import *
from gestorAplicaciones.Caja import *
from gestorAplicaciones.Cajero import *
from gestorAplicaciones.Cliente import *
from gestorAplicaciones.Negocio import *

negocio = Negocio("elSultan")

david = Cajero("david",1000313925,500000,1234)

Caja = Caja(david,negocio)

print(negocio.Estado())

Caja.Banlance(20000,15000)