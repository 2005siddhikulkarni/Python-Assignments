import os
import sys

def CopyContentsInFile(FileName1):
    
    Result = False

    Result = os.path.exists(FileName1)
    if(Result == False):
        print("There is no such file")
        return

    file1 = open(FileName1, "r")
    Data = file1.read()
    file1.close()

    file2 = open("Demo.txt", "w")
    Ret = file2.write(Data)
    
    print("File gets copied successfully ")

    file2.colse()

def main():
    CopyContentsInFile(sys.argv[1])

if __name__ == "__main__":
    main()