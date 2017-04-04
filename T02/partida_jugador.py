from mundo import Mundo
from simplificadores import Menu

class Partida:
    def __init__(self):
        dia_actual = 0
        salir = False
        mundo = Mundo()

    def partida_nueva(self):
        '''Retorna True si la persona desea comenzar una nueva partida. False si desea una partida guardada'''
        pass

    def desplegar_menu_principal(self):
        Menu()
        pass

    def desplegar_menu_estadisticas(self):
        pass


    def pasar_dia(self):
        pass

    def guardar_estado(self):
        pass

    def salir(self):
        '''Retorna True'''
        self.salir = True