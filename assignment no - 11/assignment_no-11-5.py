
def PalindromeNO(Value1):
    Original = Value1
    Rev = 0
    while Value1 > 0 :
        Digit = Value1 % 10
        Rev = Rev * 10 + Digit
        Value1 = Value1 // 10
    
    if Original == Rev :
        Ans = print("Palindrome number")

    else :
        Ans = print("Not a Palindrome number")

        return Ans

def main():
    No1 = print("enter the number: ")
    No1 = int(input())

    Result = PalindromeNO(No1)
    
if __name__ == "__main__":
    main()