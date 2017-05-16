__author__ = 'Ricardo Del Rio'


class Evento:
    '''
    Esta clase representa los eventos que se llevaran a cabo en la simulacion.
    '''
    lista_eventos = []
    evento_actual = None
    def __init__(self, tiempo, tipo):
        self.tiempo = tiempo
        self.tipo = tipo
        self.__numero = None
        self.funciones = []

    @property
    def numero(self):
        '''
        Retorna el valor de la variable '__numero'
        SI aún no se le asigna un numero al evento levanta un error.
        :return int:
        '''
        if self.__numero:
            return self.__numero
        else:
            raise ValueError('No se ha asignado un numero a este evento.')

    @numero.setter
    def numero(self, valor):
        '''
        Se le asigna el valor 'valor' a la variable '__numero'
        :param valor:
        :return:
        '''
        self.__numero = valor

    def __le__(self, other):
        '''
        Se compara que evento es menor o igual que otro en base al tiempo en el que deben ejecutarse.
        :param other:
        :return bool:
        '''
        return self.tiempo <= other.tiempo

    def seleccionar_evento(self):
        '''
        Se ordena la lista segun el tiempo en el que debe producirse un evento.
        Se selecciona el proximo evento que debe ocurrir.
        Se le asigna un numero al evente, que representa el numero de evento en ser ejecutado
        :return:
        '''
        Evento.lista_eventos.sort()
        Evento.evento_actual = Evento.lista_eventos.pop(0)
        Evento.evento_actual.numero = next(asignar_numero)

    def ejecutar_evento(self):
        for funcion in Evento.evento_actual.funciones:
            funcion()


def gen_numero():
    '''
    Esta funcion es un generador de numeros para los eventos.
    A cada evento solo se le debe asignar un numero en el momento en el que se realiza dicho evento.
    Este numero esta pensado para que las properties puedan verificar si su valor se encuentra actualizado.
    :return int:
    '''
    numero = 0
    while True:
        numero += 1
        yield numero


asignar_numero = gen_numero()
