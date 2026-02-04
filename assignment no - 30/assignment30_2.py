import os

def CntWordsInFiles():
    FileName = input("Enter the file name: ")

    Result = os.path.exists(FileName)
    if(Result == False):
        print("There is no such file exists")
        return
    
    file = open(FileName, "r")
    Data = file.read()
    Words = Data.split()
    
    Cnt = 0
    for i in Words:
        Cnt += 1
    return Cnt

def main():
    Ret = CntWordsInFiles()
    print("Count of lines in file is: ",Ret)

if __name__ == "__main__":

    main()
