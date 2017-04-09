__author__ = 'Ricardo Del Rio'

#from calendario import Calendario
from estructuras_propias

'''
Este modulo contiene funciones para facilitar y acelerar aquellas tediosas y repetitivas partes
de la programacion para dejar mas tiempo a las partes entrenenidas
'''

#-----------------------------------------------------------------------------------------------------------------------

#Idea:
#Hacer que el super input no retorne solo un str, sino que el tipo que se pidió.-

class SuperInput:
    solicitud_input = ''
    lista = []
    mensaje_error = ''
    entrada = ''

    def __init__(self, solicitud_input = '>>> ', tipos = 'str', mensaje_error = None):
        self.solicitud_input = solicitud_input
        if type(tipos) == str:
            self.lista = [tipos]
        elif type(tipos) == list:
            self.lista = tipos
        self.mensaje_error = mensaje_error
        self.entrada = ''




    def solicitar_entrada(self):
        self.entrada = input()

    def es_str(self, tipo):
        texto = ['str', 'string', 'texto']
        if tipo in texto:
            return True
        return False

    def es_int(self, tipo):
        entero = ['int', 'integer', 'entero', 'numero']
        if tipo in entero:
            return True
        return False

    def es_float(self, tipo):
        decimal = ['float', 'decimal']
        if tipo in decimal:
            return True
        return False

    def es_mail(self, tipo):
        email = ['email', 'mail', 'correo electronico']
        if tipo in email:
            return True
        return False

    def input_correcto(self):
        '''
        Revisa si el parametro ingresado en el superinput (self.entrada) es de alguno de los tipos permitidos en
        self.lista
        Si lo es, retorna True. Si no, False.
        '''
        v1, v2, v3, v4, v5, v6 = False, False, False, False, False, False
        for tipo in self.lista:
            if self.es_int(tipo):
                try:
                    self.entrada = int(self.entrada)
                    v1 = True
                except:
                    v1 = False
            elif self.es_float(tipo):
                try:
                    self.entrada = float(self.entrada)
                    v2 = True
                except:
                    v2 = False
            elif self.es_mail(tipo):
                print('Aún no está creada la opcion mail del superinput')
                v3 = False
            elif self.es_str(tipo):
                v4 = True
            elif i == 'fecha':
                v5 = True
                for l in self.entrada:
                    if not (l.isnumeric() or l == '/'):
                        v5 = False

                if (not self.mensaje_error) and (not v5):
                    self.mensaje_error = 'Formato de fecha incorrecto, ingresar de nuevo.'

                if v5:
                    dia = self.entrada[:self.entrada.find('/')]
                    fecha = self.entrada[self.entrada.find('/') + 1:]
                    mes = fecha[:fecha.find('/')]
                    fecha = fecha[fecha.find('/') + 1:]
                    ano = fecha
                    c = Calendario()
                    if not c.fecha_valida(dia, mes, ano):
                        v5 = False
                        if not self.mensaje_error:
                            self.mensaje_error = 'Fecha no válida, ingresar otra fecha.'

            elif i == 'hora':
                v6 = True
                if len(self.entrada) != 8:
                    v6 = False
                if v6:
                    for l in self.entrada:
                        if not (l.isnumeric() or l == ':'):
                            v6 = False
                if not self.mensaje_error and not v6:
                    self.mensaje_error = 'Formato de hora incorrecto, ingresar de nuevo.'
                if v6:
                    if self.entrada[0] == 0:
                        horas = int(self.entrada[1])
                    else:
                        horas = int(self.entrada[:2])
                    if self.entrada[3] == 0:
                        minutos = int(self.entrada[4])
                    else:
                        minutos = int(self.entrada[3:5])
                    if self.entrada[6] == 0:
                        segundos = int(self.entrada[7])
                    else:
                        segundos = int(self.entrada[6:])

                    if not(horas >= 0 and horas <= 23):
                        v6 = False
                    if not(minutos >= 0 and minutos <= 59):
                        v6 = False
                    if not(segundos >= 0 and segundos <= 59):
                        v6 = False

                if not v6 and not self.mensaje_error:
                        self.mensaje_error = 'Hora no válida, ingresar otra hora.'

                '''
                    Este segmento esta encaminado para que el programa acepte horas no solo del formato hh:mm:ss, sino que
                    también horas con el formato hh:mm o simplemente hh, supondiendo que todo lo demás es 0.
                    Terminar más adelante.
                    Hay partes que se deben usar del algoritmo actualmente funcional del programa (que acepta solo hh:mm:ss)


                    if v6:
                        hora = ''
                        if self.entrada.find(':') != -1:
                            horas = self.entrada[:self.entrada.find(':')]
                            hora = self.entrada[self.entrada.find(':') + 1:]
                        else:
                            horas = self.entrada

                        if hora.find(':') != -1:
                            minutos = hora[:hora.find(':')]
                            hora = hora[hora.find(':') + 1:]
                        else:
                            minutos = hora

                        if minutos != hora:
                            segundos = hora
                '''

        return (v1 or v2 or v3 or v4 or v5 or v6)

    def __new__(self, solicitud_input = '>>> ', tipos = 'str', mensaje_error = None):
        self.solicitud_input = solicitud_input
        if type(tipos) == str:
            self.lista = [tipos]
        elif type(tipos) == list:
            self.lista = tipos
        self.mensaje_error = mensaje_error
        self.entrada = ''

        stop = False
        while not stop:
            self.solicitar_entrada()
            if self.input_correcto():
                stop = True
                return self.entrada
            else:
                print(self.mensaje_error)
                print()




#-----------------------------------------------------------------------------------------------------------------------

class Error:
    pass

class Menu():
    '''def __init__(self, lista_opciones, lista_funciones = None, texto_inicio = None, texto_error = None):
        self.lista_opciones = lista_opciones
        self.lista_funciones = lista_funciones
        self.texto_inicio = texto_inicio
        self.texto_error = texto_error'''

    def __new__(self, lista_opciones, lista_funciones = None, texto_inicio = None, texto_error = None):
        self.lista_opciones = lista_opciones
        self.lista_funciones = lista_funciones
        self.texto_inicio = texto_inicio
        self.texto_error = texto_error
        '''
        Recibe una lista de opciones que el programa enumera y presenta al usuario.
        Si se le entrega una lista de funciones, estas seran asociadas en el orden entregado a la lista de opciones,
        de modo que cuando un usuario selecciona una opcion automaticamente comienza la funcion asociada.
        Si no se entrega lista de funciones el programa retorna la opcion seleccionada por el usuario.
        El programa es sensible a los errores de los usuarios, solamente admite enteros en el rango de la cantidad de
        opciones disponibles. El programa vuelve a solicitar la información correcta cada vez que el usuario ingresa una
        opcion invalida
        '''
        diccionario = {}
        stop = False
        while not stop:
            #Revisa que los argumentos enregados sean realmente listas:
            if isinstance(self.lista_opciones, list):
                if isinstance(self.lista_funciones, list):
                    #Revisa que ambas listas tengan el mismo largo:
                    if len(self.lista_funciones) == len(self.lista_opciones):
                        #Crea un diccionario con un numero y la funcion asociada:
                        contador = 0
                        for funcion in self.lista_funciones:
                            contador += 1
                            diccionario[contador] = funcion
                        #Despliga en pantalla las opciones diponibles:
                        contador = 0
                        if self.texto_inicio:
                            if type(self.texto_inicio) == str:
                                print(self.texto_inicio + '\n')
                            else:
                                raise TypeError('El texto de inicio debe ser un "string" no "{}"'.format(type(self.texto_inicio)))
                        for opcion in self.lista_opciones:
                            contador += 1
                            print('{}) {}'.format(contador, opcion))
                        #Solicita la opcion que el usuario desea seleccionar y ejecuta la funcion:
                        entrada = int(SuperInput('>>> Elige una opcion: ', 'int'))
                        if (entrada > 0) and (entrada <= contador):
                            stop = True
                            diccionario[entrada]()
                        else:
                            if self.texto_error:
                                if type(self.texto_error) == str:
                                    print(self.texto_error + '\n')
                                else:
                                    raise TypeError('El texto de error debe ser un "string"no "{}"'.format(type(self.texto_inicio)))
                    else:
                        raise IndexError('Ambas listas deben tener el mismo largo.')
                else:
                    raise TypeError('Se entrega "{}" cuando se pide una "list"'.format(type(self.lista_funciones)))
            else:
                raise TypeError('Se entrega "{}" cuando se pide una "list"'.format(type(self.lista_opciones)))



#-----------------------------------------------------------------------------------------------------------------------

def repetir(lista_funciones, condicion = False):
    '''
    La funcion recibe una lista de funciones o una funcion que se repetirá hasta q se cumpla la condicion determinada
    '''
    #Probablemente una buena forma de estructurarla es de manera recursiva. La condicion deberia ser una funcion que
    #retorne un bool que se llame constantemente hasta que algo modifique su valor de verdad y haga q el pograma se
    #detenga

#def superinput(solicitud_input = '>>> ', tipos = 'str', mensaje_error = None):
    '''
    En el parametro "tipo" la uncion puede recibir un string o una lista en la que se especifiquen todos los tipos
    validos de imput que el usuario puede hacer
    Bilingue: ES/EN
    '''
'''
    stop = False
    while not stop:

        entrada = input(solicitud_input)

        if type(tipos) == str:
            temp = tipos
            tipos = [temp]


        for i in tipos:
            if es_str(i):
                pass



            if es_str(tipos):
                entrada = str(entrada)

            elif tipos in entero:
                try:
                    entrada = int(entrada)
                    stop = True
                except:
                    if not mensaje_error:
                        mensaje_error = 'Solo puedes ingresar numeros enteros. Por favor ingresa un parametro valido.'
                    print(mensaje_error + '\n')

            elif tipos in decimal:
                try:
                    entrada = foat(entrada)
                    stop = True
                except:
                    if not mensaje_error:
                        mensaje_error = 'No ingresaste un numero. Por favor ingresa un parametro valido.'
                    print(mensaje_error)

            elif tipos in email:


                correcto = False

                if '@' in entrada:
                    pos = entrada.find('@')
                    revisa



                if correcto == False:
                    if not mensaje_error:
                        mensaje_error = 'No ingresaste un email correcto. Favor ingresa un parametro valido'
                    print(mensaje_error)


    return entrada
'''

def credenciales_usuarios(tupla_usuarios, tupla_contraseñas = None, intentos = None):
    '''
    Recibe:
    1) Una tupla de usuarios y una de contraseñas q están en el orden respectivo
    o
    2) Un diccionario con los usuarios y su respectiva contraseña asociada
        (Si la funcion no recibe una tupla de contraseñas, asume que recibio un diccionario)                            ******
    Se solicita al usuario que ingrese su nombre de usuario y su contraseña.
    Si esta correcto la funcion retorna True. De lo contrario False.
    En caso de un error el programa vuelve a solicitar las credenciales indefinidamente a no ser que se entregue un
    maximo de intentos
    '''
    #En el caso de que se entregue una cantidad de intentos el programa debería almacenar en un archivo en el que se
    #indique la fecha/hora en que se superaron los intentos de modo que cuando vuelva a iniciarse el rpograma
    #este pueda calcular si ha transcurrido el tiempo sufucuente para que determinado usuario vuelva a intentar
    #ingresar

def ordenar():
    '''
    recibe una lista o una matriz y el espacio que se le quiere asignar a cada elemento (todos igual, en el futuro
    evaluar que permita poner distinto largo a cada columna)
    no retorna un string con los datos de la matriz o lista de forma ordenada, listos para imprimir en pantalla
    '''

if __name__ == '__main__':

    def hola():
        print('hola')

    def chao():
        print('chao')

    lista1 = ['Imprimir Hola', 'Imprimir Chao']
    lista2 = [hola, chao]

    m = Menu(lista1, lista2)
