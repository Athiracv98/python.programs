#write a program to create a tuple
#62. write a program to get the length of a tuple
tup=(2,3,4)
newtup=len(tup)
print(newtup)

#63. write a program to return the data type of a tuple
tup=(2,3,4)
print(type(tup))

#64. create a tuple with items kiwi, orange, grapes, apple,
tupl=("kiwi","orange","grapes","apple")
print(tupl)
#65. then add a new item (melon) to the first index
tupl=("kiwi","orange","grapes","apple")
add=("melon",)+tupl
print(add)
#66. write a program to append an item to the tuple
tupl=("kiwi","orange","grapes","apple")
add=tupl+("melon",)
print(add)
#67. write a program to remove an item from a tuple
tupl=("kiwi","orange","grapes","apple")
li=list(tupl)
li.remove("grapes")
tupl=tuple(li)
print(tupl)
print(type(tupl))
#68. write a program to concatenate two tuples
tup1=(2,3,4)
tup2=(5,6,7)
tup3=tup1+tup2
print(tup3)
#69. write a program to extract the values from a tuple into variables
#70. extract values from tuple using Asterix
#71. count the number of occurrences of an item in a tuple
tup1=(2,3,4,2)
print(tup1.count(2))
#72. remove items from a tuple by using merge with + Character
#73. slice a tuple using start-stop, step parameter

#74. slice a tuple with step parameter is negative
tup1=(2,3,4,2,6,7,8,9,5,4,6,5)
print(tup1[-12:])
#75. returns a tuple with a jump every 3 times
tup1=(2,3,4,2,6,7,8,9,5,4,6,5)
print(tup1[-12:-1:3])
#76. find the maximum value in a tuple
tup1=(2,3,4,2)
print(max(tup1))
#77. Find min value in a tuple
tup1=(2,3,4,2)
print(min(tup1))
#78. find the sum of items in a tuple
tup1=(2,3,4,2)
print(sum(tup1))
