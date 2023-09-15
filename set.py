set1={2,3,4,2}
print(set1)
det=set([2,3,4,5,4])
print(det)
det.add(12)
print(det)
det.update([23,34])
print(det)
w={2,3,4,5}
w.discard(4)
print(w)
w.remove(2)
print(w)
w.discard(100)
print(w)
'''w.remove(100)
print(w)'''

#write a program to find the length of a set
se={3,4,5}
print(len(se))
#81. write a program to create a set
de=set([3,4,5])
print(de)
#82. write a program to remove an item from the set using the remove method
se2={3,4,5,6}
se2.remove(4)
print(se2)
# 83. write a program to add items from one set to another
sett={3,4,5,6}
set4={4,7,8}
sett.update(set4)
print(sett)
#84. write a program to join two sets
set5={5,6,7}
set6={8,9,5}
set5.update(set6)
print(set5)

#85. write a program to remove an item from the set using the discard method
set7={5,6,7}
set7.discard(5)
print(set7)
# 86. write a program to add an item to a set
set8={5,6,8}
set8.add(56)
print(set8)
#87. write a program using the symmetric difference method
set9={3,5,6}
set10={4,5,8}
print(set9.symmetric_difference(set10))
#88. write a program using the intersection update method
set1={2,5}
set2={5,6}
print(set1.intersection(set2))

word="python"
s=word[::-1]
print(s)
word=["py"]
word.reverse()
print(word)
