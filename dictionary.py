dic={1:"anu",2:"ammu"}
print(dic)
print(dic[1])
dic2=dict({"name":"aami","age":21,"mark":32.5})
print(dic2)
print(dic2.get("age"))
dic["state"]="kerala"
print(dic)
print(dic.pop("state"))
print(dic)
dic2.popitem()
print(dic2)
dic2.clear()

print(dic2)

#fromkeys

marks={}.fromkeys(["maths","english","hindi"],90)
print(marks)