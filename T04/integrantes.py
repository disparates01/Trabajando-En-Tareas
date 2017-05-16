__author__ = 'Ricardo Del Rio'

from random import choice, random, randint, uniform, triangular
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
        # Parametros que se modifican constantemente:
        # Se comienza asignandoles un primer valor que luego sera modificado.
        self.__horas_estudio = 0 # Horas que el estudiante dedicara al curso en una semana. Se modifica semana a semana.
        self.__confianza = [None,0] # [Valor, ultimo evento que la modifico]
        self.__manejo_de_contenidos = 0
        self.__nivel_de_programacion = randint(2,10) #Se calcula semanalmente
        self.__nota_esperada = 0

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

        @property
        def manejo_contenidos(self):
            return self.__manejo_de_contenidos

        @property
        def nivel_programacion(self):
            return self.__nivel_de_programacion

        @property
        def nota_esperada(self):
            return self.__nota_esperada

        @property
        def horas_estudio(self):
            return self.__horas_estudio

        @property
        def progreso_act_actual(self):
            __PEP8 = (0.7*manejo_contenidos) + (0.2*nivel_programacion) + (0.1*confianza)
            __funcionalidad = (0.3*manejo_contenidos) + (0.7*nivel_programacion) + (0.1*confianza)
            __contenidos = (0.7*manejo_contenidos) + (0.2*nivel_programacion) + (0.1*confianza)
            return (0.2*__PEP8) + (0.4*__funcionalidad) + (0.4*__contenidos)
        
        @property
        def progreso_tarea_actual(self):
            __horas = horas_estudio * 0.7
            __PEP8 = (0.5*__horas) + (0.2*nivel_programacion)
            __contenido = (0.7*manejo_contenidos) + (0.1*nivel_programacion) + (0.2*__horas)
            __funcionalidad = (0.5*manejo_contenidos) + (0.1*nivel_programacion) + (0.4*__horas)
            return (0.2*__PEP8) + (0.4*__contenido) + (0.4*__funcionalidad)

        @property
        def progreso_control_actual(self):
            __contenidos = (0.7*manejo_contenidos) + (0.05*nivel_programacion) + (0.25*confianza)
            __funcionalidad = (0.3*manejo_contenidos) + (0.2*nivel_programacion) + (0.5*confianza)
            return (0.7*__contenidos) + (0.3*__funcionalidad)

        @property
        def progreso_examen(self):
            # revisar: falta implementar, recordar que el rpogreso es por pregunta.
            __contenidos = 0
            __funcionalidad = 0
            return (0.7*__contenidos) + (0.3*__funcionalidad)

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

    def duda_catedra(self):
        '''
        Este metodo selecciona a uno de los tres ayudantes de la seccion que estan en la catedra.
        Si el ayudante ya resolvio 200 dudas, seleccionara al siguiente y así hasta haber seleccionado a los 3 o haber
        resuelto la duda.
        Si un ayudante resuelve una duda, el manejo de contenidos del estudiante aumenta un 1%
        :return:
        '''
        resuelto = False
        n = 1
        while n <= 3 and not resuelto:
            ayudante = AyudanteDocencia.ayudantes_secciones[self.seccion][n]
            try:
                ayudante.resolver_dudas()
                self.__manejo_de_contenidos *= 1.1  # Aumenta el manejo de contenidos en un 1%
                resuelto = True
            except:
                pass
            n += 1

    def catedra(self):
        '''
        Este metodo define cuantas veces el estudiante pedirá ayuda durante la catedra.
        Llama a la función que hace que el estudiante resuelva sus dudas la cantidad de veces que se establecen.
        :return:
        '''
        solicitud_de_ayuda = triangular(1,10,3)
        for i in range (solicitud_de_ayuda):
            self.duda_catedra()




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

class AyudanteTarea(Integrante):
    '''
    Esta clase representa a los ayudantes de tareas del curso.
    '''
    ayudantes_tareas = []
    def __init__(self, nombre, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        AyudanteTarea.ayudantes_tareas.append(self)


class AyudanteDocencia(Integrante):
    '''
    Esta clase representa a los ayudantes de docencia del curso.
    '''
    ayudantes_docencia = []
    ayudantia = []
    ayudantes_secciones = {}
    def __init__(self, nombre, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        AyudanteDocencia.ayudantes_docencia.append(self)
        self.__ayudados = 0
        self.__dudas_resueltas = 0
        self.contenidos_destacados = []

    @staticmethod
    def quien_hara_ayudantia():
        '''Este metodo selecciona a los ayudantesque haran la ayudantía de la semana'''
        # Se limpia la lista
        AyudanteDocencia.ayudantia = []
        # Se selecciona al primer ayudante
        AyudanteDocencia.ayudantia.append(choice(AyudanteDocencia.ayudantes_docencia))
        # Se selecciona al segundo:
        stop = False
        while not stop:
            ayudante = choice(AyudanteDocencia.ayudantes_docencia)
            if ayudante not in AyudanteDocencia.ayudantia:
                AyudanteDocencia.ayudantia.append(ayudante)
                stop = True

    @staticmethod
    def ayudantes_por_seccion():
        '''Este metodo selecciona a los ayudantes que iran a cada seccion de la catedra'''
        seleccionados = []
        AyudanteDocencia.ayudantes_secciones.clear()
        AyudanteDocencia.ayudantes_secciones[1] = []
        AyudanteDocencia.ayudantes_secciones[2] = []
        AyudanteDocencia.ayudantes_secciones[3] = []
        while len(seleccionados) < 9:
            ayudante = choice(AyudanteDocencia.ayudantes_docencia)
            if not ayudante in seleccionados:
                seleccionados.append(ayudante)
        for i in range(3):
           AyudanteDocencia.ayudantes_secciones[1].append(seleccionados.pop())
           AyudanteDocencia.ayudantes_secciones[2].append(seleccionados.pop())
           AyudanteDocencia.ayudantes_secciones[3].append(seleccionados.pop())

    @property
    def dudas_resueltas(self):
        '''
        Esta property representa la cantidad de veces que el ayudante ha resueto dudas.
        :return:
        '''
        return self.__dudas_resueltas


    def resolver_dudas(self):
        '''
        Se evita que el ayudante resuelva más dudas que el maximo permitido.
        :return:
        '''
        if self.__dudas_resueltas < 200:
            self.__dudas_resueltas += 1
        else:
            raise ValueError('Se han resuelto el máximo de dudas')

    def selec_contenidos_destacados(self):
        '''
        Se seleccionan los 3 contenidos que el ayudante domina mejor.
        :return:
        '''
        while len(self.contenidos_destacados) < 3:
            contenido = choice(Contenido.lista_contenidos)
            if contenido in self.contenidos_destacados:
                pass
            else:
                self.contenidos_destacados.append(contenido)


class Coordinador(Integrante):
    '''
    Esta clase representa al ayudante coordinador del curso.
    '''
    coordinador = None
    def __init__(self, nombre, seccion=None):
        Integrante.__init__(self, nombre, seccion)
        self.c_descuentos = 0
        self.fecha_ultimo_descuento = None
        Coordinador.coordinador = self

    @property
    def atrasar_notas(self):
        num = random()
        if num <= 0.1:
            return True
        return False

    @property
    def descontar_notas(self):
        # revisar: No debe hacerse en la última evaluación.
        if self.c_descuentos == 3:
            return False
        # Debe revisar que no vuelva a pasar en menos de un mes (revisar)
        # if self.fecha_ultimo_descuento - fecha_actual > 1 mes:
        #     pass
        num = random()
        if num <= 0.5:
            self.c_descuentos += 1
            return True
        return False


# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

posibles_personalidades = ['eficiente', 'artistico', 'teorico']




# ----------------------------------------------------------------------------------------------------------------------

