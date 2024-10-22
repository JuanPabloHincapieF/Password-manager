import pandas as pd
from utilities.cipher import decrypt


def read_all_records():
    df = pd.read_csv('passwords.csv',sep=',')
    df['Password'] = df['Password'].apply(decrypt)
    print(df)


