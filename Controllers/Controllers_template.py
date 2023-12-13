import csv

def create_record(file, new_record):
    with open(file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_record)

def read_record(file):
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def update_record(file, updating_id, new_record):
    with open(file, mode='r') as f:
        rows = list(csv.reader(f))
        for i, row in enumerate(rows):
            if row[0] == updating_id:
                rows[i] = new_record

    with open(file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def delete_record(file, deleting_id):
    with open(file, mode='r') as f:
        rows = list(csv.reader(f))
        new_rows = [row for row in rows if row[0] != deleting_id]

    with open(file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

# Example:
file_csv = 'passwords.csv'

# create record
new_record = ['1', 'Mail', 'user', 'password123']
create_record(file_csv, new_record)

# Read records
print("Actual records:")
read_record(file_csv)

# Update record
updating_id = '1'
new_record_updated = ['1', 'Mail', 'modified_user', 'modified_password']
update_record(file_csv, updating_id, new_record_updated)

# Read records after updating
print("\nRecords after updating:")
read_record(file_csv)

# delete record
deleting_id = '1'
delete_record(file_csv, deleting_id)

# Read records after deleting:
print("\nRecords after deleting:")
read_record(file_csv)
