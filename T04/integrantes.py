__author__ = 'Ricardo Del Rio'



# IDEAS
# Crear una lista que contenga todos los integrantes de la clase.
# La lista debe estar en la clase, no en la instancia de la clase.


posibles_personalidades = ['eficiente', 'artistico', 'teorico']

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
    def __init__(self, nombre, rol, seccion=None, personalidad=None):
        Integrante.__init__(self, nombre, rol, seccion)
        self.personalidad = personalidad

        Alumno.lista_alumnos.append(self)

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



