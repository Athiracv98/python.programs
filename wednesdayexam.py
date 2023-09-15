# sum of even number
n=int(input("enter the limit"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
print(sum)

# biggest
n=input("enter the number")
big=n[0]
for i in n:
    if int(i)>int(big):
        big=int(i)
print(big)

n=input("enter number")
sum=0
for i in n:
    sum=sum+int(i)
print(sum)
if sum>9:
    su=0
    for i in str(sum):
        su=su+int(i)

    print(su)
    sum = su





'''n=input("enter number")
sum=0
for i in n:
    sum=sum+int(i)
n=str(sum)
totsum=0
if len(n)>=2:
    for i in n:
        totsum=totsum+int(i)
    print(totsum)'''















