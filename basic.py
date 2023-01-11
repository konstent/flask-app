class Account:
     def __init__(self,owner,balance):
         self.owner = owner
         self.balance = balance
    
     def __repr__(self):
         return f"Account Owner: {self.owner}\nBalance: {self.balance}"
         
     def deposit(self, dep_amt):
         self.balance = self.balance + dep_amt
         print("Deposit is Succesfull")
         
     def Withdrawal(self,withdraw_amt):
         if withdraw_amt > self.balance:
             print("Withdrawal is not possible, Funds Unavailable :(")
         else:
             self.balance = self.balance - withdraw_amt
             print("Withdrawal is Successful :)")
    
Acc1 = Account('Taha',200)
print(Acc1)
Acc1.deposit(200)
Acc1.Withdrawal(100)
Acc1.Withdrawal(1000)

