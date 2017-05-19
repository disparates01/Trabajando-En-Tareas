__author__ = 'Rcardo Del Rio'

from integrantes import Alumno, Profesor, AyudanteDocencia, AyudanteTarea, Coordinador
from evento import Evento
from contenidos import Contenido

'''
COMENTARIOS
Archivos de datos = '.dsap' (Datos Simulacion Avanzacion Programada)
'''

class Simulacion:
    '''
    Esta clase es la encargada de llevar todos los procesos de la simulación.
    Lleva la linea temporal de está y ejecuta en orden los eventos correspondientes.
    '''
    def cargar_integrantes(self):
        '''
        Este método lee el archivo 'integrantes.csv' y crea un objeto de cada integrante en su clase correspondiente,
        el cual es almacenado en una lista de la clase (no de la instancia)
        '''
        with open('integrantes.csv', encoding='utf-8') as archivo:
            # Carga los alumnos
            alumnos = (filter(lambda x: x[1] == 'Alumno' ,(integrante.strip().split(',') for integrante in archivo)))
            for alumno in alumnos:
                Alumno(alumno[0], alumno[2])
            # Vuelve a la posicion inicial
            archivo.seek(0)
            # Carga los profesores
            profesores = (filter(lambda x: x[1] == 'Profesor' ,(integrante.strip().split(',') for integrante in archivo)))
            for profesor in profesores:
                Profesor(profesor[0], profesor[2])
            # Vuelve a la posicion inicial
            archivo.seek(0)
            # Carga los ayudantes
            ayudantes = (filter(lambda x: ((x[1] == 'Coordinación') or (x[1] == 'Docencia') or (x[1] == 'Tareas')),
                                (integrante.strip().split(',') for integrante in archivo)))
            for ayudante in ayudantes:
                if ayudante[1] == 'Coordinación':
                    Coordinador(ayudante[0], ayudante[2])
                elif ayudante[1] == 'Docencia':
                    AyudanteDocencia(ayudante[0], ayudante[2])
                elif ayudante[1] == 'Tareas':
                    AyudanteTarea(ayudante[0], ayudante[2])


    def run(self):
        self.cargar_integrantes()
        Contenido.importar_info_contenidos()
        Evento.creacion_eventos_principales()
        while Evento.lista_eventos:
            Evento.seleccionar_evento()
            Evento.ejecutar_evento()


if __name__ == '__main__':
    s = Simulacion()
    s.run()


    # c_alumnos = len(Alumno.lista_alumnos)
    # c_profesores = len(Profesor.lista_profesores)
    # c_audantes = len(Ayudante.lista_ayudantes)
    # c_TOTAL = c_alumnos + c_profesores + c_audantes
    #
    # print('{0:5} alumnos \n{1:5} profesores \n{2:5} ayudantes \n{3:5} TOTAL'.format(c_alumnos, c_profesores, c_audantes, c_TOTAL))

