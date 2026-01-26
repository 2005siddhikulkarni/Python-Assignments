def LenOfStr(STR):
    Cnt = 0

    for i in range(len(STR)) :
        Cnt += 1
    return Cnt

    
def main():
    print("Enter the string: ")
    Name = input()

    Result = LenOfStr(Name)
    print(Result)
    
if __name__ == "__main__":
    main()