from utilities import csv_verifier
from Controllers import create_entry,read_all_records,delete_record

def main():
    csv_verifier.verify_csv('passwords.csv')
    while True:
        choice = input('What do you want to do?\n[1]Read all records\n[2]Create a new entry\n[3]Delete a record\n[0]Exit\n')
        if choice == '1':
            read_all_records()
        elif choice == '2':
            create_entry()
        elif choice == '3':
            delete_record()
        elif choice == '0':
            break
        else:
            print('Invalid option')
            
main()