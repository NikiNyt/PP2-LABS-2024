import psycopg2,csv
from config import data
config = psycopg2.connect(**data)
current = config.cursor()

insert = """
    INSERT INTO phonebook(user_name, user_phone) VALUES(%s,%s) returning *;
"""

update = """
    UPDATE phonebook SET user_phone = %s WHERE user_name = %s;
"""

select = """
    SELECT * FROM phonebook;
"""

delete = """
    DELETE FROM phonebook WHERE user_name = %s;
"""

while True:
    command = input("insert, update, select, delete, exit\n")
    
    if command == 'insert':
        n = int(input("Insert by csv 1, from console 2\n"))
        if n == 1:
            with open("PhoneBook.csv", "r") as data_to_insert:
                reader = csv.reader(data_to_insert, delimiter=",")
                for row in reader:
                    current.execute(insert, row)
            config.commit()
        if n == 2:
            name = input("Enter the name to add:")
            phoneNumber = input("Enter the number:")
            current.execute(insert, (name, phoneNumber))
            config.commit()
            
    if command == 'update':
        name = input("Enter the name to update:")
        phone_number = input("Enter the phone number:")
        current.execute(update, (phone_number,name))
        config.commit()
    if command == 'select':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        config.commit()
    if command == 'delete':
        name = input("Enter name to delete:")
        current.execute(delete, [name])
        config.commit()
    if command == 'exit':
        break

current.close()
config.commit()
config.close()