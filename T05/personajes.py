from logging import getLogger, DEBUG, WARNING, ERROR, INFO
from loggers import archivo_logs, stream_handler, file_handler

# ------------------------------------------------------------------------------------------------------------- LOGGERS
archivo_logs()
info = getLogger('INFO [{}'.format(__name__))
info.setLevel(INFO)
info.addHandler(stream_handler)
info.addHandler(file_handler)
debug = getLogger('DEBUG [{}'.format(__name__))
debug.setLevel(DEBUG)
debug.addHandler(file_handler)
warning = getLogger('WARNING [{}'.format(__name__))
warning.setLevel(WARNING)
warning.addHandler(file_handler)
error = getLogger('ERROR [{}'.format(__name__))
error.setLevel(ERROR)
error.addHandler(file_handler)
# ------------------------------------------------------------------------------------------------------------- * * *


class EdificiosUnidades:
    def __init__(self, vida, ubicacion, sprite_sheet, team):
        self.vida = vida
        self.ubicacion = ubicacion
        self.sprite_sheet = sprite_sheet
        self.team = team



class Unidades(EdificiosUnidades):
    def __init__(self, vida, ubicacion, sprite_sheet, vel_mov, danho, vel_ataque, rango_ataque, orientacion, ts_ataque):
        super().__init__(vida, ubicacion, sprite_sheet)
        self.vel_mov = vel_mov
        self.danho = danho
        self.vel_ataque = vel_ataque
        self.rango_ataque = rango_ataque
        self.orientacion = orientacion
        self.ts_ataque = ts_ataque

class Campeones(Unidades):
    def __init__(self, vida, ubicacion, sprite_sheet, vel_mov, danho, vel_ataque, rango_ataque, nombre, habilidad_unica, enfriamiento_hab, muertes, ts_habilidad, personalidad, puntos, gastados, kills, destino):
        super().__init__(vida, ubicacion, vel_mov, danho, vel_ataque, rango_ataque, sprite_sheet)
        self.nombre = nombre
        self.habilidad_unica = habilidad_unica
        self.enfriamiento_hab = enfriamiento_hab
        self.muertes = muertes
        self.ts_habilidad = ts_habilidad
        self.personalidad = personalidad
        self.puntos = puntos
        self.gastados = gastados
        self.kills = kills
        self.destino = destino

class Subditos(Unidades):
    def __init__(self, vida, ubicacion, sprite_sheet, vel_mov, danho, vel_ataque, rango_ataque, tipo):
        super().__init__(vida, ubicacion, sprite_sheet, vel_mov, danho, vel_ataque, rango_ataque)
        self.tipo = tipo

class Torre(EdificiosUnidades):
    def __init__(self, vida, ubicacion, sprite_sheet, danho, vel_ataque, rango_ataque):
        super().__init__(vida, ubicacion, sprite_sheet)
        self.danho = danho
        self.vel_ataque = vel_ataque
        self.rango_ataque = rango_ataque

class Inhibidor(EdificiosUnidades):
    def __init__(self, vida, ubicacion, sprite_sheet):
        super().__init__(vida, ubicacion, sprite_sheet)

class Nexo(EdificiosUnidades):
    def __init__(self, vida, ubicacion, sprite_sheet):
        super().__init__(vida, ubicacion, sprite_sheet)







