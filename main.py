EMP = []


def create():
    fname = input("Enter First Name of the person you want to add: ")
    lname = input("Enter Last Name of the person you want to add: ")
    age = input("Enter Age of the person you want to add: ")

    newItem = {"fname": fname, "lname": lname, "age": age}
    EMP.append(newItem)
    input("PRESS ENTER TO CONTINUE")


def retrieve():
    fname = input("Enter name of person: ")
    print("FNAME\tLNAME\tAGE")
    for i in EMP:
        if i["fname"] == fname:
            print(f'{i.get("fname")}\t{i.get("lname")}\t\t{i.get("age")}')
    print("THERE ARE NO MORE RECORDS TO SHOW")
    input("PRESS ENTER TO CONTINUE")

def ViewAll():
    if len(EMP) == 0:
        print("THERE ARE NO RECORDS TO SHOW")
    else:
        print("FNAME\tLNAME\tAGE")
        for i in EMP:
            print(f'{i.get("fname")}\t{i.get("lname")}\t\t{i.get("age")}')
    input("PRESS ENTER TO CONTINUE")


def delete():
    fname = input("Enter First Name of the person you want to delete: ")
    lname = input("Enter Last Name of the person you want to delete: ")
    flag = False
    for i in range(len(EMP)):
        if EMP[i].get("fname") == fname and EMP[i].get("lname") == lname:
            del EMP[i]
            flag = True
            print("Record was deleted")
            ViewAll()
    if flag:
        pass
    else:
        print("There was no such record")
    input("PRESS ENTER TO CONTINUE")


def update():
    fname = input("Enter First Name of the person you want to update: ")
    lname = input("Enter Last Name of the person you want to update: ")
    for i in EMP:
        if i.get("fname") == fname and i.get("lname") == lname:
            option = input("What do you want to update. Enter\n1 for First name\n2 for Last name\n3 for age: ")
            if option == '1':
                ans = input("Enter new first name: ")
                i["fname"] = ans
            if option == '2':
                ans = input("Enter new last name: ")
                i["lname"] = ans
            if option == '3':
                ans = input("Enter new age: ")
                i["age"] = ans
            else:
                print("Enter a valid number")
    input("PRESS ENTER TO CONTINUE")


isRunning = True
print("Welcome")
while isRunning:
    choice = input("What do you want to do?\n1. Add a new person\n2. Retrieve records\n"
                   "3. Update a record\n4. Delete a record\n5. View All\n6. Exit\n")

    if choice == '1':
        create()
    elif choice == '2':
        retrieve()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        ViewAll()
    elif choice == '6':
        isRunning = False
    else:
        choice = input("Enter a valid option\n")
