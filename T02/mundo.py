__author__ = 'Ricardo Del Rio'

from manejo_csv import importar_datos

class Mundo:
    def __init__(self):
        self.propuestas = []
        self.grafo_terrestre = None
        self.grafo_aereo = None
        self.lista_paises = []

    def establecer_conecciones_terrestres(self):
        '''Crea un grafo de listas de adyacencia con las conexiones terrestres'''
        self.grafo_terrestre = {}  # OJO ESTO ESTA USANDO DICCIONARIO DE PYTHON
        for datos_fronteras_terrestres in importar_datos('borders.csv', ';'):
            if datos_fronteras_terrestres[0][:3] == 'ï»¿':
                datos_fronteras_terrestres[0] = datos_fronteras_terrestres[0][3:]
            if datos_fronteras_terrestres[0] == 'Pais 1':
                pass
            else:
                if datos_fronteras_terrestres[0] in self.grafo_terrestre:
                    self.grafo_terrestre[datos_fronteras_terrestres[0]].append(
                        datos_fronteras_terrestres[1])
                else:
                    self.grafo_terrestre[datos_fronteras_terrestres[0]] = [
                        datos_fronteras_terrestres[1]]  # OJO ESTO ESTA USANDO LISTAS DE PYTHON

    def establecer_conexiones_aereas(self):
        '''Crea un grafo de listas de adyacencia con las conexiones aereas'''
        self.grafo_aereo = {}  # OJO ESTO ESTA USANDO DICCIONARIO DE PYTHON
        for datos_fronteras_aereas in importar_datos('random_airports.csv'):
            if datos_fronteras_aereas[0][:3] == 'ï»¿':
                datos_fronteras_aereas[0] = datos_fronteras_aereas[0][3:]
            if datos_fronteras_aereas[0] == 'Pais 1':
                pass
            else:
                if datos_fronteras_aereas[0] in self.grafo_aereo:
                    self.grafo_aereo[datos_fronteras_aereas[0]].append(
                        datos_fronteras_aereas[1])
                else:
                    self.grafo_aereo[datos_fronteras_aereas[0]] = [
                        datos_fronteras_aereas[1]]

    def ordenar_propuestas(self):
        self.propuestas.sort()

    def estad_resumen_diario(self):
        ''' Imprime el resumen de estadisticas del dia anterior '''
        '''
        El dia de ayer...\n
        Se infectaron: {0} personas.\n
        Murieron: {1} personas.\n
        La infeccion llego a: {2}\n
        Se cerraron lo aeropuertos de: {3}\n
        Se cerraron las fronteras de: {4}\n
        Se entregaron mascarillas en: {5}\n
        '''
        pass

    def estad_por_pais:
        conteo = enumerate(self.lista_paises)
        for i,j in conteo:
            print('{0} {1:-20}'.format(i,j))


class Propuesta:
    def __init__(self, tipo, pais):
        self.tipo = tipo
        self.pais = pais #objeto pais
        self.prioridad = 0 #float

    def calcular_prioridad(self):
        pass

    def __le__(self, other):
        return self.prioridad <= other.prioridad


