#Herencia en python
from clases.Cliente import Cliente
from clases.Persona import Persona
#creo el obejto
persona = Cliente()

persona.nombre = input("NOMBRE: ")
persona.edad = int(input("EDAD: "))
persona.telefono = int(input("TELEFONO: "))
persona.direccion = input("DIRECCION: ")
persona.correo = input ("CORREO: ")
persona.saldo = int(input("SALDO"))


cliente1 = (persona.nombre,persona.edad,persona.telefono,persona.direccion,persona.correo)

#llamos la funcion
persona.saludar()


