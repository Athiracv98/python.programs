'''def func(*x):
    print(x[2])
func(1,2,3,4)'''
import calendar

'''def strfunc():
    s="HAPPY newYear"
    l=0
    c=0

    for i in s:
        if i.isupper():
            c=c+1
        elif i.islower():
          
            l=l+1
    print("upper count",c)
    print("lower count",l)
strfunc()'''
#arb
'''def keyar(**x):
    print(x['a'])
keyar(a='name',b=20)'''

# lii=[2,5,6,3,2,6,5,3]
# lis=[]
# se=set(lii)
# lii=list(se)
# for i in lii:
#     lis.append(i)
# print(lis)
#     lis.append(i)
#     l=lii.count(i)
#     if l==2:
#         r=lii.remove(i)
# print(lii)
#    # lis.append(i)

# lis=[1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17]
# for i in range(22,2,-2):
#     if i%2==0:
#       print(i)


# yy=int(input("enter year"))
# mm=int(input("enter month"))
# print(calendar.month(yy,mm))

#take count of upper and lower letters
'''def strfunc():
    s = "HAPPY newYear"
    l = 0
    c = 0
    i=0
    while i<len(s):
        if s[i].isupper():
            c = c + 1
        elif s[i].islower():

            l = l + 1
        i=i+1
    print("upper count", c)
    print("lower count", l)


strfunc()'''

# def keyw(a,b):
#     print(a,b)
# keyw()

'''def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)


print("fact is",fact(4))'''

wor="howareyou"
v=0
c=0

for i in wor:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        v=v+1

    else:
        c=c+1
print("count of consantants", c)
print("count of vowels", v)






