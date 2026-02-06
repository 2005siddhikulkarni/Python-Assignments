import os
import hashlib
import time
import sys

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    while(Buffer):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicateRemoval(DirName):

    timestamp = time.ctime()
    LogFileName = "DirName%s.log" % timestamp
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    fobj = open(LogFileName, "a")

    if not os.path.exists(DirName):
        fobj.write("There is no such directory\n")
        return

    if not os.path.isdir(DirName):
        fobj.write("It is not a directory\n")
        return

    CheckSumDict = {}

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for FName in FileName:
            FilePath = os.path.join(FolderName, FName)

            CheckSum = CalculateCheckSum(FilePath)

            if CheckSum in CheckSumDict:
                os.remove(FilePath)
                fobj.write("Duplicate file deleted: " + FilePath + "\n")
            else:
                CheckSumDict[CheckSum] = FilePath

    fobj.close()

def main():
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the directory name properly")
        return

    DirectoryDuplicateRemoval(sys.argv[1])

if __name__ == "__main__":
    main()
