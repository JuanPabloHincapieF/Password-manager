from cryptography.fernet import Fernet

key = b'G19JOZox5xRKOQRBWnjBBuA11xiFtgzvtRBEtL5Wc8w='
cipher_suite = Fernet(key)

def encrypt(text):
    return cipher_suite.encrypt(text.encode())

def decrypt(token):
    return cipher_suite.decrypt(token).decode()
