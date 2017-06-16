__author__ = 'Ricardo Del Río'

# Propios:
from loggers import MyLogger
from Cliente.cliente import Cliente, ProcesadorComandos, HOST, PORT, nombre_usuario

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



class PrograPopClient:
    def start(self):
        self.client = Cliente(HOST, PORT, nombre_usuario)
        self.procesador_comandos = ProcesadorComandos(self.client)
        self.client.procesador_comandos = self.procesador_comandos






class Sala:
    pass

if __name__ == '__main__':
    juego = PrograPopClient()
    juego.start()