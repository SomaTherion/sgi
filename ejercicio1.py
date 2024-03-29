
import random
#Haz una clase llamada Persona que siga las siguientes condiciones:

#    Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el mÃ¡s adecuado, tambiÃ©n su tipo. Si quieres aÃ±adir algÃºn atributo puedes hacerlo.
#   Por defecto, todos los atributos menos el DNI serÃ¡n valores por defecto segÃºn su tipo (0 nÃºmeros, cadena vacÃ­a para String, etc.). Sexo sera mujer por defecto.

class Persona:
#Un constructor con todos los atributos como parÃ¡metro.
	def __init__(self, nombre="Defecto", edad=0, dni="", sexo='M', peso=0.0, altura=0.0):
		self.nombre = nombre
		self.edad = edad
		self.dni = dni
		self.sexo = sexo
		self.peso = peso
		self.altura = altura

#Los mÃ©todos que se implementaran son:

def calcularIMC(persona):	#calcula si la persona esta en su peso ideal
	try:
		pesoIdeal = (persona.peso / persona.altura**2)

		if (pesoIdeal<18.5):
			print("Tiene infrapeso")
		elif (pesoIdeal>18.5 and pesoIdeal<25):
			print("Esta en su peso")
		else:
			print("Tiene sobrepeso")
	except:
		print("Altura o peso no especificado")

def comprobarEdad(persona): #indica si persona es mayor de edad
		if (persona.edad>=18):
			return True
		else:
			return False

def introducirSexo(): #introducido el sexo
	sexo = input("Introduce sexo:")
	if sexo == 'H' or 'h':
		return sexo
	else:
		return 'M'


def generaDni(): #Genera dni y calcula su letra
	dniNum = random.randrange(00000000,99999999)
	dniNumString = str(dniNumero).zfill(8)
	letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
	letra = letras[dniNumero%23]
	dni = dniNumeroString+letra
	return dni


def toString(persona): #Devuelve toda la informacion del objeto persona
	print("Nombre:", persona.nombre, "\nEdad:", persona.edad, "\nDNI:", persona.dni, "\nSexo:", persona.sexo, "\nPeso:", persona.peso,
	 "\nAltura:", persona.altura)

#Ejecutable
def ejecutable():
	nombre = input("Introduce el nombre de la persona:")
	edad = int(input("Introduce su edad:"))
	sexo = introducirSexo()
	peso = float(input("Introduce el peso:"))
	altura = float(input("Introduce la altura (en metros):"))
	dni = generaDni()

	#Creamos tres objetos
	# El primer objeto obtendrá las anteriores variables pedidas por teclado
	persona = Persona(nombre, edad, generaDni(), sexo, peso, altura)
	#el segundo objeto obtendrá todos los anteriores menos el peso y la altura
	persona2 = Persona(nombre, edad, generaDni(), sexo)
	#el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
	persona3 = Persona() #por defecto
	persona3.edad = "Francisco"
	persona3.edad = 25
	persona3.sexo = 'H'
	persona3.peso = 83.2
	persona3.altura = 1.85

	listaPersonas = [persona, persona2, persona3]

	#Comprobaciones peso y edad
	for persona in listaPersonas:
		toString(persona)
		calcularImc(persona)
		if comprobarEdad(p) == True:
			print("Es mayor de edad")
		else:
			print("Es menor de edad")	

ejecutable()





