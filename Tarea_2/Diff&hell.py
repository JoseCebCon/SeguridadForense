import random
import hashlib

print("Algoritmo de Diffie-Hellman: ", '\n')

def public_key(g, clave_privada, p):
    return pow(g, clave_privada, p)

def Secret_key(llave_publica_externa, clave_privada, p):
    return pow(llave_publica_externa, clave_privada, p)

def hash_calculate(valor):
    return hashlib.sha256(str(valor).encode()).hexdigest()

#Usar el número primo estándar del algoritmo Diffie-Hellman.
p = 4294967295
g = 2

#Tamaño estándar de las claves privadas
priv_Alice = random.getrandbits(256)
priv_Bob = random.getrandbits(256)

#Intercambio de Alice y Bob
pub_alice = public_key(g, priv_Alice, p)
pub_bob = public_key(g, priv_Bob, p)

#Obtener llave secreta y que sean iguales
sec_alice = Secret_key(pub_bob, priv_Alice, p)
sec_bob = Secret_key(pub_alice, priv_Bob, p)

# Verificar si las llaves secretas son iguales
hash_alice = hash_calculate(sec_alice)
hash_bob = hash_calculate(sec_bob)

print("\nLa clave privada de Alice es:", priv_Alice)
print("La llave pública de Alice es:", pub_alice)

print("\La Clave privada de Bob es:", priv_Bob)
print("La llave pública de Bob es:", pub_bob)

print("\nLa llave secreta de Alice es:", sec_alice)
print("El hash de la llave secreta de Alice es:", hash_alice)

print("\nLa llave secreta de Bob es:", sec_bob)
print("El hash de la llave secreta de Bob es:", hash_bob)

if hash_alice == hash_bob:
    print("\nLas llaves secretas son iguales. Comunicación segura.")
else:
    print("\nLas llaves secretas son diferentes. Error en la comunicación.")