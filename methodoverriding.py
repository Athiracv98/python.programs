class Person:
    name=""
    def whoami(self,greet="welcome",company="oneteam"):
        return self.name +" "+greet+" to company "+company
class Male(Person):
    pass
class Female(Person):
    def whoami(self, greet="welcome", company="oneteam"):
        return "from female class "+self.name + " " + greet + " to company " + company
p=Male()
p.name="hari"
print(p.whoami(company="tcs"))

f=Female()
f.name="ankhitha"
print(f.whoami(company="infosys"))


# abstraction
# ABS-Abstract Base class
# abc-is a module ,we want to import ABC CLASS FROM MODULE


'''from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class triangle(polygon):
    def noofsides(self):
        print("i have 3 sides")
class pentagon(polygon):
    def noofsides(self):
        print("i have 5 sides")
class Hexagon(polygon):
    def noofsides(self):
        print("i have 6 sides")
t=triangle()
t.noofsides()
p=pentagon()
p.noofsides()
h=Hexagon()
h.noofsides()
'''




