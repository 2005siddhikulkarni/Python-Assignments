import os
import sys

def CompareContentsFile(FileName1, FileName2):
    
    Result1 = os.path.exists(FileName1)
    if(Result1 == False):
        print("There is no such file")
        return
    
    Result2 = os.path.exists(FileName2)
    if(Result2 == False):
        print("There is no such file")
        return

    file1 = open(FileName1, "r")
    Data1 = file1.read()
    
    file2 = open(FileName2, "r")
    Data2 = file2.read()

    if(Data1 == Data2):
        print("Success")

    else:
        print("Failure")
    
    

def main():
    CompareContentsFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()