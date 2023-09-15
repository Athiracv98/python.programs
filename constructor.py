class person:
    name=""
    gender=""
    __company="oneteam"
    def __init__(self):
        self.name="ammu"
        self.gender="female"
    def __test(self):
        print("hello")
    def display(self,greet):
        self .__test()
        return f" greetings:{greet} name:{self.name}\ngender:{self.gender}\ncompany:{self.__company}"
d=person()
# d.__company="tcs"---never work because company is a private variable
# d.__test() it will show error because we cant call private declared function using object
d.name="athi"
d.gender="female"
print(d.display("hai"))

'''class bankaccount:
    __name=""
    __balance=""
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def deposit(self,money):
        self.__balance+=money

    def withdraw(self,money):
        if self.__balance>money:
            self.__balance-= money
            return money
        else:
            return "insufficient"
    def checkbalance(self):
       return self.__balance
    def accountname(self):
        return self.__name
b=bankaccount("athira",500)
print(b.checkbalance())
print(b.accountname())
b.deposit(2000)
print("balance:",b.checkbalance())
print("money:",b.withdraw(1000))
print(b.checkbalance())
print("money:",b.withdraw(2000))
print(b.checkbalance())'''


class vehicle:
    model=""
    nooftyres=0
    company=""
    def run(self):
        print("run vehicle")
    def printall(self):
        print(f"model:{self.model} \nno of tyres:{self.nooftyres} \ncompany:{self.company} \n")
class car(vehicle):
    def test(self):
        print("from car")

class bike(vehicle):
    def demo(self):
        print("from bike")
c=car()
c.test()
c.model="82918"
c.nooftyres=6
c.company="kok"
c.run()
c.printall()


b=bike()
b.demo()
b.run()
b.model="89809"
b.nooftyres=8
b.company="jwf"
b.printall()




