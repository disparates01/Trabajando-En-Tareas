from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys

import numpy
import matplotlib


class T03Window(MyWindow):
    def __init__(self):
        super().__init__()

    def process_consult(self, querry_array):
        # Agrega en pantalla la solución. Muestra los graficos!!
        print(querry_array)
        text = "Probando funcion\nConsulta 01\n"
        self.add_answer(text)

    def save_file(self, querry_array):
        # Crea un archivo con la solucion. NO muestra los graficos!!
        print(querry_array)

## -------------------------------------------------------------------------------------------------------------SIMBOLOS

simbolos_comparacion = ('==', '>', '<', '>=', '<=', '!=')
simbolos_operaciones = ('+', '-', '*', '/', '>=<')

## -----------------------------------------------------------------------------------------------------COMANDOS BASICOS

def asignar(variable, comando_o_dato):
    '''
    Guarda el valor de  retorno de comando o el valor de dato, bajo el nomnre 'variable'. No permite guardar
    información si el nombre ingresado es igual al nombre de algún comando propio de RQL o al nombre de alguna
    distribución de probabilidad.
    :param variable: str
    :param comando o dato: any
    :returns: None
    '''
    pass

def crear_funcion(nombre_modelo, *parametpros):
    '''
    Recibe el nombre de algun modelo de probabilidad y los parametros dnecesarios por el modelo, y retorna una nueva
    funcion que puede ser ocupada en el comando 'evaluar' para generar una columna de datos
    :param nombre_modelo: str ("normal", "gamma", "exponencial")
    :param *parametros: int or float
    :returns: funcion
    '''
    pass

def graficar(columna_opcion):
    # Se puede usar matplotlib 2.0 y numpy 1.12
    '''
    Grafica(2D) los datos de una columna. El eje Y correspondera a los valores de columna. EL eje X dependera de
    'opcion':
    ’numerico’ El eje X corresponde a una enumeraci´on de los datos. Por ejemplo, si los datos son [10, 12, 13],
        entonces los puntos del gr´aﬁco ser´an [(0, 10), (1, 12), (2, 12)]
    ’normalizado’ El eje X corresponde a una enumeracion normalizada de los datos. Por ejemplo, si los datos son
        [10, 12, 13], los puntos del graﬁco seran [(0/(10+12+13), 10), (1/35, 12), (2/35, 12)]
    ’rango:a,b,c’ Dado un string con el formato ’rango:a,b,c’, se debera interpretar del siguiente modo: Se deﬁne
        un rango de valores dado [a, b] y un step c, el eje X se compondra por los numeros generados por dicho rango.
        Esto solo es posible si la cantidad de numeros generados por el rango es mayor o igual a la cantidad de datos.
        Ademas, si a<b, entonces c debe ser positivo; mientras que si a>b, entonces c debe ser negativo.
    Columna Si, en lugar de recibir un string, se recibe otra columna de datos en el argumento opcion,
        los valores de la nueva columna seran el eje X. Esta columna debe tener la misma cantidad de datos que la
        utilizada para el eje Y .
    '''
    pass


## ---------------------------------------------------------------------------COMANDOS QUE RETORNAN UN CONJUNTO DE DATOS

def extraer_columna(nombre_de_archivo, columna):
    '''
    Dado un nombre de archivo en formato csv, retorna la columna cuyo nombre (´o head) sea igual a columna.
    :param nombre_del_archivo: str
    :param columna: str
    :returns: Columna
    '''
    pass

def filtrar(columna, sımbolo, valor):
    '''
    Dado un conjunto de datos en columna, retorna todos los que pasen el ﬁltro dado por sımbolo y valor.
    El argumento simbolo debe ser un simbolo de comparacion.
    :param columna: Columna
    :param simbolo: str
    :param valor: int or float
    :returns: Columna
    '''
    pass

def operar(columna, simbolo, valor):
    '''Dado un conjunto de datos, un simbolo de operacion, y un valor, se aplica la operacion indicada por simbolo
    y valor a cada dato de columna, y se retornan esos resultados. Si el sımbolo es >=<, entonces valor debe ser ≥ 0,
    e indica cuantos decimales aproximar. El argumento sımbolo debe ser un sımbolo de operacion.
    '''



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
