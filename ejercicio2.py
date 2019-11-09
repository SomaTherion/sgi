

class Electrodomestico:
	def __init__(self,precio=100,color="BLANCO",consumo='F',peso=5):
		self.precio = precio
		self.color = color
		self.consumo = consumo
		self.peso = peso

def comprobarColores(color): #colores disponibles

	color_valido = False
	lista_colores = ["BLANCO", "NEGRO", "ROJO", "AZUL", "GRIS"]

	for item in lista_colores:
		if color.upper() in lista_colores:
			color_valido = True

	if (color_valido):
		return color	
	else:
		return "BLANCO"

def comprobarConsumo(letra): #comprueba que la letra es correcta

	letra_valida = False
	lista_letras = ['A', 'B', 'C', 'D', 'E', 'F']

	for item in lista_letras:
		if letra.upper() in lista_letras:
			letra_valida = True

	if (letra_valida):
		return letra	
	else:
		return 'F'  #si no es correcta usara la letra por defecto.

def precioFinal(e): #Dependiendo del consumo y su tamaño se calcula el precio
	
	precioFinal = 0

	if e.consumo == 'A':
		precioFinal += 100
	elif e.consumo == 'B':
		precioFinal += 80
	elif e.consumo == 'C':	
		precioFinal += 60
	elif e.consumo == 'D':
		precioFinal += 50
	elif e.consumo == 'E':	
		precioFinal += 30
	elif e.consumo == 'F':
		precioFinal += 10

	if e.peso < 20:
		precioFinal += 10
	elif e.peso < 50:
		precioFinal += 50
	elif e.peso < 80:
		precioFinal += 80
	elif e.peso > 80:
		precioFinal += 100	

	e.precio = precioFinal


class Lavadora(Electrodomestico):

	def __init__(self,carga=5):

		super().__init__(100,comprobarColores("gris"), comprobarConsumo('A'), 70)
		print(super().precio)
		self.carga = carga

	def precioFinalLavadora(l): #carga mayor de 30 kg, aumenta el precio 50€
		if lav.carga > 30:
			lav.precio += 50
		print(lav.precio)	


class Televisor(Electrodomestico):
	def __init__(self, resolucion=20, fourk=False):
		self.resolucion = resolucion
		self.fourk = fourk

	def precioFinalTele(t): # si tiene una tamaño mayor de 40, aumentara el precio 30%, 4K 50e
		if t.res > 40:
			t.precio = t.precio + (t.precio*0.3)
		if t.res == 4:
			t.precio += 50


#e = Electrodomestico(100,comprobarColores("gris"), comprobarConsumo('A'), 70)
#precioFinal(e)
#print(e.precio)

#l = Lavadora(40)