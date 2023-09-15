# calculate interset

class BankAccount:
    accountnumber=""
    balance=""
    def __init__(self,accountno,balance):
        self.accountnumber=accountno
        self.balance=balance
    def checkbalance(self):
        print(f"account number:{self.accountnumber}\t\tbalance:{self.balance}")
class SavingsAccount(BankAccount):

    r=0
    t=0
    def calculate_interest(self,r):
        interst=self.balance*(r/100)
        return interst
s=SavingsAccount(4000,3748)

s.checkbalance()
print("interest",s.calculate_interest(2))

# person problem

'''class person:
    name=""
    age=""
    def introduce(self):
        print(f"my name is{self.name} and iam {self.age} years old")
class student(person):
    stud_id=""
    def introduce(self,stud_id):
        self.stud_id=stud_id
        print(f"my name is{self.name} and iam {self.age} years old and my student id is{self.stud_id}")

'''










