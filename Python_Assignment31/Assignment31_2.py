# 2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extenntion.
# Usage: DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with.doc
import os
import sys
from pathlib import Path

def fileExtSearch(Directory,fileext1,fileext2):

    if os.path.exists(Directory)==False:
        print("This directory is not present")
        return

    if os.path.isdir(Directory)==False:
       print("This is not directory")
       return

    fobj=open("marvellous.log","w")
    fobj.write("----------------Assignment 31--------------"+"\n")
    
    for folder,subfolder,file in os.walk(Directory):

        for fname in file:
            name,fileext1=os.path.splitext(fname)

            if fileext1==fileext1:
                oldpath=os.path.join(Directory,fname)
                newfile=name+fileext2
                newpath=os.path.join(Directory,newfile)
                
            if fname!=newfile:
                os.rename(oldpath,newpath)
                fobj.write(fname+"-->"+newfile+"\n")
                return
    # fobj.write("------------------Thank you-----------------")

def main():

    if len(sys.argv)!=4:
        print("Invalid no of arguments")
        return
    
    fileExtSearch(sys.argv[1],sys.argv[2],sys.argv[3])
    

if __name__=="__main__":
    main()