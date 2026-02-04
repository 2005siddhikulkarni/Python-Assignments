import os

def DisplayLinesInFiles():
    FileName = input("Enter the file name: ")

    Result = os.path.exists(FileName)
    if(Result == False):
        print("There is no such file exists")
        return
    
    file = open(FileName, "r")
    
    for i in file:
        print(i,end="")

def main():
    DisplayLinesInFiles()
    

if __name__ == "__main__":
    main()