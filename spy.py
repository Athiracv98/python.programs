'''n=input("enter a number")
sum=0
pro=1
for i in n:
    sum=sum+int(i)
print("sum:",sum)
for i in n:
    pro=pro*int(i)
print("product:",pro)
if sum==pro:
    print(n,"number is spy")
else:
    print("number is not spy")


n=input("enter a number")

list=[]
fact=1
sum=0
for i in n:
    fact=1
    for j in range(1,int(i)+1):
        fact=fact*j
    list.append(fact)

for x in list:
    sum=sum+x;
print("sum is",sum)
if sum==int(n):
    print("strong number")
else:
    print("not strong")
'''

# print(dir(str))
'''def capital_indexes(a):
    n=len(a)
    l=[]
    for i in range(len(a)):
        if a[i].isupper():
            l.append(i)
    return l

print(capital_indexes("HellWFHTH"))'''
'''def mid(a):
    v=len(a)
    m=10**v

    if v%2==0:
        return ""
    else:
        n=v//2
        print(a[n])





mid("abcde")'''

# s='haI'
# n=len(s)
# print(n)
# for i in range(0,n):
#     print(i)
'''def online_count(a):

    count=0
    for i in a:

        if a[i]=='online':
            count+=1
    return count



statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "offline",
}
print("count",online_count(statuses))'''

'''import random
def random_number():

    return random.randint(1,100)  
print(random_number())'''

'''def only_inits(a,b):

    m=type(a)
    n=type(b)
    if m==n:
        return True
    else:
       return False

print(only_inits(1,'a'))'''

'''def double_letters(a):
    v=len(a)
    print(v)
    count=0

    for i in range(v-1):

        print(a[i],a[i+1])
        if a[i]==a[i+1]:
            count=count+1
    print(count)

    if count>0:
        return True
    else:
        return False


print(double_letters("manu"))
'''
# stri=stri+i.__add__(".")
# def add_dots(a):
#
#     s='.'.join(a)
#     print(s)
#
# add_dots("test")


'''def add_dots(a):
    s = '.'.join(a)
    return s
def remove_dots(s):

    stri = ""
    for i in s:

        if i == '.':
            continue
        else:
            stri = stri + i
    return stri
print(remove_dots(add_dots("test")))'''

'''def add_dots(a):
    str=""
    for i in a:
        str=str+(i+'.')

    print(str[:-1])
add_dots("test")
'''

'''def count(a):
    cou=1

    for i in a:
        if i=='-':
            cou=cou+1
    return cou


print(count("ho-tel"))
def count(a):
   # print(len(a.split("-")))
   print(a.count("-")+1)
count("met-a")'''
# print(dir(str))
# return True
#         else:
#             return False
'''def is_anagram(a,b):
    count=0
    for i in a:
        if i not in b:
            count=count+1
    print(count)


    if count>0:
        return False
    else:
        return True



print(is_anagram('abc','cac'))
'''
# for j in b:
#     count=0
#     if j in li:

# def is_anagram(a,b):
#     co = 0
#     for i in a: 
#         for j in b:
#
#             if i==j and a.count(i) == b.count(j) and len(a)==len(b):
#                 co=co+1
#     if co>=len(a):
#        return True
#     else:
#         return False
#
#
# print(is_anagram('abc', 'abc'))
'''def count_letters(string):
    return {l: string.count(l) for l in string}

def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
print(is_anagram("test","stet"))
print(count_letters("test"))
'''
'''def is_anagram(string1, string2):
    print (sorted(string1))
    print(sorted(string2))
    if sorted(string1)==sorted(string2):
        print("true")
    else:
        print("false")
is_anagram("test","stet")
'''

'''def flatten(a):
    li=[]
    for i in a:
        for j in i:
            li.append(j)
    return li

print(flatten([[1,2],[3,4]]))'''
# def largest_difference(a):
#     b=a[0]
#     s=a[0]
#     for i in a:
#         if i>b:
#             b=i
#         if i<s:
#             s=i
#
#     return b-s
#
# print(largest_difference([5,4,1]))
'''def div_3(a):
    if a%3==0:
        return True
    else:
        return False
print(div_3(5))'''

def get_row_col(a):
    v=a.upper()
    m=[]
    y=[]
    row=0
    col=0

    di = {'A': 0, 'B': 1, 'C': 2}
    for i in v:
        if i.isalpha():
            m.append(i)

    for r in a:
        if r.isdigit():
            y.append(r)

    for j in di:
        for x in m:
            if j==x:
                col=di[j]

    for z in y:
        row=int(z)-1
    tup=(row,col)
    return tup

print(get_row_col("a1"))
