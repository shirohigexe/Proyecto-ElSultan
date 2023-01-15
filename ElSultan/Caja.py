from datetime import datetime
from datetime import timedelta
import pandas as pd
from Negocio import *

#################Creacion de clase #################
class Caja:

    Clave = "asdfghjklñ456"

#############Creacion del Metodo init##############
    def __init__(self,Cajero,negocio):
        self._Negocio = negocio
        self._CajaBase = 100000
        self._Usuario = Cajero

########metodos de la clase###############

    @classmethod
    def IngresaClave(cls,IntentoClave):#verificacion de clave de acceso
        if IntentoClave == cls.Clave:
            return True
        return False

    @classmethod
    def CambiarClave(cls,NuevaClave):#metodo para cambiar la clave de acceso
        cls._Clave = NuevaClave

########metodos especiales#############
    def PagarEmpleados(self,Trabajador):
        pass ##pago al trabajador pendiente

    def Facturacion(self,valor_consumo,pago):#metodo para generar una factura
        self._CajaBase += valor_consumo #se suma la ganancia
        devolucion = pago - valor_consumo #se calcula cuanto se debe devolver al cliente
        return 'Devuelve {}'.format(devolucion)

    def Banlance(self,ingresos,gastos):#funcion encargada de generar reportes de ingresos y gastos en achivos .xlsx 

        now = datetime.now()#capturamos los datos de la fecha actual para generar el informe
        tomorrow = now + timedelta(days=1)#capturamos la fecha de manana

        if (self._Negocio.Estado() == False):#esto indica que el negocio cerro

            try:#tratamos de agregar una fila
                archivo = pd.read_excel('informes/{}.xlsx'.format(now.year),sheet_name='{}'.format(now.month))#se lee el archivo xlsx y se combierte en un dataframe
                nueva_fila = {'dia':now.day,'ingresos':ingresos,'gastos':gastos, 'balance':ingresos-gastos}#la nueva fila ha agregar
                archivo.loc[len(archivo.index)] = nueva_fila#se agrega la fila al dataframe
                with pd.ExcelWriter('informes/{}.xlsx'.format(now.year),mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
                    archivo.to_excel(writer,sheet_name='{}'.format(now.month)) # se hace la modificacion en el archivo

            except FileNotFoundError:#si el archivo no es encontrado, indicador de que no existe, se crea otro librio
                nuevoArchivo = pd.DataFrame(columns=['dia','ingresos','gastos','balance'])#dado que no existe un archivo, se creara otro
                nueva_fila = {'dia':now.day,'ingresos':ingresos,'gastos':gastos, 'balance':ingresos-gastos}#la nueva fila ha agregar
                nuevoArchivo.loc[len(nuevoArchivo.index)] = nueva_fila#se agrega la fila al dataframe
                nuevoArchivo.to_excel('informes/{}.xlsx'.format(now.year),sheet_name='{}'.format(now.month))

            except ValueError:#la hoja no fue encontrada en este caso
                archivo = pd.read_excel('informes/{}.xlsx'.format(now.year))#se lee el archivo xlsx y se combierte en un dataframe
                nueva_fila = {'dia':now.day,'ingresos':ingresos,'gastos':gastos, 'balance':ingresos-gastos}#la nueva fila ha agregar
                archivo.loc[len(archivo.index)] = nueva_fila#se agrega la fila al dataframe
                with pd.ExcelWriter('informes/{}.xlsx'.format(now.year),mode='a',engine='openpyxl',if_sheet_exists='replace') as writer:
                    archivo.to_excel(writer,sheet_name='{}'.format(now.month)) # se hace la modificacion en el archivo

elSultan = Negocio('El Sultan')
print(elSultan.Estado())
caja1 = Caja('david',elSultan)
caja1.Banlance(700000,152850)
