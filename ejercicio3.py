#Crearemos una clase llamada Serie

class Serie:
	def __init__(self,titulo="",nTemp=3,entregado=False,genero="",creador=""):
		self.titulo = titulo
		self.nTemp = nTemp
		self.entregado = entregado
		self.genero = genero
		self.creador = creador

	def entregar(self, s):
		self.entregado = True

class Videojuego:
	def __init__(self,titulo="",horasEstimadas=10,entregado=False, genero="", comp=""):
		self.titulo = titulo
		self.horasEstimadas = horasEstimadas
		self.entregado = entregado
		self.genero = genero
		self.comp = comp

	def entregarVideojuego(self, v):
		self.entregado = True


serie1 = Serie("Friends", 10,False,"Comedia", "Kevin S. Bright")
serie2 = Serie("Twin Peaks", 3,True,"Sci-Fi", "David Lynch")
serie3 = Serie("Los Soprano", 6,True,"Drama", "Varios")
serie4 = Serie("Hannibal", 3 ,True,"Suspense", "Bryan Fuller")
serie5 = Serie("Los Simpsons", 31,True,"Comedia", "Varios")


juego1 = Videojuego("Doom", 10, False, "FPS", "Id Software")
juego2 = Videojuego("Monkey Island", 5, True, "Aventura Gráfica", "Lucas Arts")
juego3 = Videojuego("Overwatch", 9000, True, "FPS", "Blizzard")
juego4 = Videojuego("Celeste", 10, True, "Plataformas", "Matt Makes Games")
juego5 = Videojuego("Mass Effect", 50, False, "RPG/Accion", "Bioware")

#Entregar serie
serie1.entregar(serie1)
print(serie1.entregado)

lista_series=[serie1,serie2,serie3,serie4,serie5]
lista_juegos=[juego1,juego2,juego3,juego4,juego5]

#Entregar videojuego
juego1.entregarVideojuego(juego1)
print(juego1.entregado)

contSeries=0
contVideojuego=0

maxHorasJuego=0
maxTempSeries=0
vjMax = juego1
serieMax = serie1

for i in lista_series:
	if i.entregado == True:
		contSeries += 1

	if i.nTemp > maxTempSeries:
		maxTempSeries = i.nTemp
		serieMax = i		
		

for i in lista_juegos:
	if i.entregado == True:
		contVideojuego += 1

	if i.horasEstimadas > maxHorasJuego:
		maxHorasJuego = i.horasEstimadas
		vjMax = i		


print("Series entregadas: " , contSeries)	
print("Juegos entregados: " , contVideojuego)
print("Serie con mas temporadas:", serieMax.titulo)
print("Videojuego con mas horas:", vjMax.titulo)	