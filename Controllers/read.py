import pandas as pd

def read_all_records():
    passwords = pd.read_csv('passwords.csv',sep=',',names=['Title','Username','Password'])
    return passwords.loc[:,['Title','Username']]
            
print(read_all_records())