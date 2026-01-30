class Numbers:
    ROI = 10.5

    def __init__(self,A):
        self.Value = A 

    def ChkPrime(self):
       Cnt = 0
       if self.Value <= 1:
           return False
       
       for i in range(1,self.Value + 1):
           if self.Value % i == 0:
               Cnt += 1

       if Cnt == 2:
           return True
       
       else:
           return False
       
    def ChkPerfect(self):
         Sum = 0
         for i in range(1,self.Value + 1):
           if self.Value % i == 0:
               Sum += i

         if self.Value == Sum:
           return True
       
         else:
           return False
           
    def Factors(self):
        for i in range(1,self.Value + 1):
           if self.Value % i == 0:
               print(i)

    def SumOfFactors(self):
        Sum = 0
        for i in range(1,self.Value + 1):
           if self.Value % i == 0:
               Sum += i

        print("Sum of factors is: ",Sum)                                                                                                                                                                  

obj1 = Numbers(2)
print("Prime: ",obj1.ChkPrime())
print("Perfect is: ",obj1.ChkPerfect())
obj1.Factors()
obj1.SumOfFactors()

obj2 = Numbers(6)
print(obj2.ChkPrime())
print(obj2.ChkPerfect())
obj2.Factors()
obj2.SumOfFactors()

