import os

def ChkFile():
    FileName = input("Enter the file name: ")
    
    Result = os.path.exists(FileName)

    if(Result == True):
        print("File Exists")

    else:
        print("There is no such file")

def main():
    ChkFile()

if __name__ == "__main__":
    main()