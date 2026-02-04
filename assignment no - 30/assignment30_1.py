import os

def CntLinesInFiles():
    FileName = input("Enter the file name: ")

    Result = os.path.exists(FileName)
    if(Result == False):
        print("There is no such file exists")
        return
    
    file = open(FileName, "r")
    
    Cnt = 0
    for i in file:
        Cnt += 1
    return Cnt

def main():
    Ret = CntLinesInFiles()
    print("Count of lines in file is: ",Ret)

if __name__ == "__main__":

    main()
