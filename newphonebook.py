import contact

while True:
    choice=int(input("1.add\n 2.search\n 3.display\n 4.edit\n 5.delete\n 6.exit\n enter your choice?"))
    if choice==1:
        contact.insert()
    elif choice==2:
        contact.search()
    elif choice==3:
        contact.display()
    elif choice==4:
        contact.edit()
        contact.display()
    elif choice==5:
        contact.delete()
    elif choice==6:

        exit()
    else:
        print("invalid choice")


