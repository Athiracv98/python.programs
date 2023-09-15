'''a=[]
n=int(input("enter limit"))
print("enter numbers")
for i in range(1,n+1):
    m=int(input())
    a.append(m)
m=a[0]
for i in range(1,n):
    if m<a[i]:
        m=a[i]
print(m)'''

'''a=[]
n=int(input("enter limit"))
print("enter numbers")
for i in range(1,n+1):
    m=int(input())
    a.append(m)
m=a[0]
for i in range(1,n):
    if m<a[i]:
        m=a[i]
for i in range(1,n):
    if a[i]==m:
        m=a[i]
    else:'''


a = []
n = int(input("Enter the limit array :"))
print("Enter the elements : ")
for i in range(0, n):
    no = int(input())
    a.append(no)
big = a[0]
for i in range(1, n):
    if a[i] > big:
        big = a[i]
if big == a[0]:
    sbig = a[1]
    print(sbig)
else:
    sbig = a[0]
    print(sbig)
for i in range(0, n):
    if a[i] < big and a[i] > sbig:
        sbig = a[i]

print("Second largest is : ", sbig)

'''a = []
n = int(input("Enter the limit array: "))
print("Enter the elements: ")
for i in range(0, n):
    no = int(input())
    a.append(no)

big = max(a)
sbig = min(a)

for num in a:
    if num < big and num > sbig:
        sbig = num

print("Second largest is:", sbig)
'''











