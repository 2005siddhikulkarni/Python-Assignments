def ChkPrime(Num):
    Cnt = 0
    if Num <= 1:
        return False
    
    for i in range(1,Num+1):
        if Num % i == 0:
            Cnt += 1
    
    
    if Cnt == 2:
        return True
    
    else:
        return False