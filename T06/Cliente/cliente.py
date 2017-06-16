__author__ = 'Ricardo Del Río'

# Propios:
from loggers import MyLogger
# Networking:
from socket import gethostname, gethostbyname, AF_INET, SOCK_STREAM, socket
# Treading
from threading import Thread
# Serialización:
from pickle import dumps
# Otros
from datetime import datetime as dt
from os import listdir, getcwd, chdir, sep, mkdir
from time import sleep

# -------------------------------------------------------------------------------------------------------------- LOGGERS


log_i = MyLogger(__name__, name='SERVIDOR',
                 formatter='%(name)s[{0}]:   %(message)s'.format(__name__))
log_w = MyLogger(__name__, name='SERVIDOR',
                 nombre_archivo='servidor.log', stream_handler=False,
                 mylevel='warning')
log_e = MyLogger(__name__, name='SERVIDOR',
                 nombre_archivo='servidor.log', stream_handler=False,
                 mylevel='error')
log_d = MyLogger(__name__, name='SERVIDOR',
                 nombre_archivo='servidor.log', stream_handler=False,
                 mylevel='debug')
space = MyLogger(__name__, formatter='%(message)s')


HOST = gethostbyname(gethostname())
PORT = 8000
nombre_usuario = 'Ricardo'


class Cliente:
    def __init__(self, HOST, PORT, nombre_usuario):
        log_i.info('Inicializando cliente...')
        self.HOST = HOST
        self.PORT = PORT
        if len(nombre_usuario) > 20:
            raise ValueError('EL nombr de usuario no debe tener más de 20 caracteres')
        self.nombre_usuario = nombre_usuario
        self.funcionando = True
        self.socket = socket(AF_INET, SOCK_STREAM)

        # try:
        self.conectar_servidor()
        self.escucha()
        # except:
        #     log_i.info('Conexión terminada.')
        #     self.socket.close()
        #     exit()

    def conectar_servidor(self):
        self.socket.connect((self.HOST, self.PORT))
        primer_mensaje = (self.nombre_usuario+' '*(20-len(self.nombre_usuario))).encode('utf-8')
        self.socket.send(primer_mensaje)
        respuesta = self.socket.recv(1)
        int_respuesta = int.from_bytes(respuesta, byteorder='big')
        log_i.info('Mensaje del servidor: {}'.format(int_respuesta))
        if int_respuesta:
            log_i.info('Conexión establecida con el servidor.')
        else:
            log_i.info('No se pudo establecer conexión con el servidor, nombre de usuario ya esta siendo ocupado.')


    def thread_escucha(self):
        while self.funcionando:
            bytes_largo_respuesta = self.socket.recv(4)
            largo_respuesta = int.from_bytes(bytes_largo_respuesta, byteorder='big')
            respuesta = b''

            while len(respuesta) < largo_respuesta:
                respuesta += self.socket.recv(256)
            recibido = respuesta.decode('utf-8')
            if recibido != '':
                respuesta = self.manejo_de_comandos(recibido)

    def escucha(self):
        thread_escucha = Thread(target=self.thread_escucha)
        thread_escucha.start()

    def enviar_mensaje(self, msj):
        bytes_msj = msj.encode('utf-8')
        largo_msj = len(bytes_msj).to_bytes(4, byteorder='big')
        self.socket.send(largo_msj + bytes_msj)

# ------------------------------------------------------------------------------------------------------------- COMANDOS

class ProcesadorComandos:
    def __init__(self, servidor):
        self.servidor = servidor
        self.funcionando = True
        self.comandos = {'desconectar': [None, 'Desconecta al cliente del servidor.'],
                         'lista_comandos': [self.lista_comandos, 'Muestra los comandos validos.'],
                         'chat': [None,'Recibe un mensaje de chat y lo reeenvía a todos los usuarios']}
        self.recibir_comandos_consola()



    def __call__(self, comando):
        return self.procesar_comando(comando)

    def thread_recibir_comandos_consola(self):
        while self.funcionando:
            sleep(0.01)
            mensaje = self.procesar_comando(input('>>> '))
            log_i.info(mensaje)


    def recibir_comandos_consola(self):
        thread_comandos_consola = Thread(target=self.thread_recibir_comandos_consola,)
        thread_comandos_consola.start()

    def procesar_comando(self, comando):
        lista = comando.split(' ')
        if lista[0] in self.comandos:
            return self.comandos[lista[0]][0](*lista[1:])
        else:
            return 'Comando "{}" no existe'.format(lista[0])


    def lista_comandos(self):
        mensaje = '\n\n'
        for comando in self.comandos:
            mensaje += ('{0} {1}\n'.format(' '*22+comando, '.'*(20-len(comando))+' '+self.comandos[comando][1]))
        return mensaje




