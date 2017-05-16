from contenidos import Contenido
from random import random

class Evaluacion:
    tipos = {1: 'actividad', 2: 'tarea', 3: 'control', 4: 'examen'}
    def __init__(self, tipo, PEP8, dia, contenido):
        self.tipo = tipo
        self.fecha = dia
        self.cont_a_evaluar = contenido
        # Aspectos a evaluar:
        self.PEP8 = PEP8
        self.contenidos = True
        self.funcionalidad = True
        self.exigencia = 7 + (random(1,5)/contenido.dificultad)

    @staticmethod
    def creacion_evaluaciones():
        # Creacion de actividades:
        fecha = 4
        for contenido in Contenido.lista_contenidos:
            Evaluacion(1, True, fecha, contenido)
            fecha += 7
        #Creacion de controles:
        fecha = 0


