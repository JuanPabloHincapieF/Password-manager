import pandas as pd
from utilities.cipher import encrypt

def create_entry():
    df = pd.read_csv('passwords.csv',header=0)
    print('---------Creating new entry---------')
    title = input("Title: ")
    user = input("Username: ")
    password = input("Password: ")
    password = encrypt(password)
    df = df._append({'Title':title,'Username':user,'Password':password},ignore_index=True)
    df.to_csv('passwords.csv',index=False)
    