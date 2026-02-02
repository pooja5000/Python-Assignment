# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# If both files contain the same contents, display Success
# Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure


import os
import sys

def CheckFile(file1,file2):
    


    
    
    if (os.path.exists(file1)==True) and os.path.exists(file2):
        fobj1=open(file1,"r")
        fobj2=open(file2,"r")
        data1=fobj1.read()
        data2=fobj2.read()
        if data1==data2:
            print("Content of file is matching")

        else:
            print("Contents are Different")
        


        

    else:
        print("File is not present")
        

    

def main():
    if len(sys.argv)!=3:
        print("Invalid no of arguments")
        return
    CheckFile(sys.argv[1],sys.argv[2])
    
    
 
if __name__=="__main__":
    main()