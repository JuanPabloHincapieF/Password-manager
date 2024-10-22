from cryptography.fernet import Fernet

# Genera la clave una sola vez y guárdala para usarla en todo el proceso
key = Fernet.generate_key()
print(key)