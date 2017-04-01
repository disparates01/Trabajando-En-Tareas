class Pais:
	def __init__(self, name, poblacion, infectados = 0, muertos = 0, fecha_infeccion = None, aeropuerto = True, frontera = True, mascarillas = False, fecha_cura = None):
		self.name = name
		self.poblacion = poblacion
		self.infectados = infectados
		self.muertos = muertos
		self.fecha_infeccion = fecha_infeccion
		self.aeropuerto = aeropuerto
		self.frontera = frontera
		self.mascarillas = mascarillas
		self.fecha_cura = fecha_cura

	def avanzar_infeccion(self, infeccion):
		nuevos_infectados = sum([random.randint(0,6) for persona in range(1,100)])*infeccion.contagiosidad
		if self.mascarillas:
			nuevos_infectados *= 0.3
		self.infectados += nuevos_infectados
		return self.infectados
	
	def avanzar_muertes(self):
		nuevos_muertos = self.probabilidad_de_muerte * self.infectados
		self.muertos += nuevos_muertos
		return self.muertos

	def avanzar_contagio(self, today):
		if not self.infectado():
			return
		else:
			for pais in set(self.vecinos(lista_paises, grafo_terrestre)+self.vecinos(lista_paises, grafo_aereo)):
				min((0.07*self.infectados)/(self.poblacion*self.conecciones(grafo_terrestre, grafo_aereo, pais)),1)
		if random.random() > min((0.07*self.infectados)/(self.poblacion*self.conecciones(grafo_terrestre, grafo_aereo, pais)),1):
			pais.infectar(today)
		
	def avanzar_cura(self, today):
		if not self.curado:
			return
		else:
			paises_curados = []
			for pais in self.vecinos(lista_paises, grafo_aereo):
				pais.curar(today)
				paises_curados.append(pais)
		return paises_curados

	def aplicar_cura(self, infeccion):
		if self.curado:
			self.infectados *= 0.25*infeccion.resistencia
		return self.infectados

	def curado(self):
		return bool(fecha_cura)

	def infectado(self):
		return bool(fecha_infeccion)

	def curar(self, today):
		self.fecha_cura = today
		return self.fecha_cura

	def infectar(self, today):
		self.fecha_infeccion = today
		return self.fecha_infeccion

	def days_infected(self, today):
		return today - self.fecha_infeccion
	
	def conecciones(self, grafo_terrestre, grafo_aereo, pais2):
		conecciones = 0
		if pais2 in vecinos(grafo_terrestre):
			if self.frontera and pais2.frontera:
				conecciones += 1
		if pais2 in vecinos(grafo_aereo):
			if self.aeropuerto and pais2.aeropuerto:
				conecciones += 1
		return conecciones

	def	probabilidad_de_muerte(self, infection):
		return min(min(0.2,(self.days_infected*self.days_infected/100000))*infection.tasa_mortalidad,1)

	def probabilidad_de_contagio(self):
		return min((0.07*self.infectados/(poblacion*self.conecciones)),1)

	def sanos(self):
		return poblacion - infectados

	def porcentaje_infectados(self):
		return (infectados/poblacion)*100
	
	def vecinos(self, lista_paises, grafo):
		nombres_vecinos = grafo[self.name]
		return [pais for pais in lista_paises if pais.name in nombres_vecinos]
