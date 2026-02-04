import os

def CopyFileToAnotherFile():
    FileName1 = input("Enter the first file name: ")

    Result1 = os.path.exists(FileName1)
    if(Result1 == False):
        print("There is no such file exists")
        return
    
    FileName2 = input("Enter the second file name: ")

    Result2 = os.path.exists(FileName1)
    if(Result2 == False):
        print("There is no such file exists")
        return
    
    file1 = open(FileName1, "r")
    Data1 = file1.read()

    file2 = open(FileName2, "w")
    Data2 = file2.write(Data1)

def main():
    CopyFileToAnotherFile()

    print("File gets successfully copied into another file")
    
if __name__ == "__main__":
    main()