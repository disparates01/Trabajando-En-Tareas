__author__ = 'Ricardo Del Río'

from socket import gethostname, gethostbyname
from datetime import datetime as dt
from socket import AF_INET, SOCK_STREAM
from os import listdir, getcwd, chdir

from loggers import MyLogger, prueba
log1 = MyLogger(__name__, name='SERVIDOR', formatter='%(name)s[{0}]:   %(message)s'.format(__name__))
log2 = MyLogger(__name__, name='SERVIDOR', nombre_archivo='servidor.log', stream_handler=False)
space = MyLogger(__name__, formatter='%(message)s')

HOST = gethostbyname(gethostname())
PORT = 8080

class Servidor:
    def __init__(self, HOST, PORT):
        log1.info('Iniciando servidor...')
        space.info('')
        self.HOST = HOST
        self.PORT = PORT

        log1.info('HOST:       {}'.format(self.HOST))
        log1.info('PORT:       {}'.format(self.PORT))
        log1.info('UBICACIÓN:  {}'.format(getcwd()))
        space.info('')

        log2.warning('Completar... ')

        log1.info('Servidor iniciado: {}'.format(dt.now()))
        space.info('')
        space.info('-'*100)
        space.info('')






if __name__ == '__main__':

    servidor = Servidor(HOST, PORT)
