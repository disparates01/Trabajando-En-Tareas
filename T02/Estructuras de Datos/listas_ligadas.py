# algoritmo basado en http://librosweb.es/libro/algoritmos_python/capitulo_16

class Nodo:

    def __init__(self, dato = None, prox = None):
        self.dato= dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)





class ListaLigada:

    def verLista(self):

