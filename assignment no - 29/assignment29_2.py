import os

def DisplayFileContents():
    FileName = input("Enter the file name: ")
    Result = False

    Result = os.path.exists(FileName)
    if(Result == False):
        print("There is no such file")
        return

    file = open(FileName, "r")
    Data = file.read()

    print(Data)

def main():
    DisplayFileContents()

if __name__ == "__main__":
    main()