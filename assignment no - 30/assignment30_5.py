import os

def SearchWordInFile():
    FileName = input("Enter the file name: ")

    Result = os.path.exists(FileName)
    if(Result == False):
        print("There is no such file exists")
        return
    
    Word = input("Enter the word to search: ")

    file = open(FileName, "r")
    Data = file.read()
    Ans = Data.split()

    Ret = False
    for i in Ans:
        if(i == Word):
            Ret = True
            break

        else:
            Ret = False

    if(Ret == True):
        print(Word,"is found in",FileName)

    else:
       print(Word,"is not found in",FileName) 
        
def main():
    SearchWordInFile()
    
if __name__ == "__main__":
    main()