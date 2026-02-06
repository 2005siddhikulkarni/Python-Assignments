import os
import hashlib
import time
import sys

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)   # Data

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryCheckSum(DirName):
    
    timestamp = time.ctime()

    LogFileName = "DirName%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    
    LogFileName = LogFileName.replace(":", "_")
    fobj = open(LogFileName, "a")

    Result1 = os.path.exists(DirName)
    if(Result1 == False):
        fobj.write("There is no such directory")
        return
   
    Result2 = os.path.isdir(DirName)
    if(Result2 == False):
        fobj.write("It is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for FName in FileName:
            FilePath = os.path.join(FolderName, FName)

            Ret = CalculateCheckSum(FilePath)

            fobj.write(FilePath + ":" + Ret + "\n")
        
    fobj.close()

def main():
    if(len(sys.argv)!= 2):
        print("Invalid number of arguments ")
        print("Please specify the directory name properly")
        return
    
    DirectoryCheckSum(sys.argv[1])




if __name__ == "__main__":
    main()