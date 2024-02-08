import hashlib
import random 

print("Ataque MITM de Diffie-Hellman: ", '\n')

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
priv_Eve = random.getrandbits(256)

#Calcular la llave secreta entre Alice y Eve, y Bob y Eve.
pub_alice = public_key(g, priv_Alice, p)
pub_bob = public_key(g, priv_Bob, p)

# Eve intercepta las llaves públicas de Alice y Bob
pub_eve_alice = pub_bob
pub_eve_bob = pub_alice

# Eve calcula la llave secreta entre Alice y Eve, y Bob y Eve
sec_alice_eve = Secret_key(pub_eve_alice, priv_Eve, p)
sec_bob_eve = Secret_key(pub_eve_bob, priv_Eve, p)

# Verificar si las llaves secretas son iguales entre Alice y Eve, y Bob y Eve
hash_sec_alice_eve = hash_calculate(sec_alice_eve)
hash_sec_bob_eve = hash_calculate(sec_bob_eve)

print("La llave secreta entre Alice y Eve es:", pub_eve_alice)
print("Hash de la llave secreta entre Alice y Eve:", hash_sec_alice_eve)

print("\nla llave secreta entre Bob y Eve:", pub_eve_bob)
print("Hash de la llave secreta entre Bob y Eve:", hash_sec_bob_eve)

# Verificar si las llaves secretas son iguales
if hash_sec_alice_eve == hash_sec_bob_eve:
    print("\nEve ha conseguido atrapar y calcular la misma llave secreta entre Alice y Bob.")
    print("Comunicación comprometida.")
else:
    print("\nEve no ha conseguido obtener la misma llave secreta entre Alice y Bob.")
    print("Comunicación segura.")