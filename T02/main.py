__author__ = 'Ricardo Del Rio'

from manejo_csv import importar_datos
from pais import Pais

paises = []

for datos_pais in importar_datos('population.csv'):
    if datos_pais[0] == 'Pais':
        pass
    else:
        nuevo_pais = Pais(*datos_pais)
        paises.append(nuevo_pais)


grafo_terrestre = {}
for datos_fronteras_terrestres in importar_datos('borders.csv'):
    if datos_fronteras_terrestres[0] == 'Pais 1':
        pass
    else:
        if grafo_terrestre[datos_fronteras_terrestres[0]] == None:
            grafo_terrestre[datos_fronteras_terrestres[0]] = [datos_fronteras_terrestres[1]]
        else:
            grafo_terrestre[datos_fronteras_terrestres[0]].append(datos_fronteras_terrestres[1])

for datos_fronteras_aereas in importar_datos('random_airport.csv'):
    if datos_fronteras_aereas[0] == 'Pais 1':
        pass
    else:
        pass


