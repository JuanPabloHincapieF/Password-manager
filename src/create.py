import pandas as pd

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def create_entry():
    df = pd.read_csv('passwords.csv',header=0)
    print('---------Creating new entry---------')
    title = input("Title: ")
    user = input("Username: ")
    password = input("Password: ")
    password = encrypt(password,5)
    df = df._append({'Title':title,'Username':user,'Password':password},ignore_index=True)
    df.to_csv('passwords.csv',index=False)
    