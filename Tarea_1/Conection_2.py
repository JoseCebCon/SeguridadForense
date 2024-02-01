from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("Llave", key)
f = Fernet(key)
token = f.encrypt(b"Mother on the dance floor")

print ("token",token)

d = Fernet(key)
print("Mensaje:", d.decrypt(token))