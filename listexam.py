'''list1=[2,3,3,4,6]
se=set(list1)
list1=list(se)
print(list1)


list2=[72,4,5,66]
big=list2[0]
for i in list2:
   if i>big:
      big=i
print(big)'''

# list1=[2,3,3,4,6]
# lis=[]
# for i in list1:
#     if i not in lis:
#         lis.append(i)
# print(lis)

# li1=["age","name"]
# l2=[20,"athira"]
# print(dict(zip(li1,l2)))




# list2=[72,4,5,66]
# l=len(list2)
# big=list2[0]
# for i in list2:
#    if i>big:
#       big=i
# print(big)
# for i in range(0,l):

# li=[4,5,3,2,1]
# n=len(li)

# li.sort()

        
# print(li)
# li[0]=li[n-1]
# li[n-1]=t
# print(li)
my_list=[2,1,5,4]
tem = 0
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)):
       
        if my_list[i]<my_list[j]:
            
            tem = my_list[i]
            
            my_list[i] = my_list[j]
            my_list[j] = tem
           

print(f"After sorting: {my_list}")
    
   
       
        
            


   







