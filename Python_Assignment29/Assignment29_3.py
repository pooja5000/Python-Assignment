# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt
import os
import sys

def CheckFile(filename):
    ret=os.path.exists(filename)


    
    
    if (ret==True):
        fobj=open("Demo.txt","w")
        fobj1=open(filename,"r")
        data=fobj1.read()
        fobj.write(data)

        print("File copied sucussfully............")
        

    

def main():
    
    if len(sys.argv)!=2:
        print("Invalid no of arguments")
        return
    CheckFile(sys.argv[1])
    
    
 
if __name__=="__main__":
    main()