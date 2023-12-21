import pandas as pd

def delete_record():
    record_to_delete = input("Enter the title of the record you want to delete")
    df = pd.read_csv('passwords.csv',header=0)
    result = list(df['Title'].str.contains(record_to_delete))
    for i in result:
        if i:
            df = df[df['Title'] != record_to_delete]
            df.to_csv('passwords.csv',index=False)
            print(f"Record with username '{record_to_delete}' deleted successfully.")
            break

