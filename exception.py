'''num=int(input("enter number"))
print("menu")
print("1.automorphic")
print("2.trimorphic")
cho=int(input("enter choice"))
l=len(str(num))
print(l)
if cho==1:
    sq=num**2
    if sq%(10**l)==num:
        print(num,"is automorphic")
    else:
        print(" not automorphic")
elif cho==2:
    cu=num**3
    if cu%(10*l)==num:
        print(num,"is triomorphic")
    else:
        print("not")'''
'''a=[]
n=int(input("enter no: of elements"))
print("enter elements")
for i in range(0,n):
    k=int(input())
    a.append(k)
i=0
while i<n-1:
    j=i+1
    while j<n:
        if a[i]==a[j]:
            a.pop(j)
            n=n-1

        else:
            j+=1
    i+=1
print(a)
'''
a=[]
n=int(input("enter num elements"))
print("enter elements")
for i in range(0,n):
    k=int(input())
    a.append(k)
ind=int(input("enter index"))
for i in range(ind,n-1):
    a[i]=a[i+1]
    
print("hai",a[i])
n=n-1
print("list elem")
for i in range(0,n):
    print(a[i])