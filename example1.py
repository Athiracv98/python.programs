'''student={"name":"kiran","age":25,"mark1":76,"mark2":85}
print(student["name"])
student.update({"name":"athira"})
print(student)
c=student.copy()
print(c)
ca=dict(student)
print(ca)'''
# positional values
'''numbernames={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:"eight",9:'nine'}
positionvalues={0:"ones",1:"tens",2:"hundreds",3:"thousands",4:"ten thousands",5:"lakhs",6:"ten lakhs" ,7:"crore",8:"ten crore"}
num=input("enter any number")
result=""
l=len(num)-1
for i in num:
    key=int(i)
    value=numbernames[key]
    result=result+' '+value+' '+positionvalues[l]
    l-=1
print("the number is",num)
print("the result is",result)
'''
# electricity bill
'''unit=int(input("enter the unit"))
if unit<=100:
    charge=unit*1
elif unit<=150:
    charge=(100*1)+(unit-100)*1.5
elif unit<=200:
    charge=(100*1)+(50*1.5)+(unit-150)*2
else:
    charge=(100*1)+(50*1.5)+(50*2)+(unit-200)*3
print(charge)'''

'''l="hai hello"
s=""
for i in l:
    if i==" ":
        continue
    else:
        s=s+i
print(s)'''

'''n=int(input("enter a number"))
for i in range(1,11):
    print(i,"*",n,"=",i*n)'''

'''n=int(input("enter"))
arm=0
a=n
m=len(str(n))
while n>0:
    rem=n%10

    arm=arm+(rem**m)

    n=n//10

if a==arm:
    print("arm")
else:
    print("not")'''

n=int(input("enter num"))

h=[]
for i in range(2,n+1):
    for j in range(2,n):
        if i%j==0:
            h.append(i)
            break
print(h)








