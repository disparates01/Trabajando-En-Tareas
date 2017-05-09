__author__ = 'Ricardo Del Rio'

from random import choice, random

'''
COMENTARIOS
-Prefijos Usados:
    act = actualizar
    det = determinar
    calc = calcular


'''

# ----------------------------------------------------------------------------------------------------------------------

class Integrante():
    '''
    Esta clase representa a todos los integrantes del ramo 'Avanzación Programada'.
    '''
    def __init__(self, nombre, rol, seccion=None):
        self.nombre = nombre
        self.rol = rol
        self.seccion = seccion

# ----------------------------------------------------------------------------------------------------------------------

class Alumno(Integrante):
    lista_alumnos = []
    '''
    Esta clase representa a los alumnos del curso.
    '''
    def __init__(self, nombre, rol, seccion=None):
        Integrante.__init__(self, nombre, rol, seccion)
        # Parametros que se fijan una sola vez:
        self.cantidad_de_creditos = 0
        self.personalidad = ''

        # Parametros que se modifican constantemente:
        self.horas_semana = 0 # Horas que el estudiante dedicara al curso en una semana. Se modifica semana a semana.
        self.confianza = 0
        self.manejo_de_contenidos = 0
        self.nive_de_programacion = 0
        self.nota_esperada = 0

        # Asignacion de los primeros valores:
        self.det_cant_creditos()

        # Se anade al alumno a la list de alumnos:
        Alumno.lista_alumnos.append(self)

    def det_cant_creditos(self):
        '''
        Este asigna una cantidad de creditos a un estudiante en base a la probabilidad dada.
        Se debe utilizar solamente cuando se crea un nuevo objeto 'Alumno'.
        :return:
        '''
        num = random()
        if num <= 0.1:
            self.cantidad_de_creditos = 40
        elif num <= 0.8:
            self.cantidad_de_creditos = 50
        elif num <= 0.95:
            self.cantidad_de_creditos = 55
        elif num <= 1:
            self.cantidad_de_creditos = 55

    def det_personalidad(self):
        '''
        Este metodo determina la personalidad del estudiante
        :return:
        '''
        pass

    def act_manejo_cont(self, n_materia, horas):
        '''
        Este metodo recibe el numero asociado a la materia que se está pasando y la cantidad de horas que el estudiante
        ha dedicado a su estudio.
        Modifica el atributo 'manejo_de_contenidos' del estudiante en base a la formula dada.
        :param n_materia:
        :param horas:
        :return:
        '''
        dificultad = contenidos[n_materia][1]
        self.manejo_de_contenidos = (1/dificultad) * horas







# ----------------------------------------------------------------------------------------------------------------------

class Profesor(Integrante):
    lista_profesores = []
    '''
    Esta clase representa a los profesores del curso.
    '''
    def __init__(self, nombre, rol, seccion=None):
        Integrante.__init__(self, nombre, rol, seccion)

        Profesor.lista_profesores.append(self)

# ----------------------------------------------------------------------------------------------------------------------

class Ayudante(Integrante):
    lista_ayudantes = []
    '''
    Esta clase representa a los ayudantes del curso.
    '''
    def __init__(self, nombre, rol, seccion=None):
        Integrante.__init__(self, nombre, rol, seccion)

        Ayudante.lista_ayudantes.append(self)

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

posibles_personalidades = ['eficiente', 'artistico', 'teorico']




# ----------------------------------------------------------------------------------------------------------------------

