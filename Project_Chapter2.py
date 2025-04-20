def main_menu():
    user_input = input("1.Insert a new record\n2.Search by ID\n3.Print ages average\n4.Print all names\n5.Print all IDs\n6.Print all records\n7.Print record by index\n8.Exit\nyour choice: ")
    return user_input

#the function checks if the inputs for a new records are valid, if not - return to the menu
def add_record(records):
    new_id = input("ID: ")
    if not valid_id(new_id, records):
        return
    
    new_name = input("Name: ")
    if not valid_name(new_name):
        return
    
    new_age = input("Age: ")
    if not valid_age(new_age):
        return

    add_new_record(records, new_id, new_name, new_age)

def valid_id(new_id, records):
    is_valid_id = True
    if not new_id.isdigit():
       print(f"ID must be a number.{new_id} is not a number")
       is_valid_id = False
    if new_id in records:
       print("ID is already exsits")
       is_valid_id = False
    return is_valid_id

def valid_name(new_name):
    if not new_name.isalpha():
        print(f"Name must includ only letters.{new_name} is not a valid name") 
        return False
    return True

def valid_age(new_age):
    if new_age.isdigit():
        if 1 < int(new_age) < 120:
            return True
        else:
            print("Age is not in rational range")
    else:
        print("Age  must includ only digits")
    return False

def add_new_record(records,id,name,age):
    global total_age, records_count
    records[id] = {
        "name": name,
        "age": int(age)
    } 
    total_age += int(age)
    records_count += 1
    print(f"ID [{id}] saved successfuly")

def print_record(id, records):
    print(f"ID: {id}\nName: {records[id]['name']}\nAge: {records[id]['age']}")

def search_by_id(records, id):
    if id in records:
        print_record(id,records)
    else:
        print("ID does not exsist")

def print_all_records(records):
    for index, (id, record) in enumerate(records.items()):
        print(f"{index}. ID: {id}\n   Name: {record['name']}\n   Age: {record['age']}\n")

def print_all_names(records):
    for index, record in enumerate(records.values()):
        print(f"{index}. {record['name']}")

def print_all_ids(records):
    for index, id in enumerate(records):
        print(f"{index}. {id}")

def ages_average():
    if records_count == 0:
        return 0
    return total_age / records_count

def print_by_index(records, user_index):
    if user_index.isdigit():
        user_index = int(user_index)
        if 0 <= user_index < len(records):
            items_list = list(records.items())
            id, record = items_list[user_index]
            print(f"ID: {id}\nName: {record['name']}\nAge: {record['age']}")       
        else:
            print("Index out of range")
    else:
        print(f"Index must be a number. {user_index} is not a number")

records = {    "123456789": {"name": "Omri", "age": 35},
                "987654321": {"name": "Shahar", "age": 28}
    }

#if records is empthy, the following variables values are 0 at the start of the program. 
total_age = 28 + 35
records_count = 2

print("Welcome! please choose one of the following options:")
user_input = 0

while user_input != 8:
    user_input = int(main_menu())
    if user_input == 1: 
        add_record(records)
    elif user_input == 2: 
        search_by_id(records, input("Please enter the ID you want to look for: "))
    elif user_input == 3:
        print(f"Ages average is: {str(ages_average())}")
    elif user_input == 4: 
        print_all_names(records)
    elif user_input == 5: 
        print_all_ids(records)
    elif user_input == 6: 
        print_all_records(records)
    elif user_input == 7:     
        print_by_index(records, input("Please enter the index of  the record you want to print: "))
    elif user_input == 8:
        end_program = input("Are you sure? (y/n): ").lower()
        while end_program not in ("y", "n"):
            end_program = input("Invalid input. Please enter 'y' or 'n': ").lower()
        if end_program == "y":
            print("Bye!")
            break
        else:
            user_input = 0
    else:
        print("Please choose a number between 1-8 ")
    input("Press Enter to continue")

