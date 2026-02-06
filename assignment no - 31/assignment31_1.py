import os
import sys
import time

def DirectoryFileSearch(Extension, DirName = "Marvellous"):
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
            FName = os.path.join(FolderName, FName)
            
            if FName.endswith(Extension):
                fobj.write(FName + "\n")



   fobj.close()


def main():
    if(len(sys.argv)!= 2):
        print("Invalid number of arguments ")
        print("Please specify the directory name properly")
        return

    Extension = input("Eneter file extension (e.g. .txt, .log, .py): ")
    
    DirectoryFileSearch(Extension,sys.argv[1])


if __name__ == "__main__":
    main()