import csv
from utilities import cipher

def create_record(file):
    print('---------Creating new entry---------')
    title = input("Title: ")
    user = input("Username: ")
    password = input("Password: ")
    encryption = utilities.cipher.encrypt(password,3)
    new_record = [title, user, encryption]
    
    with open(file, mode='a', newline='') as f:
        
        writer = csv.writer(f)
        writer.writerow(new_record)
        
create_record('passwords.csv')
