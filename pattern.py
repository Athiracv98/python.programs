#basic pattern
# num=int(input("Enter rows : "))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#basic pattern reverse
num=int(input("Enter rows : "))
for i in range(num+1,1,-1):
    for j in range(num,i):
        print(j, end=" ")
        
    print()