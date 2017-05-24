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
    def __init__(self, vida, ubicacion, sprite_sheet, vel_mov, danho, vel_ataque, rango_ataque, nombre, habilidad_unica, enfriamiento_hab, muertes, ts_habilidad):
        super().__init__(vida, ubicacion, vel_mov, danho, vel_ataque, rango_ataque, sprite_sheet)
        self.nombre = nombre
        self.habilidad_unica = habilidad_unica
        self.enfriamiento_hab = enfriamiento_hab
        self.muertes = muertes
        self.ts_habilidad = ts_habilidad

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







