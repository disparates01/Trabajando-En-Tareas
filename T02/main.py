__author__ = 'Ricardo Del Rio'

from manejo_csv import importar_datos
from pais import Pais
from simplificadores import Menu


def cargar_datos():
    #Crea objetos de la clase Pais con cada linea del archivo "populatio.csv" y los almacena en una lista.
    global paises = []
    for datos_pais in importar_datos('population.csv'):
        if datos_pais[0] == 'Pais':
            pass
        else:
            nuevo_pais = Pais(*datos_pais)
            paises.append(nuevo_pais)

    #Crea un grafo de listas de listas de adyacencia con las conexiones terrestres
    global grafo_terrestre = {}
    for datos_fronteras_terrestres in importar_datos('borders.csv'):
        if datos_fronteras_terrestres[0] == 'Pais 1':
            pass
        else:
            if grafo_terrestre[datos_fronteras_terrestres[0]] == None:
                grafo_terrestre[datos_fronteras_terrestres[0]] = [datos_fronteras_terrestres[1]]
            else:
                grafo_terrestre[datos_fronteras_terrestres[0]].append(datos_fronteras_terrestres[1])

    # Crea un grafo de listas de listas de adyacencia con las conexiones aereas
    global grafo_aereo = {}
    for datos_fronteras_aereas in importar_datos('random_airport.csv'):
        if datos_fronteras_aereas[0] == 'Pais 1':
            pass
        else:
            if grafo_aereo[datos_fronteras_aereas[0]] == None:
                grafo_aereo[datos_fronteras_aereas[0]] = [datos_fronteras_aereas[1]]
            else:
                grafo_aereo[datos_fronteras_aereas[0]].append(datos_fronteras_aereas[1])

hay_guardada = True
try:
    with open('partida_guardada.csv', 'r') as archivo:
        pass
except:
    hay_guardada = False

if not hay_guardada:
    lista1 = ['Comenzar Nueva Partida', 'Comenzar Partida Guardada']
    lista2 = [] #completar esta lista.
    Menu()(lista1, lista2)

