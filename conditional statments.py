'''a=int(input("enter number1"))
b=int(input("enter number1"))
c=int(input("enter number"))
if a>b and a>c:
    print("a is greater")
if b>a and b>c:
    print("b is greater")
else:
    print("c is greater")'''
'''a=int(input("enter number1"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")'''

'''hindi=int(input("enter mark of hindi"))
english=int(input("enter mark of english"))
malayalam=int(input("enter mark of malayalam"))
total=hindi+english+malayalam
print("total",total)
avg=total/3
print("average",avg)
if avg>90 and avg<=100:
    print("grade is A")
elif avg>80:
    print("grade is B")
elif avg>70:
    print("grade is C")
elif avg>60:
    print(" grade is D")
elif avg>50:
    print("grade is E")
else:
    print("fail")'''

'''year=int(input("enter a year"))

if year%400==0 or year%4==0 and year%100!=0:
    print(year," is leap year")
else:
    print(year,"not leap year")'''
'''a=int(input("enter number"))
if a>0 :
    print(a,"is positive")
elif a<0:
    print(a,"is negative")
else:
    print(a,"is zero")'''


'''count=1
while count<=500:
    print(count)
    count+=1'''

'''mytup1=(23,45,67,89)
i=0
while i< len(mytup1) :
    print(mytup1[i])
    i+=1'''
'''lis3=[1,2,3]
sum=0
i=0
while i<len(lis3) :
    sum=sum+lis3[i]
    i+=1
print("sum",sum)'''

word="python"
print(len(word))
i=0
while i<len(word):
    if word[i]=="y" or word[i]=="h":
      i=i+1
      continue
    print(word[i])
    i=i+1
#while i<len(word) :

'''for x in range(1,10):
    print(x)'''
'''lis=[1,2,3,4]
newli=[]
for x in lis:
    y=x**2
    newli.append(y)
print(newli)

x=[23,"python",23.98]
newl=[]
for i in x:

    newl.append(type(i))

print(newl)'''

'''listt=[1,2,3,4,5,6,7,8,9]
odd=[]
even=[]
for x in listt:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(odd)
print(even)'''

'''n=int(input("enter the limit"))
i=1
fact=1

if n<0:
    print("factorial does not exist for negative number")
elif n==0:
    print("factorial is 1")
else:
 while i <= n:
    fact=fact*i
    i+=1
 print("fact is",fact)'''

'''for i in range(7,10):
    print("output based questions")'''
'''for i in  range(2,3,4):
    print("i")'''

'''for i in range(7,-2,-9):
    for j in range(i):
      print(i)'''

'''i=8
for k in range(i):
    print(k)'''












