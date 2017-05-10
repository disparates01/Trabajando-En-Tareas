__author__ = 'Ricardo Del Rio'

from random import choice, random, randint, uniform
from contenidos import Contenido
from evento import Evento

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
    def __init__(self, nombre, seccion=None):
        self.nombre = nombre
        self.seccion = seccion

# ----------------------------------------------------------------------------------------------------------------------

class Alumno(Integrante):
    lista_alumnos = []
    '''
    Esta clase representa a los alumnos del curso.
    '''
    def __init__(self, nombre, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        # Parametros que se fijan una sola vez:
        self.cantidad_de_creditos = 0
        self.personalidad = '' # revisar: ingresar forma de obtener personalidad

        # REHACER TODO ESTO USANDO PROPERTIES
        # # Parametros que se modifican constantemente:
        # # Se comienza asignandoles un primer valor que luego sera modificado.
        self._horas_semana = 0 # Horas que el estudiante dedicara al curso en una semana. Se modifica semana a semana.
        self.__confianza = [None,0] # [Valor, ultimo evento que la modifico]
        # self.manejo_de_contenidos = 0
        # self.nivel_de_programacion = randint(2,10) #Se calcula semanalmente
        # self.nota_esperada = 0

        self.reunion_profesor = False # revisar: No puede visitar al profesor dos semanas seguidas
        self.fiesta = False

        self.escuho_tips_clase = False

        # Asignacion de los primeros valores:
        self.det_cant_creditos()

        # Se anade al alumno a la list de alumnos:
        Alumno.lista_alumnos.append(self)

        # revisar: estas properties no estan bien implementadas, solo estaba tirando lineas
        @property
        def horas_semana(self):
            return self._horas_semana # Horas que el estudiante dedicara al curso en una semana. Se modifica semana a semana.

        @property # Esta property deberia estar bien, usarla de molde para las demas
        def confianza(self):
            # Revisa se tiene un primer valor asignado:
            if not self._confianza:
                self._confianza = randint(2,12)
                return self.__confianza[0]

            # Revisa si el valor esta actualizado, sino, lo actualiza:
            if self.__confianza[1] < Evento.evento_actual.numero:
                                                                        # revisar: definir como debe actualizarse en base al tipo de evento
                self.__confianza += self.__act_confianza()
                # Actualiza el ultimo evento que modifico la variable
                self.__confianza[1] = Evento.evento_actual.numero
                return self.__confianza[0]


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
        dificultad = Contenido.contenido_actual.diicultad
        self.manejo_de_contenidos = (1/dificultad) * horas

    def act_nota_esperada(self):
        '''
        Este metodo revisa cual es el contenido que se esta pasando actualmente llamando a la variable
        'contenido_actual' de la clase Contenido.
        Llama a la función del objeto 'Contenido' que permite calcular la nota esperada del alumno en base a la cantidad
        de horas que dedico al estudio de la materia. Se actualiza la variable 'nota_esperada' con el retorno de dicha
        funcion.
        :return:
        '''
        self.nota_esperada = Contenido.contenido_actual.nota_esperada(self.horas_semana) # revisar: Verificar que hora de estudio es la que se debe entregar, ¿semanal, diaria?

    def __act_confianza(self):
        '''
        Actualiza el nivel de confanza del alumno semana a semana según la formula dada.
        :return:
        '''
        # Definicion de variables
        C = self.confianza
        Naf = None # Debe ser la nota final de la actividad
        Nae = None # Debe ser la nota esperada de la actividad
        Ntf = None # Debe ser la nota final de la tarea
        Nte = None # Debe ser la nota esperada de la tarea
        Ncf = None # Debe ser la nota final del control
        Nce = None # Debe ser la nota esperada del control
        # Deiniendo x:
        if Naf:
            X = 1
        else:
            x = 0
        # Definiendo y:
        if Ntf:
            y = 1
        else:
            y = 0
        if Ncf:
            z = 1
        else:
            z = 0
        # Calculando y modificando la variable 'confianza':
        confianza_notas = 3*x*(Naf - Nae) + 5*y*(Ntf - Nte) + z*(Ncf - Nce)
        return confianza_notas

    def act_nivel_programacion(self):
        '''
        Actualiza la variable 'nivel_de_programacion' en base a los casos y la formula dada.
        :return:
        '''
        # Se define 'n':
        n = None # ¿QUE RAYOS SE SUPONE QUE ES 'n'? pagina 5
        # Se define la variable 'v':
        if self.reunion_profesor:
            v = 0.08
        else:
            v = 0
        # Se define la variable 'w':
        if self.fiesta:
            w = 0.15
        else:
            w = 0
        # Se define la formula:
        if n == 1:
            Pn = random(2,10)
        if n > 1:
            Pn = 1.05*(1 + v + w) * self.nivel_de_programacion # revisar: que se cumpla que es el nivel de programacion anterior despues de hacer cambios


# ----------------------------------------------------------------------------------------------------------------------

class Profesor(Integrante):
    dict_profesores = {}
    '''
    Esta clase representa a los profesores del curso.
    '''
    def __init__(self, nombre, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        self.dia_consultas_alumnos = None
        self.alumnos_quieren_reunion = []
        self.alumnos_semana = []
        Profesor.dict_profesores[seccion] = self

    def elegir_estudiantes(self):
        self.alumnos_semana = []
        if len(self.alumnos_quieren_reunion) > 10:
            while len(self.alumnos_semana) < 10:
                self.alumnos_semana.append(self.alumnos_quieren_reunion.pop(randint(0,len(self.alumnos_quieren_reunion) - 1)))
        else:
            self.alumnos_semana = self.alumnos_quieren_reunion


    def atender_alumnos(self):
        for alumno in self.alumnos_semana:
            alumno.reunion_profesor = True


# ----------------------------------------------------------------------------------------------------------------------

class Ayudante(Integrante):
    lista_ayudantes = []
    '''
    Esta clase representa a los ayudantes del curso.
    '''
    def __init__(self, nombre, rol, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        self.rol = rol
        Ayudante.lista_ayudantes.append(self)

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

posibles_personalidades = ['eficiente', 'artistico', 'teorico']




# ----------------------------------------------------------------------------------------------------------------------

