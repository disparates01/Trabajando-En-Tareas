
class Objeto():

    def __init__(self):
        hola = 'hola'

    def __getattr__(self, item):
        pass


class Fruit(object):
    def __init__(self):
        self.Fruits = {"Apple": 0, "Pear": 1, "Banana": 2}

    def __getitem__(self, item):
        return self.Fruits[item]

'''class Fruit(object):
    __metaclass__ = GetAttr

    Apple = 0
    Pear = 1
    Banana = 2'''

if __name__ == '__main__':
    print(Fruit['Apple'], Fruit['Banana'])