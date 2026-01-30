class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B 

    def Display(self):
        print("Account holder name is: ",self.Name)
        print("Current balance is: ",self.Amount)

    def Deposit(self):
        print("Enetr the amount: ")
        amt = int(input())
        self.Amount += amt
        print("Deposited Amount is: ",amt)
        print("Total amount is: ",self.Amount)

    def Withdraw(self):
        print("Enetr the amount: ")
        WtdAmt = int(input())
        self.Amount -= WtdAmt
        print("Withdrawn Amount is: ",WtdAmt)
        print("Total amount is: ",self.Amount)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interst is: ",Interest)
                                                                                                                                                                                

obj1 = BankAccount("Siddhi", 10000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("XYZ", 20000)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()

