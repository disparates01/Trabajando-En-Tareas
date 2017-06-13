__author__ = 'Ricardo Del Río'

# Propios:
from loggers import MyLogger
from Servidor.servidor import Servidor, ClienteUsuario, ProcesadorComandos, HOST, PORT




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



class PrograPopServer:
    def start(self):
        self.servidor = Servidor(HOST, PORT)
        self.procesador_comandos = ProcesadorComandos(self.servidor)






class Sala:
    pass

if __name__ == '__main__':
    juego = PrograPopServer()
    juego.start()