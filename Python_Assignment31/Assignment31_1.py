# 1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage: DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search
import os
import sys
from pathlib import Path

def fileExtSearch(fileext,Directory):

    if os.path.exists(Directory)==False:
        print("This directory is not present")
        return

    if os.path.isdir(Directory)==False:
        print("This is not directory")
        return

    fobj=open("marvellous.log","w")
    fobj.write("----------------Assignment 31--------------"+"\n")
    for folder,subfolder,file in os.walk(Directory):

        for subfolder_name in subfolder:
             fobj.write("Sub directory is:"+subfolder_name+"\n")

        for fname in file:
            #filename=os.path.join(fname,folder)
            if fname.endswith(fileext):
                fobj.write("File with extesion .txt:")
                fobj.write(fname+"\n")

    fobj.write("------------------Thank you-----------------")

def main():

    if len(sys.argv)!=3:
        print("Invalid no of arguments")
        return
    
    fileExtSearch(sys.argv[1],sys.argv[2])
    

if __name__=="__main__":
    main()