'''class Student:
    name=""
    age=0
    height=""
    def display(self):
        print (f" Name:{self.name} age:{self.age} height:{self.height}")
s=Student()
s.name=input("enter name")

s.age=int(input("enter age"))
s.height=input("enter height")
s.display()'''
bus={"routeno":5,"driver":"kiran","cleaner":"manu","points":["karamana","PMG","PATTOM"]}
print(bus["driver"])
print(bus.get("driver"))
print(bus.keys())
print(bus.values())
print(bus.items())
bus["driver"]="mohan"
bus["color"]="red"
print(bus)
bus.pop("color")
bus.popitem()
print(bus)


for x in bus:
    print(x)
for x in bus:
    print(bus[x])
