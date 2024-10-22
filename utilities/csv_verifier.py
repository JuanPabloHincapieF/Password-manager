import os 
import pandas as pd

def verify_csv(route):
    if not os.path.exists(route):
        passwords = pd.DataFrame({
                'Title':[],
                'Username':[],
                'Password':[]
            } )
        
        passwords.to_csv(route,index=False)
        
verify_csv('passwords.csv')