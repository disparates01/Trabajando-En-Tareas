__author__ = 'Ricardo Del Río'

from sys import getsizeof

# Algoritmos basado en http://librosweb.es/libro/algoritmos_python/capitulo_16
# y material del curso Programación Avanzada de la Pontificia Universidad Catolica de Chile del 1er semestre del 2017.

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
        # len = 0

    def append(self, valor):
        #Revisa si la lista tiene comienzo. Sino se crea un primer nodo.
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza

        #Si ya tiene comienzo:
        else:
            self.cola.prox = Nodo(valor)
            self.cola = self.cola.prox

    def pop(self, posicion = None):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def insert(self,posicion, elemento):
        pass

    def remove(self, elemento):
        pass

    def index(self):
        pass

#--------------------------------------------------DICCIONARIO-------------------------------

class Diccionario:
    def __init__(self):
        self.llaves = []
        self.valores = []

    def __getitem__(self, llave):
        '''Permite ingresar una llave en parentesis de corchete. Ej: diccionario['llave'] '''

        #Si la llave esta en la lista de llaves:
        if llave in self.llaves:
            return self.valores[self.llaves.index(llave)]
        #Si no esta:
        else:
            raise KeyError('La llave entregada no pertenece al diccionario')

    def __setitem__(self, llave, valor):
        '''Permite asignar un valor a la llave. Ej: diccionario[llave] = valor'''
        # Si la llave esta en la lista de llaves:
        try:
            pos = self.llaves.index(llave)
            self.valores[pos] = valor
        # Si no esta:
        except:
            self.llaves.append(llave)
            self.valores.append(valor)

    def __contains__(self, llave):
        return llave in self.llaves

    def __delitem__(self, llave):
        pos = self.llaves[llave]
        del self.llaves[pos]
        del self.valores[pos]

    def __eq__(self, other):
        return self.llaves == other.llaves and self.valores == other.valores

    '''
    def __ge__(self, other):
        pass
    def __getattribute__(self, item):
        pass
    '''

    def __gt__(self, other):
        return len(self.llaves) > len(other.llaves)

    '''
    def __iter__(self, /):
        pass
    '''

    def __le__(self, other):
        pass

    def __len__(self):
        return len(self.llaves)

    def __lt__(self, other):
        pass

    def __ne__(self, other):
        pass

    '''
    def __new__(cls, *args, **kwargs):
        pass
    '''

    def __repr__(self):
        texto_dic = '{'
        for i in range(len(self.llaves)):
            texto_dic += '{0}: {1} , '.format(self.llaves[i], self.valores[i])
        texto_dic += '}'
        return repr(texto_dic)

    '''
    def __sizeof__(self):
        pass
    '''
    def clear(self):
        self.llaves.clear()
        self.valores.clear()

    def copy(self):
        return self

    def fromkeys(self):
        pass
    def get(self):
        pass
    def items(self):
        pass
    def keys(self):
        pass

    def pop(self, pos):
        pass #esta es importante, completar


#----------------------------------------------------EJECUCION_____________________________

if __name__ == '__main__':

    diccionario = Diccionario()
    diccionario['hola'] = 'chao'
    print(diccionario['hola'])
    diccionario['hola'] = 'hola'
    print(diccionario['hola'])
    diccionario['hello'] = 'hello'
    print(diccionario['hello'])

    dict2 = diccionario
    print(str(diccionario == dict2))
    print(diccionario)
    dict3 = diccionario.copy()
    print(dict3)

    #¿Cómo hacer para poder usar los paréntesis de corchetes?



