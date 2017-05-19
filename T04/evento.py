__author__ = 'Ricardo Del Rio'

from contenidos import Contenido
from random import random, randint
from integrantes import Alumno, AyudanteDocencia



class Evento:
    '''
    Esta clase representa los eventos que se llevaran a cabo en la simulacion.
    '''
    lista_eventos = []
    eventos_ocurridos = []
    evento_actual = None
    tipos = {1: 'actividad',
             2: 'tarea',
             3: 'control',
             4: 'examen',
             5: 'ayudantia',
             6: 'catedra',
             7: 'entrega_nota_evaluacion'}
    def __init__(self, tiempo, tipo, funciones, contenido=None):
        self.tiempo = tiempo
        self.tipo = tipo
        self.__numero = None
        self.funciones = funciones
        #Si es una evaluación:
        if contenido:
            self.exigencia = 7 + (randint(1, 5) / contenido.dificultad)
            self.cont_a_evaluar = contenido
        Evento.lista_eventos.append(self)

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

    @staticmethod
    def creacion_eventos_principales():
        '''
        Se crean los eventos que pueden crearse al comienzo de la simulación.
        :return:
        '''
        # Actividades:
        fecha = 4 #Considerando la primera actividad el primer jueves
        funciones = [] # revisar: agregar las funciones correspondientes
        for contenido in Contenido.lista_contenidos:
            Evento(1, fecha, contenido)
            fecha += 7

        # Controles:
        c_controles = 0
        fecha = 11  # Considerando el primer control el segundo jueves
        fechas_controles = []
        funciones = [] # revisar: agregar las funciones correspondientes
        while (c_controles < 5) and semana(fecha) < 12:
            if (fecha - 7) in fechas_controles:
                pass
            else:
                num = random()
                if num <= 0.7:
                    Evento(fecha, 3, funciones, Contenido.lista_contenidos[semana(fecha)])
                    c_controles += 1
            fecha += 7
        # Si es que no se distribuyeron los 5 controles en el maximo de tiempo posible.
        if c_controles < 5:
            fecha = 11
            while c_controles < 5:
                if (fecha - 7) in fechas_controles:
                    pass
                else:
                    Evento(fecha, 3, funciones, Contenido.lista_contenidos[semana(fecha)])
                    c_controles += 1
                fecha += 7
                print('2 cantidad de controles: {}'.format(c_controles))


        # Tarea (Entrega de enunciado)
        fecha = 1
        funciones = [] # revisar: completar funciones
        for i in range(6):
            Evento(fecha, 2, funciones, Contenido.lista_contenidos[semana(fecha)])
            fecha += 7

        # Ayudantias:
        funciones = []  # revisar: establecer funciones
        fecha = 2  # La primera ayudantia es el primer martes
        while fecha < 84:
            Evento(fecha, 5, funciones)
            fecha += 7

        # Catedra:
        funciones = []  # revisar: establecer funciones
        fecha = 4  # La primera catedra es el primer jueves
        while fecha < 84:
            Evento(fecha, 6, funciones)
            fecha += 7


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
        Evento.eventos_ocurridos.append(Evento.evento_actual)

    def ejecutar_evento(self):
        for funcion in Evento.evento_actual.funciones:
            funcion()

# ----------------------------------------------------------------------------------------------------------------------

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

def semana(dia):
    '''
    Esta función calcula a que semana pertenece cierto día.
    Usada para ver que contenido se está viendo.
    :param dia:
    :return:
    '''
    return (dia//7)+1


numero_evento = gen_numero()
numero_actividad = gen_numero()
numero_tarea = gen_numero()
numero_control =
