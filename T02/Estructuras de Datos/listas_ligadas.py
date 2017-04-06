__author__ = 'Ricardo Del Río'

# Algoritmos basado en http://librosweb.es/libro/algoritmos_python/capitulo_16
# y material del curso Programación Avanzada de la Pontificia Universidad Catolica de Chile
# del 1er semestre del 2017.

class Nodo:

    def __init__(self, dato = None, prox = None):
        self.dato= dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class ListaLigada:
    def __init__(self):
        self.cola = None
        self.cabeza = None

    def append(self, valor):
        #Revisa si la lista tiene comienzo. Sino se crea un primer nodo.
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza

        #Si ya tiene comienzo:
        else:
            self.cola.prox = Nodo(valor)
            self.cola = self.cola.prox

class Diccionario:
    def __init__(self):
        self.llaves = []
        self.valores = []

    def __call__(self, llave, valor):
        #Si la llave esta en la lista de llaves:
        pos = self.llaves.index(llave)
        if pos != -1:
            return self.valor[pos]
        #Si no esta:
        else:
            self.llaves.append(llave)

if __name__ == '__main__':

    diccionario = Diccionario()
    diccionario.valores.append('chao')
    diccionario['hola'] #= 'chao'
    #¿Cómo hacer para poder usar los paréntesis de corchetes?



