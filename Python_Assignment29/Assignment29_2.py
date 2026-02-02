# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console
import os
import sys

def CheckFile(filename):
    ret=os.path.exists(filename)

    if (ret==True):
        fobj=open(filename,"r")
        print(fobj.read())

    

def main():
    filename=input("Enter file name:")
    CheckFile(filename)
    
    
 
if __name__=="__main__":
    main()