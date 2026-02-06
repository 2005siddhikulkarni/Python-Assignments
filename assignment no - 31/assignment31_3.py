import os
import sys
import time

def DirectoryCopy(DirName1, DirName2):
   timestamp = time.ctime()

   LogFileName = "DirName%s.log" %(timestamp)
   LogFileName = LogFileName.replace(" ","_")
    
   LogFileName = LogFileName.replace(":", "_")
   fobj = open(LogFileName, "a")

   Result1 = os.path.exists(DirName1)
   if(Result1 == False):
        fobj.write("There is no such directory")
        return
   
   Result2 = os.path.isdir(DirName1)
   if(Result2 == False):
        fobj.write("It is not a directory")
        return
   
   Result3 = os.path.exists(DirName2)
   if(Result3 == False):
        os.mkdir(DirName2)
        fobj.write("Second directory is created")
        
   Result4 = os.path.isdir(DirName2)
   if(Result4 == False):
        fobj.write("It is not a directory")
        return
    
   for FolderName, SubFolderName, FileName in os.walk(DirName1):
        for FName in FileName:
           Src_Path = os.path.join(FolderName, FName)
           DestPath = os.path.join(DirName2, FName)

           Src_File = open(Src_Path, "rb")
           Dest_File = open(DestPath, "wb")

           Files = Src_File.read()
           Copied_Files = Dest_File.write(Files)

           Src_File.close()
           Dest_File.close()

           fobj.write(Src_Path + "gets successfully copies to " + DestPath + "\n")

def main():
    if(len(sys.argv)!= 3):
        print("Invalid number of arguments ")
        print("Please specify the directory name properly")
        return
    
    DirectoryCopy(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()