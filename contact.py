contact={}
def insert():
    name = input("enter name:")
    phone = input("enter phone number:")
    contact[name] = phone
    print(contact)
def search():
    name1 = input("enter your name1")
    if name1 in contact:

        print("Name \t\t\t\t  number")
        print("{} \t\t\t\t {}".format(name1,contact.get(name1)))
def edit():
    edit_name = input("enter edited name")
    if edit_name in contact:
        phone = input("enter phone number\n")
        contact[edit_name] = phone
        display()
    else:
        print("name is not found")
def delete():
    deletename = input("enter name")
    if deletename in contact:

        item = input("do you want to delete yes or no?\n")
        if item == "yes":
            print("deleted", contact.pop(deletename))
            display()
        else:
            print("not deleted")
            display()
    else:
        print("no contact found")

def display():
    print("name \t\t\t\t contact number")
    for x in contact:
        print("{} \t\t\t\t {}".format(x,contact.get(x)))