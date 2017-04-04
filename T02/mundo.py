
class Mundo:
    def __init__(self, conexiones_paises):
        conexiones_terrestres_paises = conexiones_paises #lista
        self.propuestas = []
        self.grafo_conexiones_terrestres = None
        self.grafo_conexiones_aereas = None

    def establecer_conecciones_terrestres(self):
        pass

    def establecer_conexiones_aereas(self):
        pass

    def ordenar_propuestas(self):
        self.propuestas.sort()

    def generar_estadisticas(self):
        pass

class Propuesta:
    def __init__(self, tipo, pais):
        self.tipo = tipo
        self.pais = pais #objeto pais
        self.prioridad = 0 #float

    def calcular_prioridad(self):
        pass

    def __le__(self, other):
        return self.prioridad <= other.prioridad


