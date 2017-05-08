__author__ = 'Ricardo Del Río'

from datetime import datetime as dt

def tiempo_ejecucion(funcion):
    def nueva_funcion(*args):
        inicio = dt.now()
        funcion(*args)
        fin = dt.now()
        tiempo = fin - inicio
        with open('mediciones.txt', 'a', encoding='utf-8') as archivo:
            archivo.write('{0} '
                          '\n Fecha/Hora:          {1}'
                          '\n Tiempo de ejecución: {2}'.format(funcion, inicio, tiempo))
            archivo.write('\n\n')
        return funcion(*args)
    return nueva_funcion



if __name__ == '__main__':

    @tiempo_ejecucion
    def contar_hasta(numero):
        with open('contador.txt', 'w', encoding='utf-8') as archivo:
            for i in range(numero):
                archivo.write('Estoy contando el número: {0} \n'.format(i))
            archivo.write('\n Terminé de contar')
        return 'Conté hasta {}'.format(numero)

    func1 = contar_hasta(100000)
    func2 = contar_hasta(1000000)
    func3 = contar_hasta(10000000)
    print(func1, func2, func3)