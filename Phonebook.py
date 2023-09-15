contact={}
def display():
    print("name \t\t\t\t contact number")
    for x in contact:
        print("{} \t\t\t\t {}".format(x,contact.get(x)))
while True:
    choice=int(input("1.add\n 2.search\n 3.display\n 4.edit\n 5.delete\n 6.exit\n enter your choice?"))
    if choice==1:

        # n=int(input("enter range"))

        '''for i in range(n):
            
            if name in contact:
                print("already exist")
            else:'''
        name = input("enter name:")
        phone = input("enter phone number:")
        contact[name] = phone
        print(contact)
    elif choice==2:

        name1=input("enter your name1")
        if name1 in contact:
            print("name:",name1, "\ncontact number:",contact[name],"\n")

        else:
            print("contact not found")
    elif choice==3:
        if len(contact)==0:
        #if not contact:
            print("contact list is empty\n")
        else:
            display()
            # print("contact name :",name)
            # print("contact number:",contact[name])
    elif choice==4:
        edit_name=input("enter edited name")
        if edit_name in contact:
             phone=input("enter phone number\n")
             contact[name]=phone
             display()
        else:
            print("name is not found")
        
    elif choice==5:
        deletename=input("enter name")
        if deletename in contact:

             item=input("do you want to delete yes or no?\n")
             if  item=="yes":
                 print("deleted",contact.pop(deletename))
                 display()
             else:
                 print("not deleted")
                 display()
        else:
            print("no contact found")

    elif choice==6:
        exit()
    else:
        print("invalid choice\n")




