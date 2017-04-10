__author__ = 'Ricardo Del Rio'
#Libre de estructuras python

from random import randint, random
from estructuras_propias import Diccionario, ListaLigada


class Pais:
    def __init__(
            self,
            nombre,
            poblacion,
            infectados=0,
            muertos=0,
            fecha_infeccion=None,
            aeropuerto=True,
            frontera=True,
            mascarillas=False,
            fecha_cura=None,
            estado='limpio'):
        self.nombre = nombre
        self.poblacion = poblacion
        self.infectados = infectados
        self.muertos = muertos
        self.fecha_infeccion = fecha_infeccion
        self.aeropuerto = aeropuerto
        self.frontera = frontera
        self.mascarillas = mascarillas
        self.fecha_cura = fecha_cura
        self.estado = estado
        self.bitacora = Diccionario() #key = Numero de día ; valores = lista[infectados, muertos]

        self.propuestas_gobierno = []

    def avanzar_infeccion(self, infeccion, today):  ###ESta tiene que antes que avanzar muertes!!!!!
        nuevos_infectados = sum([randint(0, 6) for persona in range(
            1, 100)]) * infeccion.contagiosidad  # ESTO USA UNA LISTA PYTHON
        self.bitacora[today] = ListaLigada(nuevos_infectados)
        if self.mascarillas:
            nuevos_infectados *= 0.3
        self.infectados += nuevos_infectados
        return self.infectados

    def avanzar_muertes(self, today):
        nuevos_muertos = self.probabilidad_de_muerte * self.infectados
        self.bitacora[today].append(nuevos_muertos)
        self.muertos += nuevos_muertos
        return self.muertos

    def avanzar_contagio(self, today):
        if not self.infectado():
            return
        else:
            for pais in set(  # ESTO USA UN CONJUNTO PYTHON
                self.vecinos(
                    lista_paises,
                    grafo_terrestre) +
                self.vecinos(
                    lista_paises,
                    grafo_aereo)):
                min((0.07 * self.infectados) / (self.poblacion *
                                                self.conecciones(grafo_terrestre, grafo_aereo, pais)), 1)
        if random() > min((0.07 * self.infectados) / (self.poblacion *
                                                             self.conecciones(grafo_terrestre, grafo_aereo, pais)), 1):
            pais.infectar(today)

    def avanzar_cura(self, today):
        if not self.curado:
            return
        else:
            paises_curados = []
            for pais in self.vecinos(lista_paises, grafo_aereo):
                pais.curar(today)
                paises_curados.append(pais)
        return paises_curados

    def aplicar_cura(self, infeccion):
        if self.curado:
            self.infectados *= 0.25 * infeccion.resistencia
        return self.infectados

    def curado(self):
        return bool(self.fecha_cura)

    def muerto(self):
        return self.muertos == self.poblacion

    def infectado(self):
        return bool(self.fecha_infeccion)

    def curar(self, today):
        self.fecha_cura = today
        return self.fecha_cura

    def infectar(self, today):
        self.fecha_infeccion = today
        return self.fecha_infeccion

    def days_infected(self, today):  # cambiar nombre a dias_infeccion
        return today - self.fecha_infeccion

    def conecciones(self, grafo_terrestre, grafo_aereo, pais2):
        conecciones = 0
        if pais2 in self.vecinos(grafo_terrestre):
            if self.frontera and pais2.frontera:
                conecciones += 1
        if pais2 in self.vecinos(grafo_aereo):
            if self.aeropuerto and pais2.aeropuerto:
                conecciones += 1
        return conecciones

    def probabilidad_de_muerte(self, infection):
        return min(min(0.2, (self.days_infected *
                             self.days_infected /
                             100000)) *
                   infection.tasa_mortalidad, 1)

    def probabilidad_de_contagio(self):
        return min((0.07 * self.infectados / (self.poblacion * self.conecciones)), 1)

    def sanos(self):
        return self.poblacion - self.infectados

    def porcentaje_infectados(self):
        return (self.infectados / self.poblacion) * 100

    def vecinos(self, lista_paises, grafo):
        nombres_vecinos = grafo[self.nombre]
        return [pais for pais in lista_paises if pais.nombre in nombres_vecinos]  ###LISTA PYTHON!!!!

    def anadir_propuestas(self):
        propuestas = []
        return propuestas

    def mostrar_estadisticas(self):
        #Al probar el programa ver cuanto espacio usan mas o menos los numeros,
        #Para verificar la alineacion a la derecha
        print('PAIS: {0}\n'
              'Estadistcas:\n'
              '\tPersonas vivas:      {1:11}\n'
              '\tPersonas infectadas: {2:11}\n'
              '\tPersonas muertas:    {3:11}\n\n'
              'Propuestas del Gobierno:\n'
              '\t{}'.format(self.nombre,
                            self.poblacion - self.muertos,
                            self.infectados,
                            self.muertos,
                            '\n'.join(self.propuestas_gobierno.sort())))

    def abrir_aeropuerto(self):
        pass

    def cerrar_aeropuerto(self):
        pass

    def abrir_frontera(self):
        pass

    def cerrar_frontera(self):
        pass

    def repartir_mascarillas(self):
        pass

    def generar_estadisticas(self):
        return estadisticas
