from cryptography.fernet import Fernet
from Crypto.Util import number
import random
import hashlib

print("Algoritmo de Diffie-Hellman: ", '\n')

g = 2
p = 4294967295
ali = random.getrandbits(256)
bob = random.getrandbits(256)

a = print("Numero Aleatorio de Alice Silverstone: ", ali, '\n')
b = print("Numero Aleatorio de Bob Patiño: ", bob, '\n')

def potencia(x,y,z):
    print("El numero intercambiado de Alice es: ", "\n", pow(x,y,z))

A = potencia(g,ali,p)

def potencia(x,y,z):
    print("El numero intercambiado de Bob es: ", "\n", pow(x,y,z))

B = potencia(g,bob,p)

def potencia(x,y,z):
    print("La llave secreta de Alice es: ", "\n", pow(x,y,z))

s1 = potencia(B,a,p)

def potencia(x,y,z):
    print("La llave secreta de Alice es: ", "\n", pow(x,y,z))

s2 = potencia(A,b,p)
