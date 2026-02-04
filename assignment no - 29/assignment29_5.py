import os


def CntFreqString():
    FileName = input("Enetr the file name: ")
    Word = input("Enter the word to search: ")
    
    Result1 = os.path.exists(FileName)
    if(Result1 == False):
        print("There is no such file")
        return
    
    file = open(FileName, "r")
    Data = file.read()

    Cnt = 0
    wordlist = Data.split()

    for i in wordlist:
        if(i == Word):
            Cnt += 1
    
    return Cnt
    
def main():
    Result = CntFreqString()
    print("The count of the word in the file is: ",Result)

if __name__ == "__main__":
    main()