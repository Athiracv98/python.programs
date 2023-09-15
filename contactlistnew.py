contactlist={}
n=int(input("enter no:of contacts"))
for i in range(1,n+1):
    name=input("enter name")
    phone=input("enter number")
    contactlist[name]=phone
print("name \t\t number")
print("{} \t\t {}".format(name,contactlist.get(name)))
print("\n keys \n")
for i in contactlist.keys():
    print(i,"\n")
for i in contactlist:
    print(contactlist[i])

for x,y in contactlist.items():


    print(x,"",y)