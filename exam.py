'''lis=[1,6,7,8,9,10]
i=1
while i<len(lis):
    print(lis[i])
    i=i+2'''

'''lis2=[2,1,4,3,6,5]
i=0
t=0
while i<len(lis2):
    if lis2[i] > lis2[i+1]:
     t=lis2[i]
     lis2[i]=lis2[i+1]
     lis2[i+1]=t
     i = i + 1
     print(lis2)'''





'''n=int(input("enter number"))
cube=0
for x in range(1,n+1):
    cube=x**3
    print(cube)'''

'''li=[1,4,3,2,5]
temp=0
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            temp=li[i]
            li[i]=li[j]
            li[j]=temp
print("after sorted")
for i in range(0,len(li))  :
    print(li[i])'''


'''for i in range(1500,2700):
    if i%7==0 and  i%5==0:
        print(i)'''
'''def fact():
    n=int(input("enter limit"))
    i=1
    fac=1
    while i<=n:
        fac=fac*i
        i=i+1
    #print(fac)
    return fac'''

# print("fact",fact())

'''def mul(a):
    pro=1
    for i in a:
        pro=pro*i
    return pro
list1=[2,3,5,6,7]
print("product is",mul(list1))'''

'''def test(a):
    print(a)
    def sum():
        print("hai")
    sum()


test(5)'''

'''li=[]
for i in range(4,30,2):

    li.append(i)
print(li)'''











