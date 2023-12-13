import pandas as pd


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
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
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text



def read_all_records():
    df = pd.read_csv('passwords.csv',sep=',')
    df['Password'] = df['Password'].apply(lambda x : decrypt(x,3))
    print(df)


