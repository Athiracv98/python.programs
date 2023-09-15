#44. write a program to retrieve the first item from a list
item=[2,3,4,5]
print(item[0])

#45. write a program to determine the length of a list
item=[2,3,4,5,8]
print(len(item))

#46. write a python program to change the first item in a list
item=[2,3,4,5,8]
item[0]=7
print(item)

#47. write a python program using negative indexing
item='athira'
print(item[-6:-3])

#48. write a program to add a new item to the end of a list
item=[2,3,4,5,8]
item.append(15)
print(item)

#49. create a list and display the list in reverse order
item=[2,3,4,5,8]
item.reverse()
print(item)

#50. write a program to find the maximum value in a list
item=[2,3,4,5,8]
print(max(item))

#51. write a program to display the index of an element in a list
item=[2,3,4,5,8]
print(item.index(5))

#52. write a program to count the occurrence of an Element in a list
item=[2,3,4,5,8,3]
print(item.count(3))

#53. create a nested list and display each item from the list

num=[2,4,[3,5,[7,6]],9]
sub5=num[0]
print(sub5)
sub6=num[1]
print(sub6)
sub7=num[-1]
print(sub7)
sub1=num[2][0]
print(sub1)
sub4=num[2][1]
print(sub4)
sub2=num[2][2][0]
print(sub2)
sub3=num[2][2][1]
print(sub3)


#54. Based on a list of fruits, create a new list, containing only the fruits with the letter "a" in the name.

fruits=['apple','orange','kiwi']
newlist=[]

for x in fruits:

    if "a" in x:
     newlist.append(x)
print(newlist)


#55. fruits = ["apple", "banana", "cherry", "kiwi", "mango"] Based on a list of fruits, create a new list, Only accept items that are not "kiwi"

fruits=['apple','orange','kiwi','plum']
newlist=[]
for x in fruits:

    if "kiwi" not in x:
     newlist.append(x)
print(newlist)
#56. fruits = ["apple", "banana", "cherry", "kiwi", "mango"] Based on a list of fruits, create a new list, Set the values in the new list to upper case
fruits=['apple','orange','kiwi','plum']
newlist=[x.upper() for x in fruits]
print(newlist)
#57. create a list and iterate over the list
list2 = [1, 2, 3, 4, 5]

# Iterating list using for loop
for i in list2:
    print(i)
    
