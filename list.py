list_in=[4,5,6]
list_in.extend([2,45,67,89])
print(list_in)

del list_in[1]
print(list_in)
list_in[1]=7
print(list_in)
list_in.remove(45)
print(list_in)
list_in.pop()
print(list_in)
list_in.pop(2)
print(list_in)
list_in.clear()
print(list_in)
del list_in
print(list_in)
list2=[3,4,5]
print(list2.index(4))

print(list2.count(5))
