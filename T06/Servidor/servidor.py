# 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
__author__ = 'Ricardo Del Río'

# -------------------------------------------------------------------------------------------------------------- IMPORTS

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


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   AQUI SE SE DEFINEN EL HOST Y EL PORT   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
HOST = gethostbyname(gethostname())
PORT = 8000
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# ------------------------------------------------------------------------------------------------------------- SERVIDOR

class Servidor:
    def __init__(self, HOST, PORT):
        space.info('')
        log_i.info('Iniciando servidor...')
        space.info('')
        self.HOST = HOST
        self.PORT = PORT
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.funcionando = True
        # Ejecución de funciones:
        self.bind_and_listen()
        self.aceptar_conexiones()


        # self.ubicacion = getcwd()
        # self.ubic_canciones = self.ubicacion + sep + 'Canciones'
        # # Si no existe la carpeta se crea:
        # if not 'Canciones' in listdir():
        #     mkdir('Canciones')

        log_i.info('HOST:       {}'.format(self.HOST))
        log_i.info('PORT:       {}'.format(self.PORT))
        log_i.info('UBICACIÓN:  {}'.format(getcwd()))
        space.info('')
        log_i.info('Servidor iniciado: {}'.format(dt.now()))
        log_i.info('Escuchando ...')
        space.info('')
        space.info('-'*100)
        space.info('')

    def bind_and_listen(self):
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen(10)

    def enviar_mensaje(self, valor, socket):
        valor_str = str(valor)
        msj_bytes = valor_str.encode('utf-8')
        tipo_bytes = 'msj'.encode('utf-8')
        largo_msj = (len(msj_bytes) + 3).to_bytes(4, byteorder='big')
        socket.send(largo_msj + tipo_bytes + msj_bytes)

    def enviar_archivo(self, tipo, path, socket, reprodccion=0):
        if tipo == 'wav':
            with open(path, 'rb') as archivo:
                bytes_archivo = archivo.read()
                tamano = len(bytes_archivo) + 5 # 3 bytes del tipo y 2 del segundo de reproducción
                bytes_tamano = tamano.to_bytes(4, byteorder='big')
                bytes_tipo = tipo.encode('utf-8')
                bytes_reproduccion = reprodccion.to_bytes(2, byteorder='big')
                socket.send(bytes_tamano + bytes_tipo + bytes_reproduccion + bytes_archivo)



    def thread_escuchar_cliente(self, socket_cliente):
        while self.funcionando:
            bytes_largo_respuesta = socket_cliente.recv(4)
            largo_respuesta = int.from_bytes(bytes_largo_respuesta, byteorder='big')
            respuesta = b''

            while len(respuesta) < largo_respuesta:
                respuesta += socket_cliente.recv(256)
            recibido = respuesta.decode('utf-8')
            if recibido != '':
                respuesta = self.manejo_de_comandos(recibido, socket_cliente)
                self.send(respuesta, socket_cliente)

    def thread_aceptar_conexiones(self):
        while self.funcionando:
            try:
                socket_cliente, direccion = self.socket.accept()
                thread_escucha = Thread(target=self.thread_escuchar_cliente,
                                        args=(socket_cliente,))
                thread_escucha.start()
            except:
                log_i.info('Conexión terminada.')

    def aceptar_conexiones(self):
        thread_conexiones = Thread(target=self.thread_aceptar_conexiones)
        thread_conexiones.start()

    def finalizar_servidor(self):
        log_d.debug('Enviar mensaje a todos los usuario de que se terminará el servidor')
        space.info('-' * 100)
        log_i.info('Terminando servidor...')
        self.funcionando = False
        self.socket.close()
        sleep(0.01)

# ------------------------------------------------------------------------------------------------------------- COMANDOS

class ProcesadorComandos:
    def __init__(self, servidor):
        self.servidor = servidor
        self.funcionando = True
        self.comandos = {'desconectar': [None, 'Desconecta al cliente del servidor.'],
                         'terminar_servidor': [self.terminar_servidor, 'Finaliza la ejecución del servidor.'],
                         'usuario': [None, 'Solicita la incorporación de un usuario.'],
                         'lista_comandos': [self.lista_comandos, 'Muestra los comandos validos.'],}
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

    def terminar_servidor(self):
        self.servidor.finalizar_servidor()
        self.funcionando = False
        return 'Servidor finalizado.'





# ------------------------------------------------------------------------------------------------------------- CLIENTES


class ClienteUsuario:
    clientes = []

    def __init__(self, socket, direccion, nombre):
        self.socket = socket
        self.direccion = direccion
        self.nombre = nombre

    @staticmethod
    def usuario_valido(self, nombre_usuario):
        '''Verifica si ya existe un usuario activo con ese nombre, en cuyo casoretorna False. De lo contrario True'''
        for cliente in ClienteUsuario.clientes:
            if cliente.nombre == nombre_usuario:
                return False
            return True

    @staticmethod
    def agregar_usuario(self, *args):
        ClienteUsuario.clientes.append(ClienteUsuario(*args))


    @staticmethod
    def eliminar_usuario(self):
        pass











if __name__ == '__main__':

    servidor = Servidor(HOST, PORT)

    # while True:
    #     sleep(0.01)
    #     log_i.info(input('>>> '))
