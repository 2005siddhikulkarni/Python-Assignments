import os
import sys
import time

def DirectoryRename(Ext1,Ext2,DirName = "Marvellous"):
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
            OldPath= os.path.join(FolderName, FName)
            
            if FName.endswith(Ext1):
                New_FName = FName.replace(Ext1, Ext2)
                NewPath= os.path.join(FolderName,New_FName)

                os.rename(OldPath, NewPath)

                fobj.write(NewPath + "\n")

   fobj.close()


    


def main():
    if(len(sys.argv)!= 2):
        print("Invalid number of arguments ")
        print("Please specify the directory name properly")
        return

    Extension1 = input("Eneter the first file extension (e.g. .txt, .log, .py) which will get replaced: ")
    Extension2 = input("Eneter the second file extension (e.g. .txt, .log, .py) which will be new : ")
    
    DirectoryRename(Extension1, Extension2)


if __name__ == "__main__":
    main()